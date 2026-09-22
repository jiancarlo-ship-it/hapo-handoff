# Hapo Handoff

Repositório de passagem de bastão do trabalho de marketing/growth do Grupo
Hapo (Goalfy, Hapo Educação, Hapo Assessoria). Não é uma cópia completa de
tudo que existia — é um recorte selecionado do que faz sentido continuar.

**Não leia este README primeiro.** Clone este repositório e abra a pasta
com o [Claude Code](https://claude.com/claude-code) — o arquivo
[`CLAUDE.md`](./CLAUDE.md) carrega sozinho e conduz o onboarding: mostra o
que foi entregue, abre o dashboard/brand systems/criativos, e só pede
token/acesso na hora exata em que uma tarefa específica precisar. Ver
também [`bem-vindo.html`](./bem-vindo.html) (aberto automaticamente nesse
fluxo) e [`docs/onboarding-checklist.md`](./docs/onboarding-checklist.md)
— mesma lista de credenciais em formato estático, caso prefira ler sem o
Claude Code.

## Onde está cada coisa

### Neste repositório

| Pasta | O que é |
|---|---|
| [`docs/onboarding-checklist.md`](./docs/onboarding-checklist.md) | O que pedir ao Jian no dia do handoff (acessos, tokens, contas) |
| [`docs/estrutura-grupo-hapo.md`](./docs/estrutura-grupo-hapo.md) | Como as 3 marcas se organizam e onde ficava cada tipo de trabalho |
| [`docs/briefing-comunicacao-grupo.md`](./docs/briefing-comunicacao-grupo.md) | Divisão Goalfy/Assessoria/Educação × Aquisição/Nutrição/Reativação, gaps de site pendentes na época |
| [`docs/diretrizes-criativos-grupo/`](./docs/diretrizes-criativos-grupo/) | Copywriting avançado, roteiros de reels/ads, diretrizes de legenda — válido para as 3 marcas |
| [`brand-systems/grupo-hapo-marca-mae/`](./brand-systems/grupo-hapo-marca-mae/) | Brand system da marca mãe (usado também pela Hapo Assessoria): cores, tipografia, logo, ícones |
| [`brand-systems/hapo-educacao/`](./brand-systems/hapo-educacao/) | Identidade visual da Hapo Educação: logo + tipografia (decidida no handoff), paleta própria ainda pendente |
| [`comercial/`](./comercial/) | Scripts Python que geram as análises de funil/vendas a partir do Goalfy CRM. Os dados/análises já gerados (receita, taxa de fechamento) **não estão neste repositório público** — pedir ao Jian se precisar do histórico |
| [`skills/ad-art-brief/`](./skills/ad-art-brief/) | Skill do Claude Code: transforma narrativa aprovada em brief de arte completo (headline + prompt de imagem) |
| [`skills/ad-creative-copy/`](./skills/ad-creative-copy/) | Skill do Claude Code: modelo padrão de legenda de anúncio |
| [`skills/meta-ads-hapo/`](./skills/meta-ads-hapo/) | Skill do Claude Code: gerencia campanhas Meta Ads via SDK oficial — cadastro de contas filtrado só para as marcas do Grupo Hapo |

A **Goalfy tem brand system próprio, em repositório separado**:
[`goalfy-brand-system`](https://github.com/jiancarlo-ship-it/goalfy-brand-system)
(público) — tokens extraídos 1:1 do site ao vivo (goalfy.com.br), componentes
de UI prontos, fonte oficial (Red Hat Text) e logo em `assets/`.

Todas as skills usam variável de ambiente para credenciais (nunca commitadas
aqui). Ver `comercial/config-links-goalfy.md` para como reobter o link do
Goalfy, e o `SKILL.md` de `meta-ads-hapo` para como configurar o token do Meta
Ads.

### Fora deste repositório

**Código (GitHub, conta `jiancarlo-ship-it`):**

- [`hapo-marketing-dashboard`](https://github.com/jiancarlo-ship-it/hapo-marketing-dashboard) (público) —
  dashboard de Ads ao vivo (Node.js, hospedado no Render) + aba Análise
  Comercial com o funil Goalfy CRM ao vivo. É o app real em uso.
- [`ad-art-chatgpt-pipeline`](https://github.com/jiancarlo-ship-it/ad-art-chatgpt-pipeline) (público) —
  pipeline de geração de arte de anúncio: cena via ChatGPT web + acabamento
  determinístico (cor de marca exata + logo real) via Python/Pillow. Tem
  `CLAUDE.md` próprio com onboarding guiado.

**Artes, vídeos e motions (Google Drive):**

[`Hapo - Handoff Jian / Criativos e Videos`](https://drive.google.com/drive/folders/1g-2_aBQCwKpk-n4UTnFhPbNX-TRCYoSd)
— pasta compartilhada como "qualquer pessoa com o link pode visualizar",
organizada por marca (Goalfy, Hapo Assessoria, Hapo Educação, Diretrizes do
Grupo). Contém todo o histórico de criativos (inclusive testes e variações
descartadas, sem filtro) e os vídeos/motions produzidos. **Não confundir**
com a pasta "GRUPO HAPO" que já existe no mesmo Drive — aquela é mantida por
uma equipe externa de produção de vídeo/foto e tem conteúdo diferente
(material bruto de câmera).

## Segurança — leia antes de usar

Dois tipos de segredo foram **deliberadamente excluídos** deste repositório
e precisam ser reobtidos/reconfigurados pela próxima pessoa:

1. **Link de relatório do Goalfy** (JWT admin embutido na URL) — ver
   `comercial/config-links-goalfy.md`.
2. **Token de acesso do Meta Ads** (`META_ADS_TOKEN`) — usado pela skill
   `meta-ads-hapo`, configurado via variável de ambiente / `.env` local, nunca
   commitado.

Se algum desses acabar indo parar num commit por engano, **revogar o token
imediatamente** (no Goalfy: gerar novo link; no Meta: regenerar o token de
acesso no Business Manager) antes de qualquer outra coisa.
