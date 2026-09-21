"""
Analise do funil comercial a partir do export Excel do Goalfy (board de vendas).

Uso:
    python analise_funil_goalfy.py caminho_do_arquivo.xlsx [--mes AAAA-MM]

Sem --mes, analisa a base inteira (com segmentacao Base Antiga vs funil ativo).
Com --mes, filtra os leads criados naquele mes (ex.: --mes 2026-08) e roda
o mesmo diagnostico so para aquele recorte.

Gera um .json com todos os numeros na mesma pasta do script, pronto pra
ser lido e virar texto de diagnostico (nao tenta gerar prosa, so os fatos).
"""
import sys
import json
import argparse
from datetime import datetime
from collections import Counter

import openpyxl

ORDEM_FUNIL = [
    'Caixa de Entrada',
    'Contato Inicial',
    'Em Contato',
    'Qualificação',
    'Reunião Agendada',
    'No-show',
    'Oportunidade Gerada',
    'Lead Desqualificado',  # saida lateral, pode ocorrer a partir de qualquer fase
]


def parse_dt(v):
    if isinstance(v, datetime):
        return v
    if isinstance(v, str):
        for fmt in ('%d/%m/%Y %H:%M:%S', '%d/%m/%Y %H:%M', '%d/%m/%Y'):
            try:
                return datetime.strptime(v, fmt)
            except ValueError:
                pass
    return None


