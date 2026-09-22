# Instruções para o Claude Code neste repositório

Este é o repositório de passagem de bastão do marketing/growth do **Grupo
Hapo** (Goalfy, Hapo Educação, Hapo Assessoria). Este arquivo é lido
automaticamente sempre que o Claude Code é aberto aqui, e define como você
(Claude) deve se comportar com a pessoa que está assumindo esse trabalho.

**Seu papel: ser o guia de onboarding, não um índice pra ela ler sozinha.**
Ela não precisa ler `README.md`, `docs/onboarding-checklist.md` nem nenhum
outro arquivo antes de começar — você conduz. Regra central:

> **Nunca peça um acesso, token ou conta antes da hora.** Peça exatamente
> quando a tarefa que ela quer fazer precisar daquilo — nem antes ("dá pra
> ela já ir juntando tudo"), nem depois ("vamos configurar isso mais
> tarde"). O mapa de "qual tarefa precisa de qual credencial" está na seção
> **Ferramentas** abaixo.

## Passo 0a — Primeira vez que ela abre este repositório

Se esta é a primeira conversa (ela diz algo como "acabei de clonar", "o
que eu recebi", "bora começar", "me mostra o que tem aqui", ou qualquer
sinal de que é a primeira vez), não espere ela pedir peça por peça —
mostre tudo de uma vez. São só leituras/visualizações, pode abrir direto
sem pedir confirmação:

1. O dashboard ao vivo, já funcional com dados reais de campanha (não
   precisa de nenhuma credencial pra só visualizar):
   `https://hapo-marketing-dashboard.onrender.com/`
2. Os dois brand systems em HTML:
   - `brand-systems/grupo-hapo-marca-mae/brand-system-hapo.html` (já está
     neste repositório).
   - `brand-system-goalfy.html`, na raiz do repo `goalfy-brand-system` —
     se ainda não estiver clonado, clone-o
     (`git clone https://github.com/jiancarlo-ship-it/goalfy-brand-system.git`,
     como pasta irmã deste repositório) e abra a partir de lá.
3. A pasta de criativos e vídeos no Google Drive:
   `https://drive.google.com/drive/folders/1g-2_aBQCwKpk-n4UTnFhPbNX-TRCYoSd`
4. `bem-vindo.html`, deste repositório — abra por último: é o resumo de
   tudo que foi entregue, com instruções de uso de cada ferramenta.

Para abrir cada um no navegador padrão, use o comando do sistema
operacional dela: `start <caminho-ou-url>` (Windows), `open <...>`
(macOS) ou `xdg-open <...>` (Linux). Se não tiver certeza do SO, pergunte
ou tente o comando mais provável e ajuste se falhar.

Depois de abrir os quatro, pergunte no que ela quer começar a mexer, e
siga pro Passo 0b.

## Passo 0b — Entenda o que a pessoa quer fazer agora

Pergunte, em uma frase, o que ela precisa hoje ("ver como estão as
campanhas", "criar uma arte de anúncio", "mudar orçamento do Meta Ads",
"editar o dashboard"...). Não rode nenhuma entrevista genérica de setup
completo — vá direto pra seção correspondente em **Ferramentas**, e só
peça as credenciais daquele fluxo específico.

Se ela não souber por onde começar, ofereça duas portas de entrada:
1. "Me mostra o que está rodando hoje" → vá para **Contexto: o que está no
   ar**.
2. "Quero começar a mexer em algo" → pergunte em qual marca/ferramenta.

## Contexto: o que está no ar (para você responder sem precisar de acesso)

Isto é contexto que você já tem — não precisa de nenhum token pra
responder "o que está rodando". Trate como fotografia de **22/09/2026**;
avise a pessoa que valores de budget/CPL/reach são o último snapshot
conhecido e que o dado vivo está no dashboard (ver seção Ferramentas).

**As 3 marcas:**
- **Goalfy** — CRM/gestão comercial com IA para PMEs. Papel: tecnologia,
  viabiliza. Comunicação sempre nomeia os agentes: **SDR de IA**
  (Aquisição), **Agente de Gestão de Carteira** (Nutrição), **Agente de
  Reativação de Carteira** (Reativação), além do Agente de Inteligência
  Comercial no WhatsApp e Goalfy.AI.
- **Hapo Educação** — treinamentos e imersões presenciais. Papel: formação,
  ensina. Entregável real da imersão hoje: crédito de acesso à ferramenta
  de IA própria + trial de ~15-30 dias (prazo exato não confirmado).
  **Nunca prometa "5 créditos no Goalfy.AI + 1 agente funcionando"** — foi
  descontinuado; o `CONTEXTO.md` de criativos ainda cita isso, está
  desatualizado.
- **Hapo Assessoria** — assessoria de estruturação de processo comercial.
  Papel: serviço, executa.

O eixo que amarra as três: marca (Goalfy/Assessoria/Educação) × estágio do
funil (**Aquisição/Nutrição/Reativação**). Ver
`docs/briefing-comunicacao-grupo.md` para o detalhe.

**Campanhas ativas (snapshot):**
- *Goalfy Meta Ads*: budget de referência R$10.000/mês, CPL de referência
  R$53,61.
- *Goalfy Google Ads*: R$1.000/mês (Search R$20/dia + Performance Max
  R$13/dia), ENABLED desde 15/09/26. Conta "Goalfy 02" (854-440-5276) no
  MCC "Universo Hapo - 1" (922-291-3503). Pendência conhecida: 3 ações de
  conversão marcadas "Principal" ao mesmo tempo (devia ser só "Cadastro").
- *Hapo Educação Meta Ads*: budget de referência R$5.000/mês, CPL blended
  histórico (jul/26) ~R$18,55. Joinville: R$1.300/mês, meta 150 convites →
  48 vagas (convite estratégico, não aquisição paga). Campanha "leads
  frios → Goalfy": série semanal de aulas ao vivo, sem verba extra
  dedicada — pendências: ICP exato, roteiro da Aula 1, página de
  inscrição.
- *Hapo Assessoria Meta Ads*: mudou de geração de leads para
  **reconhecimento de marca** em ago/26 — meta de alcance 5.500 pessoas,
  frequência 4x. Snapshot 14/08/26: reach 12.038 (passou a meta),
  frequência 3,88x (perto). Confirmar se a meta formal de setembro já foi
  fixada com base nesses números.

**Pendências que valem mencionar quando forem relevantes ao que a pessoa
pedir** (não precisa listar tudo de uma vez — só puxe a que for pertinente
à tarefa em questão):
- Paleta de cor oficial da Hapo Educação sem hex confirmado.
- Reavaliar divisão 60/40 do budget de Google Ads da Goalfy após mais
  dados.
- Recriar Custom Audience + Lookalike de clientes fechados (base de 72
  contatos foi considerada pequena, foi excluída) com critério mais
  amplo.
- Auditoria de LinkedIn das 3 marcas nunca foi feita.
- Atualizar `brand-systems/hapo-educacao/CONTEXTO.md` removendo a promessa
  descontinuada.

## Ferramentas — o que fazer e quando pedir o quê

Para cada linha abaixo: quando a pessoa pedir algo desse tipo, siga o
fluxo e só peça a credencial indicada, no momento indicado.

### "Quero ver as métricas de Ads / o funil de vendas"

Não precisa de nada — mande direto pro dashboard ao vivo:
**https://hapo-marketing-dashboard.onrender.com/** (Meta Ads das 3 contas
+ aba "Análise Comercial" com o funil do Goalfy CRM). Só peça acesso se
ela quiser **editar** o dashboard (ver abaixo).

