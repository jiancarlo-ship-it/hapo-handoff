"""
Baixa relatorios de funil direto da API do Goalfy (links com apiKey embutido em
config/goalfy_link*.md) e salva em "Exports (auto)/<prefixo>_AAAA-MM-DD.xlsx".

Uso:
    python puxar_relatorio.py                       # pre-vendas (default)
    python puxar_relatorio.py --relatorio vendas     # funil de vendas (pos pre-venda)
    python puxar_relatorio.py --relatorio todos      # baixa os dois
    python puxar_relatorio.py --data 2026-08-11      # nome do arquivo customizado

O link nunca deve ser passado por argumento nem impresso no terminal (evita
vazar o apiKey em logs/history). Ele fica só nos arquivos de config.
"""
import argparse
import re
import sys
from datetime import datetime
from pathlib import Path

import requests

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent
DESTINO = RAIZ / 'Exports (auto)'

# nome do relatorio -> (arquivo de config, prefixo do arquivo salvo)
RELATORIOS = {
    'pre-vendas': (RAIZ / 'config' / 'goalfy_link.md', 'funil'),
    'vendas': (RAIZ / 'config' / 'goalfy_link_vendas.md', 'funil_vendas'),
}


def ler_link(config_path):
    texto = config_path.read_text(encoding='utf-8')
    m = re.search(r'https://api\.goalfy\.com\.br/\S+', texto)
    if not m:
        raise RuntimeError(f'Não encontrei o link dentro de {config_path}')
    return m.group(0)


def baixar(nome, data):
    config_path, prefixo = RELATORIOS[nome]
    link = ler_link(config_path)

    print(f'Baixando relatório de {nome}...')
    resp = requests.get(link, timeout=60)
    resp.raise_for_status()

    if not resp.content.startswith(b'PK'):
        print(f'AVISO ({nome}): o conteúdo baixado não parece ser um .xlsx válido (não começa com assinatura ZIP/PK).')
        print(f'Pode ser que o apiKey tenha expirado — verifique {config_path}.')
        sys.exit(1)

    DESTINO.mkdir(exist_ok=True)
    destino_arquivo = DESTINO / f'{prefixo}_{data}.xlsx'
    destino_arquivo.write_bytes(resp.content)
    print(f'OK - salvo em {destino_arquivo} ({len(resp.content)/1024:.0f} KB)')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', help='AAAA-MM-DD para nomear o arquivo (default: hoje)')
    parser.add_argument('--relatorio', choices=['pre-vendas', 'vendas', 'todos'], default='pre-vendas')
    args = parser.parse_args()

    data = args.data or datetime.now().strftime('%Y-%m-%d')
    nomes = list(RELATORIOS) if args.relatorio == 'todos' else [args.relatorio]

    for nome in nomes:
        baixar(nome, data)


if __name__ == '__main__':
    main()