def to_float(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def bucket_fonte(f):
    if f is None:
        return 'Sem fonte (null)'
    if 'Base Antiga' in f:
        return 'Base Antiga (reativação)'
    if f == 'Outbound':
        return 'Outbound'
    if f in ('Meta_Ads', 'facebook', 'ig', 'fb', 'Instagram_Stories') or f.startswith('http'):
        return 'Inbound Ads/Social'
    if f in ('adwords', 'google_ads'):
        return 'Inbound Ads/Social'
    if f in ('Formulario_Instantaneo', 'Material Gratuito') or f.startswith('[JM]') or f.startswith('['):
        return 'Inbound Formulário/Site'
    if f in ('Referral', 'Feira - Gumz Transforma', 'direct', 'social'):
        return 'Outros Inbound'
    return 'Outros/Não classificado'


def _normaliza_unidade(v):
    """Normaliza grafias/typos de unidade de negocio (Goalfy/Goslfy, Educação/Educação SP,
    Hapo Assessoria/Assessoria) a partir de um valor de campo já preenchido."""
    if not v:
        return None
    vl = v.strip().lower()
    if 'goalfy' in vl or 'goslfy' in vl:
        return 'Goalfy'
    if 'assessoria' in vl:
        return 'Hapo Assessoria'
    if 'educa' in vl:
        return 'Hapo Educação'
    return None


def classificar_unidade(g):
    """Classifica um lead em Goalfy / Hapo Educação / Hapo Assessoria / Não classificado.

    Prioridade: campo explicito 'Unidade de Negócio' -> 'Etiqueta - Unidade de
    Negócio' -> heuristica por palavra-chave em Campanha/Fonte do Lead/Título do
    Evento. Mesmo com a heuristica, boa parte da base fica 'Não classificado' —
    o CRM não tagueia unidade de negocio de forma confiavel na maioria dos leads
    (ver README.md, seção de tagueamento). Isso é reportado, não escondido.
    """
    v = _normaliza_unidade(g('Unidade de Negócio'))
    if v:
        return v
    v = _normaliza_unidade(g('Etiqueta - Unidade de Negócio'))
    if v:
        return v
    for campo in ('Campanha', 'Fonte do Lead', 'Título do Evento'):
        val = g(campo)
        if not val:
            continue
        vl = val.lower()
        if 'goalfy' in vl:
            return 'Goalfy'
        if 'assessoria' in vl:
            return 'Hapo Assessoria'
        if 'educa' in vl or 'imers' in vl:
            return 'Hapo Educação'
    return 'Não classificado'


def stats(vals):
    vals = [v for v in vals if v is not None and v >= 0]
    if not vals:
        return None
    vals.sort()
    n = len(vals)
    return {
        'n': n,
        'mediana': round(vals[n // 2], 2),
        'media': round(sum(vals) / n, 2),
        'p25': round(vals[int(n * 0.25)], 2),
        'p75': round(vals[int(n * 0.75)], 2),
    }


def carregar_linhas(caminho_xlsx):
    wb = openpyxl.load_workbook(caminho_xlsx, data_only=True)
    ws = wb['Sheet']
    headers = [c.value for c in ws[1]]
    idx = {h: i for i, h in enumerate(headers)}
    rows = [r for r in ws.iter_rows(min_row=2, values_only=True)]
    return rows, idx


def analisar(rows, idx, agora=None):
    def g(r, h):
        return r[idx[h]]

    def ent(r, fase):
        return parse_dt(g(r, f'Primeira vez que entrou na fase {fase}'))

    is_base_antiga = lambda r: (g(r, 'Fonte do Lead') or '').__contains__('Base Antiga')
    ativo = [r for r in rows if not is_base_antiga(r)]

    out = {'total_linhas': len(rows), 'total_ativo_sem_base_antiga': len(ativo)}

    # fase atual (estado presente)
    out['fase_atual'] = Counter(g(r, 'Fase Atual') for r in rows).most_common(20)

    # classificacao por unidade de negocio, no recorte ativo (ver classificar_unidade
    # para a ordem de prioridade dos campos usados; "Não classificado" é esperado
    # ser uma fatia grande hoje, é um problema de tagueamento no CRM, não bug daqui)
    out['classificacao_unidade_ativo'] = Counter(
        classificar_unidade(lambda h, r=r: g(r, h)) for r in ativo
    ).most_common(10)

    # funil ever-entered por unidade de negocio (so nas unidades classificadas)
    por_unidade = {}
    for r in ativo:
        u = classificar_unidade(lambda h, r=r: g(r, h))
        if u == 'Não classificado':
            continue
        d = por_unidade.setdefault(u, {f: 0 for f in ORDEM_FUNIL})
        for f in ORDEM_FUNIL:
            if ent(r, f) is not None:
                d[f] += 1
    out['funil_por_unidade_negocio'] = por_unidade

    # funil ordenado por "ever entered", no recorte ativo
    out['ever_entered_ativo'] = {f: sum(1 for r in ativo if ent(r, f) is not None) for f in ORDEM_FUNIL}

    # tempo total na fase (mediana em dias, so valores > 0), recorte ativo
    tempo_fase = {}
    for fase in ORDEM_FUNIL:
        h = f'Tempo total na fase {fase}'
        vals = [to_float(g(r, h)) for r in ativo]
        vals = [v for v in vals if v is not None and v > 0]
        if vals:
            tempo_fase[fase] = stats(vals)
    out['tempo_na_fase_dias'] = tempo_fase

    # lead time total: criado -> oportunidade gerada
    lt = []
    for r in ativo:
        c = parse_dt(g(r, 'Criado em'))
        o = ent(r, 'Oportunidade Gerada')
        if c and o:
            lt.append((o - c).total_seconds() / 86400)
    out['lead_time_total_dias'] = stats(lt)

    # transicoes entre fases (dias)
    def transicao(a, b):
        vals = []
        for r in ativo:
            x, y = ent(r, a), ent(r, b)
            if x and y and y >= x:
                vals.append((y - x).total_seconds() / 86400)
        return vals

    out['transicoes_dias'] = {
        'Caixa de Entrada -> Contato Inicial': stats(transicao('Caixa de Entrada', 'Contato Inicial')),
        'Contato Inicial -> Qualificação': stats(transicao('Contato Inicial', 'Qualificação')),
        'Qualificação -> Reunião Agendada': stats(transicao('Qualificação', 'Reunião Agendada')),
        'Reunião Agendada -> Oportunidade Gerada': stats(transicao('Reunião Agendada', 'Oportunidade Gerada')),
    }

    # segmentacao por fonte (funil completo, todas as linhas)
    detail = {}
    for r in rows:
        b = bucket_fonte(g(r, 'Fonte do Lead'))
        d = detail.setdefault(b, {'total': 0, 'entrou_contato_inicial': 0, 'entrou_qualificacao': 0,
                                   'entrou_reuniao': 0, 'entrou_oportunidade': 0, 'entrou_desqualificado': 0})
        d['total'] += 1
        if ent(r, 'Contato Inicial'):
            d['entrou_contato_inicial'] += 1
        if ent(r, 'Qualificação'):
            d['entrou_qualificacao'] += 1
        if ent(r, 'Reunião Agendada'):
            d['entrou_reuniao'] += 1
        if ent(r, 'Oportunidade Gerada'):
            d['entrou_oportunidade'] += 1
        if ent(r, 'Lead Desqualificado'):
            d['entrou_desqualificado'] += 1
    out['segmentacao_por_fonte'] = detail

    # motivo de desqualificacao normalizado
    motivo = Counter()
    for r in rows:
        m = g(r, 'Motivo da desqualificação')
        if not m:
            continue
        ml = m.strip().lower()
        if 'icp' in ml:
            key = 'Fora do ICP'
        elif 'duplic' in ml:
            key = 'Duplicado'
        elif 'potencial' in ml or 'invest' in ml:
            key = 'Sem potencial de investimento'
        elif 'agencia' in ml or 'agência' in ml:
            key = 'É agência de marketing'
        else:
            key = m.strip()
        motivo[key] += 1
    out['motivo_desqualificacao_normalizado'] = motivo.most_common(20)

    # backlog: leads ainda na Caixa de Entrada, idade desde criacao (precisa de 'agora')
    if agora:
        parados = []
        for r in rows:
            if g(r, 'Fase Atual') == 'Caixa de Entrada':
                c = parse_dt(g(r, 'Criado em'))
                if c:
                    parados.append((agora - c).total_seconds() / 3600)
        parados.sort()
        if parados:
            out['backlog_caixa_de_entrada_horas'] = {
                'n': len(parados),
                'mediana_h': round(parados[len(parados) // 2], 1),
                'maior_24h': sum(1 for p in parados if p > 24),
                'maior_48h': sum(1 for p in parados if p > 48),
            }

    return out


def filtrar_mes(rows, idx, ano_mes):
    ano, mes = (int(x) for x in ano_mes.split('-'))
    c = idx['Criado em']

    def dt_no_mes(v):
        d = parse_dt(v)
        return d is not None and d.year == ano and d.month == mes

    return [r for r in rows if dt_no_mes(r[c])]


def filtrar_unidade(rows, idx, unidade):
    def g(r, h):
        return r[idx[h]]

    return [r for r in rows if classificar_unidade(lambda h, r=r: g(r, h)) == unidade]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('xlsx')
    parser.add_argument('--mes', help='AAAA-MM, ex.: 2026-08')
    parser.add_argument('--unidade', help='Goalfy | Hapo Educação | Hapo Assessoria (filtra so essa unidade)')
    parser.add_argument('--agora', help='DD/MM/AAAA HH:MM:SS, timestamp de referencia p/ backlog (default: max Criado em do arquivo)')
    parser.add_argument('--out', default='analise_saida.json')
    args = parser.parse_args()

    rows, idx = carregar_linhas(args.xlsx)

    agora = parse_dt(args.agora) if args.agora else max(
        (parse_dt(r[idx['Criado em']]) for r in rows if parse_dt(r[idx['Criado em']])), default=None
    )

    if args.mes:
        rows = filtrar_mes(rows, idx, args.mes)

    if args.unidade:
        rows = filtrar_unidade(rows, idx, args.unidade)

    resultado = analisar(rows, idx, agora=agora)

    with open(args.out, 'w', encoding='utf-8') as f:
        json.dump(resultado, f, ensure_ascii=False, indent=1, default=str)

    print(f'OK - {len(rows)} linhas analisadas -> {args.out}')


if __name__ == '__main__':
    main()
