import json
import os

BASE = os.path.join(os.path.dirname(__file__), '..', 'Analises', '2026-08-13')


def w(n, base):
    if base == 0 or n == 0:
        return "0%"
    return f"{(n/base*100):.1f}%"


def pct_br(x):
    return f"{x:.1f}".replace('.', ',') + '%'


UNITS = [
    ("Goalfy", "u-goalfy", "Goalfy", "metas: qualificação 30% · fechamento 40%", 30, 40),
    ("Hapo_Educação", "u-educacao", "Hapo Educação", "metas: qualificação 40% · fechamento 30%", 40, 30),
    ("Hapo_Assessoria", "u-assessoria", "Hapo Assessoria", "sem meta definida — contexto", None, None),
]


def rate_class(rate, meta):
    if meta is None or rate is None:
        return ""
    if rate >= meta:
        return "good"
    if rate >= meta * 0.7:
        return "warning"
    return "critical"


def mini_row(label, n, base, cssvar):
    return (
        '          <div class="mini-row">\n'
        f'            <span class="mini-label">{label}</span>\n'
        f'            <div class="mini-track"><div class="mini-fill" style="width:{w(n, base)}; background:var(--{cssvar})"></div></div>\n'
        f'            <span class="mini-n">{n}</span>\n'
        '          </div>\n'
    )


def load(name):
    with open(os.path.join(BASE, name), encoding='utf-8') as f:
        return json.load(f)


