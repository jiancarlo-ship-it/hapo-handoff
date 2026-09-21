# Comercial — Funil de Vendas (Goalfy)

Pasta de trabalho para análise do funil comercial (CRM/board do Goalfy) e,
na sequência, cruzamento com dados de campanhas de marketing.

## Estrutura

- `config/goalfy_link.md` — link da API do Goalfy que baixa o relatório de
  funil (contém apiKey sensível, ver aviso no próprio arquivo). **O fluxo é
  sempre puxar por esse link, não salvar relatório manualmente.**
- `Exports (auto)/` — arquivos .xlsx baixados automaticamente pelo script
  `puxar_relatorio.py`, nomeados `funil_AAAA-MM-DD.xlsx` (data do download).
  Tratar como cache local, descartável — a fonte da verdade é o link.
- `Analises/` — saídas .json geradas pelo script de análise, uma por
  rodada/mês/unidade.
- `scripts/puxar_relatorio.py` — baixa o export mais recente direto da API
  (lê o link em `config/goalfy_link.md`, salva em `Exports (auto)/`). Uso:

  ```
  python scripts/puxar_relatorio.py
  ```

- `scripts/analise_funil_goalfy.py` — script reutilizável que lê o export e calcula
  todos os números do diagnóstico (funil por volume, tempo por fase, lead time até
  oportunidade, segmentação por fonte e por unidade de negócio, motivos de
  desqualificação, backlog na Caixa de Entrada). Uso:

  ```
  python scripts/analise_funil_goalfy.py "Exports (auto)/funil_AAAA-MM-DD.xlsx" --agora "DD/MM/AAAA HH:MM:SS" --out "Analises/saida.json"
  # com filtro de mes:
  python scripts/analise_funil_goalfy.py "..." --mes 2026-08 --agora "..." --out "Analises/saida_agosto.json"
  # com filtro de unidade de negocio (Goalfy | Hapo Educação | Hapo Assessoria):
  python scripts/analise_funil_goalfy.py "..." --unidade "Goalfy" --agora "..." --out "Analises/saida_goalfy.json"
  ```

  `--agora` é o timestamp de referência pra calcular backlog (leads parados na Caixa
  de Entrada); sem isso, o script usa o maior "Criado em" do próprio arquivo.

### Fluxo de trabalho padrão (a cada rodada de análise)

1. `python scripts/puxar_relatorio.py` — baixa o export mais recente pelo link.
2. Rodar `analise_funil_goalfy.py` sobre esse export (geral e/ou filtrado por
   `--mes` / `--unidade`, conforme o que for pedido).
3. Ler o .json de saída e transformar em diagnóstico de texto (isso é feito na
   conversa, não pelo script — o script só extrai os fatos).

## Ordem oficial do pipeline (confirmada com o Jian)

Caixa de Entrada → Contato Inicial → Em Contato → Qualificação → Reunião Agendada →
No-show → Oportunidade Gerada → **Lead Desqualificado** (saída lateral — pode
acontecer a partir de qualquer fase, não é etapa sequencial final).

## O que já sabemos (consolidado até 11/08/2026)