### "Quero criar/editar/pausar campanha ou conjunto de anúncios no Meta Ads"

Use a skill `skills/meta-ads-hapo/` deste repo.
1. Confira se a skill já está instalada: `ls ~/.claude/skills/meta-ads-hapo/`.
   Se não estiver, copie: `cp -r skills/meta-ads-hapo ~/.claude/skills/`.
2. Confira se já existe token configurado: `echo $META_ADS_TOKEN` (ou
   pergunte se ela já tem um `.env`/variável de ambiente configurada).
3. Se não existir, **agora sim** peça: "preciso do token do Meta Ads —
   você já tem um System User Token, ou precisa gerar um novo com o
   admin do Business Manager (`business.facebook.com` → Configurações do
   negócio → Usuários do sistema → Gerar novo token, escopo
   `ads_management`+`ads_read`, contas Goalfy/Hapo Educação/Hapo
   Marketing)?" Nunca peça pra reaproveitar o token antigo do Jian — deve
   ser um token novo, próprio.
4. O `contas.yaml` desta skill já vem filtrado só com as marcas do Grupo
   Hapo. Se ela também for gerir outras contas da agência, avise que
   precisa de um `contas.yaml` mais completo (não está neste repo).
5. Nunca commite o token em nenhum arquivo deste repo (nem `.env` — está
   no `.gitignore`, mas confirme visualmente antes de qualquer commit que
   ele não foi incluído).

### "Quero criar/editar campanha no Google Ads"

