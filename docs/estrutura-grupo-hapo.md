# Estrutura do Grupo Hapo

O Grupo Hapo opera três frentes/marcas principais, cada uma com seu próprio
posicionamento e funil:

- **Goalfy** — CRM/gestão comercial com IA para pequenas e médias empresas.
- **Hapo Educação** — treinamentos e imersões (ex.: gestão comercial, vendas + IA).
- **Hapo Assessoria** — assessoria de estruturação de processo comercial.

O eixo de comunicação divide as frentes em dois blocos (ver
[`briefing-comunicacao-grupo.md`](./briefing-comunicacao-grupo.md) para o detalhe):

- **Goalfy / Assessoria / Educação** — produto/serviço de cada marca.
- **Aquisição / Nutrição / Reativação** — estágio do funil que a comunicação atende.

## Como o trabalho era organizado localmente

No computador do responsável anterior, o projeto vivia numa pasta única
("Hapo Masterplan 2026"), com uma subpasta por marca/frente:

```
Hapo Masterplan 2026/
├── Goalfy/                        # Contexto, identidade visual, criativos, campanhas
├── Hapo Educacao/                 # Apoio comercial, criativos, campanhas
├── Criativos Hapo Assessoria/     # Peças prontas da Assessoria
├── Diretrizes Criativos (Grupo)/  # Copywriting, roteiros, padrões válidos pras 3 marcas
├── Comercial/                     # Scripts + análises de funil/vendas (Goalfy CRM)
├── Google Ads API/
├── Reports e Dashboards Ads/
├── Podcast Visao de Dono/
├── Planejamento Mensal/
├── Estrategia de Iscas/
├── Skills/                        # Skills do Claude Code usadas no dia a dia
└── tools/                         # Pipeline de edição de vídeo local (ffmpeg + whisper.cpp)
```

Este repositório de handoff **não é uma cópia 1:1** dessa pasta — é um recorte
com o que foi selecionado como relevante para a próxima pessoa. Ver
[`README.md`](../README.md) na raiz para o índice completo do que entrou (e
onde encontrar o que ficou de fora: repositórios próprios no GitHub e a pasta
de mídia no Google Drive).

## Outros lugares onde havia trabalho do Grupo Hapo

- **GitHub** (conta `jiancarlo-ship-it`): repositórios de código dos
  dashboards, automações e pipeline de criativos — ver README raiz.
- **Google Drive**: existe uma estrutura própria ("GRUPO HAPO") mantida por uma
  equipe externa de produção de vídeo/foto (conta `myzzaelarquivos@gmail.com`),
  com material bruto de câmera e reels — **diferente** da pasta de handoff
  criada especificamente para esta passagem (`Hapo - Handoff Jian/Criativos e
  Videos`, ver README raiz).
- **Skills do Claude Code** ficavam registradas globalmente
  (`~/.claude/skills/`), não dentro da pasta do projeto — por isso algumas
  (como `meta-ads-hapo`) tiveram que ser copiadas manualmente para este repo.