full = []
for key, cssvar, label, goalstag, meta_q, meta_f in UNITS:
    block = []
    block.append('  <div class="unit-section">\n')
    block.append('    <div class="unit-section-head">\n')
    block.append(f'      <span class="unit-swatch" style="background:var(--{cssvar})"></span>\n')
    block.append(f'      <h2>{label}</h2>\n')
    block.append(f'      <span class="goals-tag">{goalstag}</span>\n')
    block.append('    </div>\n')
    block.append('    <div class="months-cols">\n')

    for mes_key, mes_label, badge in [
        ("2026-07", "Julho", ('closed', 'Mês fechado')),
        ("2026-08", "Agosto", ('open', 'Em andamento — dia 13 de 30')),
    ]:
        pv = load(f"prevendas_{key}_{mes_key}.json")
        ve = load(f"vendas_{key}_{mes_key}.json")
        ee = pv["ever_entered_ativo"]
        leads = ee["Caixa de Entrada"]
        contato = ee["Contato Inicial"]
        emcontato = ee["Em Contato"]
        qualif = ee["Qualificação"]
        reuniao = ee["Reunião Agendada"]
        oport_pv = ee["Oportunidade Gerada"]
        vee = ve.get("ever_entered", {})
        sql = vee.get("Oportunidade (SQL)", 0)
        rc = vee.get("Reunião Comercial", 0)
        ec2 = vee.get("Em Contato", 0)
        pc = vee.get("Proposta Comercial", 0)
        fu = vee.get("Follow-Up", 0)
        nc = vee.get("Negociação/Contrato", 0)
        fechado = ve.get("negocio_fechado", 0)
        perdido = ve.get("negocio_perdido", 0)
        andamento = ve.get("em_andamento_sem_decisao", 0)

        rate1 = (reuniao / leads * 100) if leads else 0.0
        rate2 = (fechado / reuniao * 100) if reuniao else None

        cls, badgetxt = badge
        block.append('      <div class="month-panel">\n')
        block.append('        <div class="month-panel-head">\n')
        block.append(f'          <span class="m-name">{mes_label}</span>\n')
        block.append(f'          <span class="month-badge {cls}">{badgetxt}</span>\n')
        block.append('        </div>\n')
        block.append('        <div class="funnel3">\n')
        block.append('          <div class="checkpoint">\n')
        block.append('            <span class="cp-label">Leads (Caixa de Entrada)</span>\n')
        block.append(f'            <span class="cp-value">{leads}</span>\n')
        block.append('          </div>\n\n')

        c1class = rate_class(rate1, meta_q)
        block.append('          <details class="connector">\n')
        block.append('            <summary>\n')
        block.append('              <span class="conn-line"></span>\n')
        block.append(f'              <span class="conn-rate {c1class}">{pct_br(rate1)}</span>\n')
        if meta_q is not None:
            block.append(f'              <span class="conn-goal">meta {meta_q}%</span>\n')
        else:
            block.append('              \n')
        block.append('              <span class="conn-hint">ver etapas <span class="chevron">▾</span></span>\n')
        block.append('            </summary>\n')
        block.append('            <div class="expand-body">\n')
        block.append('              <div class="board-label">Funil de pré-vendas</div>\n')
        block.append(mini_row("Caixa de Entrada", leads, leads, cssvar))
        block.append(mini_row("Contato Inicial", contato, leads, cssvar))
        block.append(mini_row("Em Contato", emcontato, leads, cssvar))
        block.append(mini_row("Qualificação", qualif, leads, cssvar))
        block.append('            </div>\n')
        block.append('          </details>\n\n')

        block.append('          <div class="checkpoint">\n')
        block.append('            <span class="cp-label">Reuniões Agendadas</span>\n')
        block.append(f'            <span class="cp-value">{reuniao}</span>\n')
        block.append('          </div>\n\n')

        c2class = rate_class(rate2, meta_f)
        rate2txt = pct_br(rate2) if rate2 is not None else "—"
        block.append('          <details class="connector">\n')
        block.append('            <summary>\n')
        block.append('              <span class="conn-line"></span>\n')
        block.append(f'              <span class="conn-rate {c2class}">{rate2txt}</span>\n')
        if meta_f is not None and rate2 is not None:
            block.append(f'              <span class="conn-goal">meta {meta_f}%</span>\n')
        else:
            block.append('              \n')
        block.append('              <span class="conn-hint">ver etapas <span class="chevron">▾</span></span>\n')
        block.append('            </summary>\n')
        block.append('            <div class="expand-body">\n')
        block.append('              <div class="board-label">Funil de pré-vendas</div>\n')
        block.append(mini_row("Oportunidade Gerada", oport_pv, oport_pv, cssvar))
        block.append('              <div class="bridge-marker">⚡ handoff pré-vendas → vendas (boards separados, ver aviso no topo)</div>\n')
        block.append('              <div class="board-label">Funil de vendas</div>\n')
        block.append(mini_row("Oportunidade (SQL)", sql, sql, cssvar))
        block.append(mini_row("Reunião Comercial", rc, sql, cssvar))
        block.append(mini_row("Em Contato", ec2, sql, cssvar))
        block.append(mini_row("Proposta Comercial", pc, sql, cssvar))
        block.append(mini_row("Follow-Up", fu, sql, cssvar))
        block.append(mini_row("Negociação/Contrato", nc, sql, cssvar))
        block.append('            </div>\n')
        block.append('          </details>\n\n')

        block.append('          <div class="checkpoint">\n')
        block.append('            <span class="cp-label">Negócios Fechados</span>\n')
        block.append(f'            <span class="cp-value">{fechado}</span>\n')
        block.append('          </div>\n')
        block.append('        </div>\n')

        if fechado == 0:
            block.append(
                f'        <div class="pending-inline">{fechado} fechados · {perdido} perdidos — '
                f'{andamento} negócios em andamento, aguardando decisão.</div>\n'
            )
            block.append('        \n')
        elif reuniao == 0:
            block.append('        \n')
            block.append(
                '        <div class="pending-inline">⚠ negócio fechado neste mês veio de fora deste '
                'recorte de reuniões agendadas — os dois boards não têm a mesma população, ver aviso no '
                'topo.</div>\n'
            )
        else:
            block.append('        \n')
            block.append('        \n')
        block.append('      </div>\n')

    block.append('    </div>\n')
    block.append('  </div>\n')
    full.append(''.join(block))

result = ''.join(full)
out_path = os.path.join(BASE, 'generated_unit_sections.html')
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(result)
print('done, chars:', len(result), '->', out_path)