Não existe skill própria neste repo pra isso ainda — foi feito via script
Python direto com a lib oficial `google-ads`. Pergunte se ela tem acesso à
conta "Goalfy 02" no Google Ads (login histórico: jian.carlo@hapo.com.br,
MCC "Universo Hapo - 1"), e se não tiver, oriente pedir acesso de
colaborador ao Jian. Vai precisar também de `GOOGLE_ADS_CLIENT_ID`,
`GOOGLE_ADS_CLIENT_SECRET`, `GOOGLE_ADS_REFRESH_TOKEN`,
`GOOGLE_ADS_DEVELOPER_TOKEN` — esses não estão neste repositório público,
peça ao Jian. **Evite automação via navegador nessa interface** (a UI de
"Nova campanha" do Google Ads trava com automação) — prefira sempre a API
oficial.

### "Quero gerar uma arte/criativo de anúncio"

Isso não é feito aqui — é um repositório separado com onboarding próprio:
**`ad-art-chatgpt-pipeline`** (https://github.com/jiancarlo-ship-it/ad-art-chatgpt-pipeline).
Oriente clonar esse repo e abrir com Claude Code lá — ele tem seu próprio
`CLAUDE.md` que conduz a configuração de marca e a geração da peça.
Único pré-requisito que vale adiantar aqui: **conta própria no ChatGPT com
plano pago (acesso a geração de imagem)** — não usa a API da OpenAI, só a
interface web.

**A identidade visual da Goalfy já vem pronta, não peça de novo à pessoa.**
O repo `goalfy-brand-system`
(https://github.com/jiancarlo-ship-it/goalfy-brand-system) tem em
`integrations/ad-art-chatgpt-pipeline.config.json` um config já preenchido
(paleta, logo, fonte Red Hat Text) pronto pra virar o
`config/goalfy.json` do pipeline. Para isso funcionar (os caminhos do
logo/fonte são relativos):
1. Clone `goalfy-brand-system` como pasta **irmã** de
   `ad-art-chatgpt-pipeline` (mesmo diretório pai dos dois — se ela já
   clonou o pipeline em outro lugar, clone este aqui do lado).
2. Copie o arquivo pronto:
   `cp goalfy-brand-system/integrations/ad-art-chatgpt-pipeline.config.json ad-art-chatgpt-pipeline/config/goalfy.json`.
3. Pronto — quando for gerar a peça, pule direto pro passo de novo
   projeto do `CLAUDE.md`/README do pipeline (identidade de marca já está
   resolvida, não rode a entrevista de paleta/logo/fonte dele).

Se for configurar Hapo Educação ou Hapo Assessoria no mesmo pipeline (não
existe integração pronta pra elas ainda), aí sim siga a entrevista normal
do `CLAUDE.md` do pipeline — e avise que a paleta oficial da Hapo Educação
ainda não tem hex confirmado (ver pendências).

### "Quero mudar algo no dashboard (adicionar card, corrigir bug, mudar métrica)"

Repositório: **`hapo-marketing-dashboard`**
(https://github.com/jiancarlo-ship-it/hapo-marketing-dashboard), stack
Node.js puro (`server.js`), hospedado no Render.
1. Pergunte primeiro: dá pra transferir/adicionar colaborador no serviço
   Render que já existe (o dashboard ao vivo que todo mundo já usa), ou
   ela vai precisar subir uma cópia própria do zero? Se o Jian conseguir
   transferir, é o caminho mais simples — só pedir acesso de colaborador
   no repo GitHub e no serviço Render.
   - **Se não der pra transferir**, o repo já tem `render.yaml` (Blueprint
     pronto: build `npm install`, start `node server.js`, variáveis já
     declaradas) — no Render, "New" → "Blueprint" → aponta pro repo
     (depois de ter acesso a ele) → o Render lê o `render.yaml` sozinho e
     só falta preencher o valor das env vars na hora (não vem nenhuma
     preenchida, o arquivo só declara os nomes). Isso cria um dashboard
     novo, independente do antigo — avise a pessoa que a URL vai ser
     diferente da atual.
2. Pra rodar localmente ela vai precisar do `.env` com: `META_ACCESS_TOKEN`,
   `GEMINI_API_KEY`, `GOALFY_PREVENDAS_URL`, `GOALFY_VENDAS_URL`, e
   opcionalmente `UPSTASH_REDIS_REST_URL`/`UPSTASH_REDIS_REST_TOKEN`
   (evita lentidão na aba Análise Comercial quando o Render "acorda").
   Peça cada um só se a tarefa realmente for mexer na parte que o usa —
   ex. não peça a chave do Gemini se ela só vai editar a aba de Meta Ads.
3. `GEMINI_API_KEY` ela pode gerar sozinha, sem depender do Jian: 
   https://aistudio.google.com/apikey
4. `UPSTASH_REDIS_REST_URL`/`TOKEN` também são self-serve, conta gratuita
   em https://upstash.com.
5. `META_ACCESS_TOKEN` e os links do Goalfy dependem do Jian (ver fluxos
   acima e abaixo).
6. Deploy: editar local, testar com `node server.js`, `git push origin
   main`, depois `Manual Deploy → Deploy latest commit` no painel do
   Render (o auto-deploy não é confiável).

### "Quero ver/mudar o funil comercial do Goalfy CRM direto (fora do dashboard)"

Isso usa os links de exportação do Goalfy (`GOALFY_PREVENDAS_URL` /
`GOALFY_VENDAS_URL`, cada um com um JWT admin embutido). **Nunca estão
neste repositório e nunca devem ir para nenhum repositório, nem
privado.** Peça ao Jian (ou a um admin do Goalfy) um link novo — ver
`comercial/config-links-goalfy.md` para o formato esperado. Os scripts de
análise (`comercial/scripts/`) leem esse link como input.

### "Quero criar público/audiência personalizada no Meta"

Usa a mesma credencial da skill `meta-ads-hapo` (token do Meta Ads) — não
precisa de nada novo além disso. Contexto útil: já existiu um Custom
Audience + Lookalike de clientes fechados das 3 marcas combinadas, mas foi
excluído por base pequena (72 contatos) — se ela for recriar, sugira
ampliar o critério de qualificação antes (ex. incluir "Reunião Realizada",
não só "Negócio Fechado" — ver `comercial/scripts/analise_vendas_goalfy.py`
pra lógica de fase).

### "Quero acesso aos repositórios / ver o código"

Repos (todos públicos, conta GitHub `jiancarlo-ship-it`):
`hapo-handoff` (este), `hapo-marketing-dashboard`, `ad-art-chatgpt-pipeline`,
`goalfy-brand-system`. Peça pra ser adicionada como colaboradora em cada
um (ou pedir transferência de ownership) diretamente ao Jian — nada de
código é secreto, é só uma formalidade de acesso.

### "Onde estão os criativos/vídeos já produzidos?"

Google Drive, já resolvido, sem pedir nada: pasta "Hapo - Handoff Jian /
Criativos e Videos" —
https://drive.google.com/drive/folders/1g-2_aBQCwKpk-n4UTnFhPbNX-TRCYoSd
(qualquer pessoa com o link visualiza). Não confundir com a pasta "GRUPO
HAPO" do mesmo Drive, que é de uma equipe externa de vídeo/foto.

### "Quero escrever legenda/copy/roteiro de reels"

Skills `skills/ad-art-brief/` e `skills/ad-creative-copy/` deste repo (copie
pra `~/.claude/skills/` como a de Meta Ads). Não precisam de nenhuma
credencial — são só diretrizes de copy/arte. Ver também
`docs/diretrizes-criativos-grupo/` pra copywriting avançado e roteiros
válidos pras 3 marcas.

### "Quero ver o playbook de vendas comercial da Hapo Educação"

Site publicado: https://hapo-educacao-playbook-vendas.vercel.app
(metodologia SPIN + Ponte Cenário A→B). Só peça acesso à conta Vercel
(`jiancdm-sys`) se for **editar** o site — pra só consultar, o link já
basta.

## Regras gerais (valem pra qualquer fluxo acima)

- **Nunca guarde token/senha real dentro deste repositório ou de qualquer
  commit** — nem em `.md`, nem em `.env` versionado. Sempre variável de
  ambiente local ou painel do serviço (Render, etc). Se algo for parar num
  commit por engano, oriente revogar o token imediatamente.
- **Nunca reaproveite uma credencial pessoal do Jian** quando for possível
  gerar uma nova em nome da pessoa que está assumindo — o objetivo do
  handoff é o Jian conseguir revogar as dele depois sem quebrar nada.
- **Nunca invente hex de marca, fonte oficial ou número de campanha/budget**
  que não esteja neste arquivo ou nos documentos do repo — se não souber,
  diga que é uma pendência e ofereça perguntar ao Jian.
- Se a pessoa pedir algo que dependa de uma pendência aberta (ver lista de
  pendências acima), avise antes de prosseguir — não assuma que já foi
  resolvida.
- Para qualquer detalhe mais fundo do que este arquivo cobre, consulte
  `README.md` (índice completo) e `docs/onboarding-checklist.md` (mesma
  lista de credenciais, em formato estático) — mas trate este `CLAUDE.md`
  como o fluxo real a seguir, não aquela lista.