**Achado estrutural nº1 — segmentar sempre por fonte antes de tirar conclusão.**
56% da base (2.121 leads) é uma importação de lista antiga ("Base Antiga -
Pré-vendas", entrada em massa em abril/2026) que nunca foi trabalhada como funil
ativo — foi parqueada direto em "🤖 Nutrição". Toda análise deve excluir essa
fatia (ou tratá-la separadamente como reativação) antes de calcular conversão.

**Funil ativo (exclui Base Antiga), histórico completo — "ever entered" por fase:**

| Fase | Nº leads | Conversão da fase anterior |
|---|---|---|
| Caixa de Entrada | 2.624 | — |
| Contato Inicial | 1.040 | 39,6% ⚠️ maior gargalo por volume |
| Em Contato | 23 | 2,2% — estágio morto/pulado, considerar remover |
| Qualificação | 226 | 21,7% ⚠️ segundo maior gargalo |
| Reunião Agendada | 113 | 50,0% |
| No-show | 16 | 14,2% das reuniões |
| Oportunidade Gerada | 151 | ~65% de quem passou por Qualificação/Reunião |
| Lead Desqualificado (lateral) | 302 | 11,5% do funil ativo total |

**Lead time até Oportunidade Gerada** (Criado em → 1ª entrada em Oportunidade
Gerada, n=147): mediana **1,21 dia**, média 5,1 dias. Quando o lead avança, avança
rápido — o problema do funil é cobertura/volume, não velocidade de processo.

**Motivo de desqualificação nº1 (histórico, normalizado): "Fora do ICP" (85
ocorrências)** — é insumo direto pra etapa 2 (cruzar com campanhas de mídia:
provavelmente dá para apontar quais campanhas/públicos trazem lead fora de perfil).

**Recorte de Agosto/2026 (mês em andamento, 257 leads, 01–11/08):**
100% inbound (86% Meta_Ads/Instagram). Topo do funil convertendo melhor que o
histórico (Caixa→Contato 63,4% vs 39,6%), mas:
- **Backlog real de leads sem 1º contato**: 69 de 82 leads ainda em Caixa de
  Entrada estão parados há mais de 48h (mediana 7,5 dias) — ação imediata, não é
  distorção de censura por mês em andamento.
- **No-show subiu para 31%** (9 de 29 reuniões) vs 14% histórico — amostra pequena,
  mas monitorar.
- Motivo de desqualificação do mês é dominado por "Duplicado" (9 de 16), diferente
  do padrão histórico ("Fora do ICP") — sugere problema técnico de cadastro
  duplicado no formulário/campanha, não problema de targeting.

**Problemas de tagueamento no CRM que limitam qualquer cruzamento futuro:**
- `Campanha` vazia em 82% das linhas (inclusive em 89 das 148 oportunidades atuais)
  → atribuição por campanha só é confiável para ~59 oportunidades.
- `Plataforma` vazia em 87% das linhas.
- `Unidade de Negócio` vazia em 79%, e com chaves duplicadas (`Goalfy`/`Goslfy`,
  `Hapo Educação`/`Educação`/`Educação SP`).

## Segmentação por unidade de negócio (Goalfy / Hapo Educação / Hapo Assessoria)

O campo "Unidade de Negócio" do CRM só está preenchido em ~25% da base (mesmo
somando com a etiqueta equivalente). Para segmentar, o script aplica uma
heurística por prioridade: (1) campo explícito → (2) etiqueta → (3) palavra-chave
em Campanha/Fonte do Lead/Título do Evento. Mesmo assim, no funil ativo (exclui
Base Antiga), **62% dos leads (1.838 de 2.944) ficam "Não classificado"** — não é
bug do script, é lacuna de tagueamento no CRM. Nenhum outro campo do export
(responsável, pré-vendas, criador) serve como proxy confiável — está tudo
concentrado num único operador que atende as três marcas.

**Cobertura por unidade (funil ativo):** Goalfy 597, Hapo Educação 481, Hapo
Assessoria 28. Assessoria tem amostra pequena — ler os números dela como
indicativo, não estatisticamente robusto.

| Métrica | Goalfy | Hapo Educação | Hapo Assessoria |
|---|---|---|---|
| Caixa → Contato Inicial | 69,5% | 69,8% | 82,1% |
| Contato Inicial → Qualificação | 23,9% | 21,7% | 17,4% |
| Qualificação → Reunião Agendada | 83,7% | 91,4% | — (amostra mínima) |
| Taxa de No-show | 19,5% | 12,5% | 0% (n pequeno) |
| Lead time até Oportunidade (mediana) | 1,16 dia | 0,92 dia | 2,44 dias |
| Backlog Caixa de Entrada (mediana, leads parados) | 94,5h (~4 dias) | **566h (~24 dias)** | 313h (~13 dias) |
| Motivo de desqualificação nº1 | Duplicado / Fora do ICP (empate) | Duplicado (54%) | Fora do ICP |

Leitura: as três unidades têm o mesmo padrão de gargalo do diagnóstico geral
(Contato Inicial → Qualificação é o ponto fraco nas três, ~17-24%), mas o
**backlog de leads sem 1º contato é desproporcionalmente mais grave em Hapo
Educação** (mediana de 24 dias parado vs 4 dias no Goalfy) — isso não aparecia
tão nítido no agregado porque o volume de Educação é menor que o de Goalfy.

## Próximo passo pendente

Cruzar os leads/oportunidades do funil (por fonte/campanha, quando disponível)
com o gasto e CPL das campanhas de marketing (dashboard de ads — ver
`Reports e Dashboards Ads/` no masterplan e a memória `dashboard_ads_repo`), pra
entender custo por oportunidade gerada e se o "Fora do ICP" está concentrado em
campanhas específicas. Bloqueado parcialmente pela lacuna de tagueamento de
Campanha/Plataforma acima.
