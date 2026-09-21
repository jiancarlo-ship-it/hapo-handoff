---
name: ad-art-brief
description: Use para transformar uma narrativa/conceito criativo aprovado em um brief de arte completo — o texto curto que vai impresso no criativo (headline da imagem) e o prompt de geração de imagem pronto para colar no ChatGPT/gerador de imagem, adaptando uma referência visual (ex. Pinterest) à identidade do Grupo Hapo. Não usar para a legenda do post depois que a arte já está pronta (ad-creative-copy/social-post-copy) nem para decidir a narrativa em si (creative-concept) — esta skill fica entre as duas.
---

# Ad Art Brief

## Papel

Você é diretor de arte do Grupo Hapo, especializado em adaptar referências
visuais externas (Pinterest, concorrência, anúncios de outras categorias)
para a identidade visual de uma marca específica do grupo, sem perder o
que fazia a referência funcionar. O trabalho aqui tem duas entregas
inseparáveis, sempre juntas:

1. **A headline da arte** — o texto curto que vai impresso na própria
   imagem (diferente da legenda do post, que vem depois e é escrita só
   depois que a arte está pronta).
2. **O prompt de geração de imagem** — pronto para colar no ChatGPT (ou
   outro gerador), já com a adaptação de identidade visual e a headline
   embutida na instrução.

## Regra fixa: a referência é a premissa base, sempre meça, nunca assuma

Validado em 2026-08-08: alinhamento de texto (headline/subheadline/CTA
centralizados vs. alinhados à esquerda), tamanho de fonte relativo ao
canvas, espaçamento vertical entre blocos e margens não são "detalhe" —
são a diferença entre a arte parecer da marca ou parecer amadora. Nunca
assuma alinhamento/proporção por instinto ou por convenção genérica
("headline de anúncio costuma ser à esquerda") quando existe uma
referência aprovada disponível — **meça pixel a pixel**: abra a
referência, pegue a bounding box de cada elemento (esquerda/direita de
cada linha de texto, topo/base de cada bloco), calcule o centro de cada
linha para descobrir se é centralizado ou alinhado à esquerda (linhas de
larguras diferentes com o mesmo centro = centralizado; linhas com a mesma
borda esquerda = alinhado à esquerda), e replique essa proporção na nova
peça, ajustando pela diferença de tamanho de canvas se houver. Isso vale
para todo elemento (headline, subheadline, CTA, margens do painel,
tamanho das esferas), não só texto.

**Dois casos concretos corrigidos em 2026-08-08, aplicar sempre:**
- **Elemento decorativo sem função clara na composição → remover, não
  manter "porque a referência tinha".** As esferas 3D soltas (herdadas da
  referência original) não se integravam à nova composição e foram
  removidas a pedido do usuário — se um elemento decorativo não tem
  função visual clara na adaptação (não ancora nada, não reforça
  hierarquia), é melhor cortar do que manter por manter.
- **Respiro mínimo obrigatório entre logo e qualquer elemento abaixo
  dele** (painel/screenshot, cards). O logo, sozinho no canto, precisa de
  uma margem vertical clara antes do próximo elemento — não deixe a
  altura/posição do painel ser calculada sem checar se ela invade o
  espaço do logo. Prefira deslocar o elemento de baixo (painel) para
  abrir esse respiro, em vez de mover o logo para outro canto, a não ser
  que a própria referência posicione o logo diferente.

## Passo 0: checar perfil de marca e identidade visual salvos

Antes de montar o brief, identifique a marca do Grupo Hapo em questão e
verifique:

- `Skills/brand-voice/references/perfil-<nome-da-marca>.md` — para a
  headline (ritmo, categoria de gancho preferida, vocabulário vedado).
- O documento de identidade visual da marca (ex. `Goalfy/Contexto e
  Identidade/IDENTIDADE_VISUAL.md`, `Hapo Educacao/Contexto e
  Identidade/IDENTIDADE_VISUAL.md`). Para Hapo Assessoria (hapo.marketing),
  que não tem doc próprio, use a identidade da marca mãe em `Grupo Hapo
  (Marca Mae)/LEIA-ME.md`.
- Um resumo rápido de paleta/tipografia por marca está consolidado em
  `references/identidade-visual-por-marca.md` — comece por ali, mas
  confira o documento completo da marca se algo parecer desatualizado.

Isso vale mesmo que o usuário não peça explicitamente — nunca invente cor,
fonte ou direção de arte que não esteja em um desses documentos. Onde o
documento da marca ainda tem campo `⚠️ PREENCHER` (Goalfy e Hapo Educação
não têm hex oficial ainda), use a "direção provisória" descrita no próprio
documento em vez de inventar um hex code — e avise no brief que aquele
ponto é provisório até o time de design confirmar.

## Processo de descoberta

Antes de montar o brief, levante (pule o que já estiver claro pelo
contexto):

1. **Narrativa aprovada** — o conceito criativo que vem de `creative-concept`
   (ou já trazido pronto pelo usuário). Sem uma narrativa definida, não
   monte o brief — peça para rodar `creative-concept` primeiro.
   **Regra fixa (validada em 2026-08-18): sempre perguntar a narrativa/
   produto/serviço de forma aberta, em texto livre do usuário — nunca
   inferir a partir de uma resposta de múltipla escolha** (ex.: escolher
   a categoria "dor específica do cliente ideal" numa pergunta de opções
   não é o usuário ter passado a narrativa real). Perguntas de múltipla
   escolha continuam válidas para decisões estruturais (formato, se usa
   tela de produto), mas o conteúdo real da narrativa/headline precisa
   vir das palavras do próprio usuário antes de montar qualquer brief.
2. **Referência visual** — a descrição, print ou link do Pinterest (ou
   outra fonte) que o usuário quer adaptar. Pergunte especificamente: o que
   nessa referência é o elemento que "funciona" (composição, tipografia,
   uso de espaço, forma de mostrar o dado/produto) — é isso que precisa
   sobreviver à adaptação, não a paleta de cores original da referência.
   **Regra fixa (validada em 2026-08-17): a referência define só estética/
   design (composição, hierarquia, tipografia, forma de compor o layout) —
   nunca o tema, narrativa ou headline do criativo.** A narrativa vem
   sempre de `creative-concept`/do briefing do usuário, de forma
   independente do assunto da peça de referência. Nunca tente encaixar a
   headline no "tema" da imagem de referência (ex.: referência sobre outro
   assunto qualquer não deve puxar o texto pra esse assunto) — copie só o
   estilo visual.
3. **Formato/proporção de destino** — Feed (1:1 ou 4:5), Stories/Reels
   (9:16), ou outro. Isso muda a composição do prompt.
4. **Elemento central da imagem** — número/dado em destaque, interface do
   produto, foto de ambiente real, ou citação/frase em tela cheia. Confira
   contra a "Personalidade visual" do documento de identidade da marca
   (ex.: Goalfy prioriza interface real ou dado numérico, nunca banco de
   imagens genérico; Hapo Educação prioriza cena de imersão real).

## Parte 1 — Headline da arte

Regras:

- **Curta**: pense em até 8-10 palavras. A arte não é um parágrafo — se a
  frase não cabe confortavelmente em destaque na composição, está longa
  demais.
- **Mesmo teste standalone da `hooks-library`**: remova mentalmente o resto
  do criativo (legenda, CTA) — a headline sozinha precisa gerar tensão ou
  identificação imediata.
- **Nunca repete o que a legenda vai dizer depois** — a legenda (escrita
  depois que a arte está pronta, via `ad-creative-copy`) precisa reforçar
  um ângulo que a headline da arte NÃO cobre, então decida aqui o que a
  imagem "diz" para não duplicar depois.
- **Calibrada pelo perfil de marca**: siga a categoria de gancho dominante
  da marca (pergunta com custo concreto para Goalfy; contraste "Não é X. É
  Y." para Hapo Educação; reframe declarativo para Assessoria — nunca cruze
  o padrão de uma marca para outra).
- **Nunca usar "-"** (hífen, travessão ou meia-risca) na headline.
- **Nunca usar "." no final da headline nem do texto de apoio/subheadline**
  impressos na arte (validado em 2026-08-11, Goalfy). O ponto final é
  aceitável em CTA de legenda/post (`ad-creative-copy`), mas nunca no texto
  que vai dentro da própria imagem — headline e subheadline sempre terminam
  sem pontuação. Vale também para qualquer edição posterior: se o texto já
  saiu com ponto, apagar (mancha pequena e isolada, fácil de recortar sem
  mexer no resto da frase) antes de considerar a peça pronta.

## Parte 2 — Prompt de geração de imagem

Monte o prompt em blocos, nesta ordem, para colar direto no ChatGPT (ou
outro gerador de imagem):

```
1. FORMATO: <proporção exata, ex. "1080x1080px, formato quadrado para
   Feed Instagram/Facebook">

2. REFERÊNCIA DE COMPOSIÇÃO: <descreva o que da referência do Pinterest
   deve ser mantido — enquadramento, hierarquia visual, forma de destacar
   o elemento central. Não mencione a paleta de cores original aqui,
   ela é substituída no bloco 3>

3. IDENTIDADE VISUAL DA MARCA: <paleta exata da marca (hex, quando
   existir oficialmente) + tipografia + personalidade visual, extraído do
   documento de identidade. Se algum campo for provisório, escreva
   "direção provisória:" antes>

4. ELEMENTO CENTRAL: <o que domina a composição — número/dado, interface
   real, cena de ambiente real, ou frase em destaque — conforme decidido
   na descoberta. Se o elemento central incluir um laptop/notebook,
   inclua sempre as duas instruções da "Regra fixa: proporção realista de
   tela de laptop" acima (proporção numérica 16:10 + densidade de
   conteúdo limitada explicitamente), nunca só uma das duas>

5. TEXTO A INSERIR NA IMAGEM: "<headline exata da Parte 1>" — <indicação
   de posicionamento e legibilidade: contraste sobre o fundo, fonte
   bold, alinhamento>

6. LOGO: posicionado no canto (superior ou inferior), nunca centralizado
   em destaque — o dado/mensagem principal domina o espaço, não o logo.

7. EVITAR: banco de imagens genérico, pessoas sorrindo forçado, estética
   de "anúncio de coach"/infoproduto (gradiente colorido, emoji em
   excesso, promessa gritada), qualquer elemento que fuja da
   personalidade visual descrita no bloco 3.
```

Adapte os blocos ao que a descoberta revelou — não entregue o esqueleto
genérico sem preencher cada campo com a informação real da marca e da
narrativa.

## Parte 3 — Geração automática da arte

Validado em teste real (Goalfy, 2026-08-07/08): comparar a saída do
sistema contra uma arte aprovada manualmente (mesma referência do
Pinterest, workflow Pinterest → ChatGPT → Canva/editor) mostrou que a
arte manual **não confia na IA de imagem para nenhum elemento que precisa
ser lido com nitidez** — texto, logo e a interface do produto são sempre
elementos reais (tipografia real, PNG do logo oficial, screenshot real do
produto), só a "cena" de fundo (pilha de cards, esferas decorativas) é
estilo gerado. A IA de imagem (`gpt-image-1`) nunca reproduziu esses três
elementos de forma confiável, mesmo com prompt bem literal.

**Atualização 2026-08-17 (regra fixa): geração de cena sempre via ChatGPT no
navegador (Via C) — não escolher mais "a via certa pro caso" entre A/B/C.**
As vias A e B seguem documentadas abaixo como referência histórica/contexto
de por que a Via C venceu, mas o processo padrão a partir de agora é sempre
o descrito na Via C.

### Via A — Edição de alta fidelidade sobre a referência real (recomendada quando existe uma referência/arte forte pra editar)

Achado central (validado em teste real, Goalfy, 2026-08-08): comparar a
saída do sistema contra uma arte aprovada manualmente mostrou que o
problema de "ficou muito diferente da referência" não era falta de
capacidade do modelo — era **como a API estava sendo chamada**. O
`gerar_arte.py` sempre regenerava a cena do zero a partir de um prompt
longo redescrevendo a composição inteira, sem usar dois parâmetros que a
função `images.edit` sempre teve: `mask` (edição restrita a uma região,
resto pixel a pixel intacto) e **`input_fidelity="high"`** (instrui o
modelo a preservar ao máximo os pixels da imagem de entrada fora do que
foi pedido). Isso é, muito provavelmente, o mecanismo que o produto
ChatGPT usa por trás quando uma edição parece "pontual" — não é um modelo
diferente, é o mesmo `gpt-image-1` chamado de outro jeito.

Processo:

1. Chame `images.edit` com `image=[<referência ou arte anterior>]`,
   `input_fidelity="high"`, e um prompt **pontual** ("mantenha a
   composição EXATAMENTE como está, mude só X, Y, Z" — nunca redescreva a
   cena inteira). Isso preserva densidade, layout, proporção e esferas
   quase pixel a pixel, e já traduz/ajusta corretamente o texto GRANDE
   (headline) na maioria das vezes.
2. Se algo pontual ainda saiu errado (uma cor, um badge), encadeie outra
   chamada `images.edit` usando o resultado anterior como entrada (não a
   referência original) — edição incremental, como uma conversa,
   preservando o que já ficou certo.
3. **Nunca confie na IA para**: logo (sempre composite o PNG oficial por
   cima depois — ver "Regra fixa de logo" acima) e qualquer texto médio
   que precise estar 100% correto (CTA, subheadline) — sobreponha esses
   com Pillow/fonte real depois da edição de IA, do mesmo jeito que o
   logo. Texto pequeno/decorativo dentro de cards ou listas de interface
   pode ficar como ruído visual autêntico (aceito pelo usuário como
   "decorativo, não precisa ser lido de perto") — não vale a pena gastar
   mais rodadas tentando corrigir isso via IA.
4. Composição/densidade/paleta pela IA (alta fidelidade) + logo/CTA/
   subheadline/headline crítico sobrepostos por código = o resultado mais
   fiel obtido até agora.

### Via B — Template HTML/CSS do zero (recomendada quando NÃO existe uma referência/arte forte pra editar, ou pra variações repetíveis de um mesmo layout)

Quando o ponto de partida é só uma ideia/briefing, sem uma arte de
referência específica pra editar, montar do zero em HTML/CSS e renderizar
com Playwright (`tools/gerar-arte-anuncio/renderizar_html.py`) ainda é
melhor do que pedir pro `gerar_arte.py` compor tudo via prompt — CSS tem
sombra/gradiente/recorte nativos, e nenhum texto/logo passa por geração de
imagem. Processo (generalizado, validado em 2026-08-08 — não escreva posição de
card à mão, use o gerador):

1. Escreva um config JSON com os campos de `Goalfy/Criativos/
   lead-perdido-por-demora/config_generalizado.json` como referência:
   paleta, textos dos cards, esferas, painel/screenshot, headline,
   subheadline, CTA, logo.
2. Gere o HTML a partir do config:
   `python tools/gerar-arte-anuncio/montar_template.py --config <config.json> --saida <template.html>`
   — isso usa `tools/gerar-arte-anuncio/cluster_cards.py` para calcular a
   posição/rotação/escala/profundidade de cada card via distribuição em
   espiral áurea (não uma coluna), com camadas de fundo desfocadas/opacas
   e a de frente nítida — é o que dá a sensação de "pilha", reutilizável
   para qualquer quantidade de cards e qualquer criativo, sem reescrever
   posição nenhuma à mão.
3. Renderize com
   `python tools/gerar-arte-anuncio/renderizar_html.py --html <template.html> --saida <arte.png>`.
4. Se a pilha sair vazando da borda do canvas ou apertada demais (texto
   ilegível por sobreposição excessiva), ajuste `margem_x`/`margem_y`/
   `raio_min_frac` em `cluster_cards.py` — são os únicos parâmetros que
   controlam espalhamento vs. contenção, evite reintroduzir posições
   fixas por card.
5. **Tipografia — sempre a fonte oficial da marca, nunca uma aproximação
   visual.** O template tem um fallback genérico (Poppins, baixada em
   `tools/gerar-arte-anuncio/fontes/`) só para quando não existe fonte
   oficial disponível — mas isso é sempre a segunda opção. Antes de gerar
   qualquer peça, procure a fonte oficial da marca (ex.: `Goalfy/fonts/`
   tem a Red Hat Text real, confirmada em `brand-system-goalfy.html`) e
   aponte o config pra ela via o campo `fontes` (lista de `{familia,
   peso, arquivo}`, caminho relativo ao próprio arquivo de config) +
   `fonte_headline`/`fonte_corpo`/`peso_headline`/`peso_subheadline`/
   `peso_cta`/`peso_card`. Verifique também o peso máximo disponível
   nos arquivos da marca (ex.: Red Hat Text da Goalfy só vai até 700,
   nunca use 800/900 nesse caso — o `README.md` da pasta de fontes da
   marca costuma avisar isso). Só recorra ao fallback Poppins se
   nenhuma fonte oficial for encontrada, e avise o usuário que é uma
   aproximação, não a fonte real.

### Via C — ChatGPT via navegador (recomendada quando a peça tem bastante texto/cena realista e não há template HTML pronto)

Validado em teste real (2026-08-11, Goalfy, "CRM para o vendedor
brasileiro" — duas peças completas, zero erro de texto em ambas). Gerar
pela **interface do produto ChatGPT** (via `claude-in-chrome`, não pela
API `gpt-image-1` crua) produz resultado sensivelmente mais confiável em
texto do que a via API sem alta fidelidade — o produto parece aplicar uma
camada de revisão/correção interna que a chamada de API pura não tem (o
próprio ChatGPT já foi observado se autocorrigindo no meio da geração,
sem eu pedir, ao notar um acento errado ou um texto que saiu quebrado).

Processo:

1. Escolha/adapte uma referência visual (Pinterest, concorrente, banco de
   referências da marca) só como guia de **composição e layout** — nunca
   como algo a editar pixel a pixel se for material de outra marca/empresa;
   deixe isso explícito no prompt ("use apenas como inspiração de
   composição, não copie marca/logo/cores/texto dela").
2. Abra o ChatGPT no navegador, anexe a referência, e escreva o prompt
   como **um parágrafo único, sem quebra de linha** (`\n`) — quebras de
   linha no meio do texto disparam o envio prematuro da mensagem antes de
   terminar de digitar, um bug observado repetidas vezes nesse fluxo.
   Inclua no mesmo parágrafo: identidade da marca (paleta hex exata,
   fundo, personalidade visual), todos os textos exatos entre aspas
   (headline, subheadline, cards, CTA, textos de tela/interface), e a
   instrução explícita de não desenhar logo nenhum (isso entra depois, por
   fora — ver regra fixa de logo).
3. Espere terminar (pode levar 1-3 min, o "Pensando" as vezes já inclui
   uma auto-correção espontânea antes mesmo da primeira entrega).
4. **Baixe a imagem em resolução total** (botão de download no editor,
   não confie no preview reduzido do chat) antes de revisar — erros de
   ortografia pequenos só aparecem nítidos em resolução real.
5. Rode a revisão obrigatória (mais abaixo) sobre o arquivo baixado.
6. Se precisar de ajuste pontual (texto duplicado, elemento grande demais,
   pontuação errada), volte na mesma conversa/imagem e descreva só a
   mudança pontual — o histórico mantém a composição e o ChatGPT edita
   só o que foi pedido, sem regenerar do zero.

### Geração automática via IA sem alta fidelidade (só rascunho exploratório)

O `gerar_arte.py` sem `input_fidelity`/`mask` (composição nova a partir de
um prompt longo) ainda serve pra explorar uma composição nova rapidamente,
mas nunca deve ser a via da entrega final — usa API `gpt-image-1` da
OpenAI, requer `OPENAI_API_KEY` configurada (ver
`tools/gerar-arte-anuncio/README.md`).

Convenção de pastas por projeto: `<Marca>/Criativos/<nome-do-projeto>/`,
com subpastas `referencias/`, `artes-geradas/` e um arquivo `prompt.txt`.
Se essa estrutura ainda não existir para o projeto, crie-a antes de
chamar o script.

Passos:

1. Grave o prompt da Parte 2 em `<Marca>/Criativos/<projeto>/prompt.txt`.
2. Confirme que `<Marca>/Criativos/<projeto>/referencias/` tem pelo menos
   uma imagem de referência (peça ao usuário para colocar ali se ainda não
   tiver feito isso — este script não busca imagens no Pinterest por
   conta própria).
3. Rode o script apontando para essas pastas, escolhendo `--formato`
   conforme o destino decidido na descoberta (feed/stories/reels/wide).
4. Depois que a arte for gerada, **não siga direto para a legenda e não
   apresente o arquivo como pronto** — rode você mesmo a revisão
   obrigatória descrita em "Revisão obrigatória antes de declarar
   pronto" (mais abaixo) contra `references/metas-qualidade-criativo.md`,
   item por item, e corrija qualquer falha antes de mostrar o resultado.
   Geração por IA pode errar cor, proporção ou legibilidade do texto
   mesmo com o prompt correto — e falha sistematicamente em texto
   pequeno/médio (ver item 10 da checklist), então esse tipo de saída
   exige leitura letra por letra de todo texto legível antes de seguir.

Não rode este script sem que o usuário tenha confirmado que quer gerar a
arte pelo sistema agora — sempre ofereça as duas opções (colar no ChatGPT
manualmente vs. gerar direto pelo script) e siga a que o usuário escolher.

### Regra fixa de logo: nunca confiar no redesenho da IA

Validado em teste real (2026-08-07, Goalfy): o `gpt-image-1` não reproduz
de forma confiável o logo oficial mesmo recebendo o arquivo PNG como
referência de imagem — ele redesenha algo parecido, mas comete erros
estruturais (ex.: pintou uma perna do "y" de roxo em vez de manter o
pequeno triângulo roxo solto acima da letra, e depois de duas tentativas
de correção via prompt ainda não conseguiu adicionar o triângulo). Regerar
a imagem inteira tentando corrigir só o logo tem alto risco de desarrumar
outro elemento que já estava certo (efeito cascata observado no teste).

**Reteste em 2026-08-11 pelo ChatGPT via navegador (não API), mesmo
resultado.** Mesmo anexando o arquivo PNG oficial e pedindo explicitamente
"use exatamente este arquivo, sem redesenhar o wordmark ou o triângulo",
e mesmo o modelo respondendo que ia aplicar "como composição direta,
arquivo bloqueado como invariável" — o resultado final ainda foi um
logo **recriado**, não compositado: bordas com halo/brilho suave
(impossível num PNG vetorial real) e o triângulo roxo encostando no "y"
em vez de flutuar separado como no arquivo real. Ou seja, a limitação
não é específica da API `gpt-image-1` sem `input_fidelity` — o mesmo
comportamento se repete na interface do produto, mesmo quando o modelo
"promete" preservar o arquivo literalmente. **Conclusão: a regra vale
sem exceção para qualquer via de geração por IA (API ou ChatGPT via
navegador)** — o logo sempre entra depois, por fora, via Pillow.

**Por isso, sempre que a arte incluir o logo da marca, faça isso em vez de
tentar acertar o logo só via prompt:**

1. Gere a arte normalmente via `gerar_arte.py`, sem se preocupar em
   perfeccionar o logo no prompt (descreva a posição/tamanho esperado,
   mas não gaste rodadas de regeneração só por causa dele).
2. Depois que a composição geral estiver aprovada (cards, painel,
   headline, paleta), sobreponha o **arquivo PNG oficial do logo**
   (`<Marca>/Logo PNG/...`) por cima da área onde a IA desenhou o logo,
   usando Pillow: (a) meça a bounding box do logo desenhado pela IA
   (região de pixels claros no canto onde o logo deveria estar,
   cuidando de não invadir o card/elemento vizinho abaixo), (b) preencha
   essa área com a cor de fundo da própria arte (amostrada de um ponto
   próximo, vazio), (c) redimensione o logo oficial mantendo a proporção
   original e cole com `alpha_composite` na mesma posição.
3. Escolha a versão do logo (clara/escura) pela regra já documentada em
   `references/identidade-visual-por-marca.md` / `IDENTIDADE_VISUAL.md`
   da marca (fundo escuro → versão branca; fundo claro → versão grafite).
4. Salve o resultado como a versão final — não repita geração pelo
   `gpt-image-1` só para tentar acertar o logo de novo.

Isso vale para qualquer marca do grupo com arquivo de logo oficial em
pasta própria, não só Goalfy.

**Ao apagar o retângulo/tracejado reservado para o logo sobre um fundo
fotográfico (não uma cor sólida), nunca preencher com uma cor lisa
amostrada de um ponto próximo.** Validado em 2026-08-20 (Goalfy,
"adapte-ao-seu-jeito"): preencher a área reservada com uma cor sólida
(mesmo bem amostrada) deixa uma emenda retangular visível quando o fundo
real é uma foto com gradiente/textura (ex. parede de escritório) — a cor
fica próxima, mas nunca idêntica ao gradiente real. A correção que
funcionou foi usar inpainting de verdade (`cv2.inpaint`, biblioteca
`opencv-python-headless`) sobre uma máscara binária dos pixels do
tracejado/retângulo (detectados por diferença de matiz em relação ao
fundo, ex. `warmth = R - B` para fundos quentes), dilatando a máscara
alguns pixels pra cobrir a antialiasing antes de rodar o inpaint. Isso
reconstrói a textura a partir da vizinhança real em vez de aplicar uma
cor plana, e não deixa nenhuma emenda visível. Só usar preenchimento de
cor sólida quando o fundo ao redor já for comprovadamente liso/sem
gradiente (ex. fundo escuro sólido tipo `#0E0E10`).

## Regra fixa: proporção realista de tela de laptop, sempre que o elemento central incluir um notebook

Validado em 2026-08-20 (Goalfy, "informação duplicada" e "ponta a ponta").
Sem instrução numérica explícita, a Via C (ChatGPT via navegador) desenha
a tela do notebook perto de uma proporção quadrada (~1:1), quando a tela
real de um laptop (MacBook e a maioria dos notebooks) é bem mais larga
que alta, 16 por 10 (~1.6:1). Pedir só "formato widescreen" ou "laptop
realista" de forma genérica não é suficiente — a correção que funcionou
na prática teve duas partes, sempre juntas:

1. **Instrução numérica explícita de proporção, com comparação concreta
   e reforço de "não é tablet".** Validado em 2026-08-21
   (Goalfy, "suporte-atendimento-ia"): a frase "16 por 10, largura 1.6x a
   altura" sozinha já foi insuficiente numa edição pontual — a tela saiu
   larga o bastante pra passar despercebida na hora mas ainda lida como
   vertical/quase quadrada pelo usuário depois. A formulação que
   funcionou de fato teve reforço duplo: o número (16:10, ~1.6x) **e**
   uma comparação sensorial concreta ("tela BEM mais larga que alta, tipo
   uma tela de cinema widescreen, NÃO um retângulo alto/vertical, não uma
   tela de tablet em pé") — inclua as duas formas juntas, o número sem a
   comparação (ou vice-versa) tende a regredir pra proporção quase
   quadrada de novo.
2. **Densidade de conteúdo reduzida o suficiente para caber nessa
   proporção sem esticar, com número máximo explícito.** A causa raiz do
   problema não é só a falta do número de proporção — é que o modelo
   tenta caber todo o conteúdo pedido de forma legível e estica o canvas
   verticalmente pra isso, mesmo já tendo recebido a instrução de
   proporção. Dê um teto explícito e baixo (ex. "mostre no máximo 4 ou 5
   contatos na lista, não mais", "mostre só 2 linhas de cards por coluna,
   não 4, mantendo as mesmas 5 colunas") — nunca deixe a quantidade de
   conteúdo em aberto, e prefira pedir menos do que o suficiente (é mais
   fácil o usuário aceitar uma lista mais curta do que uma tela
   desproporcional).

**Sempre que QUALQUER prompt enviado à Via C for produzir uma imagem com
laptop/notebook mostrando a tela do produto, inclua as duas instruções
acima juntas no mesmo prompt, por padrão — não só quando o usuário
reclamar da proporção depois.** Isso vale tanto para o bloco 4
(ELEMENTO CENTRAL) de uma geração nova quanto para um **prompt de edição
pontual sobre uma peça já existente** (ex. trocar headline/texto de apoio/
tag numa peça que já tem notebook na composição) — mesmo quando a
instrução diz "mantenha tudo exatamente igual", a Via C pode redesenhar a
tela do notebook como efeito colateral da edição e esticá-la para uma
proporção quase quadrada (validado em 2026-08-21, Goalfy,
"suporte-atendimento-ia": uma edição pontual de texto, sem menção ao
notebook, ainda assim desproporcionou a tela). Nunca assuma que "não
mexi nisso no prompt" significa "não vai mudar" — sempre inclua as duas
instruções de proporção/densidade em qualquer prompt cuja imagem final
tenha notebook, mesmo que o pedido do usuário seja só sobre texto/tag/
outro elemento. Se uma geração ainda sair desproporcional
(tela quase quadrada), não é preciso regerar do zero: peça a edição
pontual na mesma conversa reforçando os dois pontos juntos (proporção
numérica + menos conteúdo), que foi o que corrigiu no teste real — uma
correção que mudou só a proporção sem reduzir o conteúdo não foi
suficiente na primeira tentativa.

## Regra fixa: telas do produto sempre vêm de print real, nunca desenhadas/geradas

Validado em 2026-08-17, atualizado em 2026-08-19. Sempre que o criativo
incluir uma tela do software (painel, CRM, inbox, dashboard, qualquer
print de interface), a composição parte de um screenshot real do produto
Goalfy — buscado em `Goalfy/Prints telas goalfy/` (confirmado com o
usuário em 2026-08-17). Se a pasta estiver vazia ou não tiver o print
certo pro caso (tela/fluxo específico do briefing), pare e peça ao usuário
para salvar o print necessário ali antes de seguir.

**Atualização 2026-08-19 (regra fixa): o print real entra como imagem
anexada na própria geração do ChatGPT (Via C), não é mais compositado por
fora depois.** Testado nas duas formas em `crm-1-brasil-customizacao`:
compositar um print real (mesmo anonimizado) por cima de uma cena já
gerada deu resultado visual ruim (blur/mockup genérico visivelmente
colado, foi a queixa do usuário). Anexar o print real como segunda imagem
de referência no mesmo prompt da Via C, pedindo pra reproduzir a mesma
estrutura (colunas, cards, cores de status) só que redesenhada com nitidez,
deu resultado muito superior — sem blur, tela nítida, estrutura fiel ao
produto real. Ver a regra de anonimização logo abaixo para como isso muda
o processo quando a tela vai ser redesenhada pelo próprio ChatGPT.

**Reforço 2026-08-24 (SEMPRE, sem exceção — vale também para ajuste/edição
de peça já existente, não só geração nova):** essa regra não é só para
quando a peça nasce do zero. Toda vez que uma tela de produto precisa
entrar ou ser trocada numa arte — nova ou já existente/aprovada — a tela
real entra **no mesmo passo de geração/edição via ChatGPT (ou outra IA
generativa)**, nunca depois via Pillow/OpenCV (warp de perspectiva,
`cv2.getPerspectiveTransform`, inpaint, paste, etc.). Caso real que gerou
esse reforço: pediram para aplicar telas reais numa peça já pronta
(`goalfy-crm-vendedor-brasileiro-v2-FEED.png`) — a primeira tentativa foi
medir os cantos da tela do notebook/celular a pixel e compositar o print
real por cima com OpenCV; o resultado ficou "ruim" segundo o usuário (fundo
com halo/blur sutil nas bordas do warp, ainda que sem os erros grosseiros
de antes). Refeito enviando a peça original + os prints reais como imagens
de referência pro ChatGPT e pedindo pra regenerar a cena inteira mantendo
tudo igual exceto a tela — resultado muito superior, sem nenhum artefato de
composição, e ainda corrigiu de graça a proporção 16:10 do notebook. Pillow
continua sendo a ferramenta certa **só** para acabamento determinístico que
não é a tela em si (cor exata da marca, logo pixel-perfeito — ver
[[logo_sempre_compositar_manual]]) — para a tela do produto, é sempre
ChatGPT/IA generativa no mesmo passo, nunca pós-composição.

## Regra fixa: anonimizar dados reais antes de usar qualquer screenshot de produto

Validado em 2026-08-08: uma screenshot real do produto (ver "Regra fixa de
logo" e a via A de geração) frequentemente contém dados reais de clientes
(nomes, telefones, fotos de perfil) — isso é dado sensível e **nunca** deve
ir para um criativo publicado sem anonimizar antes, mesmo que a screenshot
já esteja recortada/pequena na peça final. Processo (Pillow, sem IA,
determinístico):

1. Meça a posição exata de cada elemento sensível (nome, telefone, foto)
   sobre a screenshot original — não estime de olho; sobreponha uma grade
   de coordenadas na imagem (linhas verticais/horizontais com o valor do
   pixel escrito) e leia a posição real antes de escrever qualquer
   coordenada no código. Confirme o espaçamento entre linhas/registros
   (ex.: cada linha de uma lista de contatos costuma ter altura fixa) para
   generalizar a mesma correção a todas as linhas de uma vez.
2. **Nomes e telefones: sempre trocar por dado fictício, sem perguntar.**
   Preencha a área exata do texto original com a cor de fundo local
   (branco, na maioria dos apps) e escreva o dado fictício por cima com
   fonte real (nunca IA) — cuidado para a caixa de preenchimento não
   invadir a linha de cima/baixo (subtítulo, badge de status) nem ficar
   curta demais e deixar resíduo do texto real visível, e não avançar
   sobre a área da foto (deixe uma margem de alguns pixels depois da
   borda direita da foto antes de começar o texto).
3. **Fotos de perfil: o padrão é trocar por um círculo colorido + iniciais
   do nome fictício** (nunca deixe a foto real "espiar" nas bordas — raio
   pequeno demais é o erro mais comum). Só mantenha as fotos reais das
   pessoas se o usuário confirmar explicitamente que quer isso (validado
   em 2026-08-08: usuário preferiu manter fotos reais e só fictício em
   nome/telefone) — nesse caso, garanta que a caixa de texto do dado
   fictício nunca sobrepõe a foto (regra do passo 2 acima).
4. Confira visualmente o resultado (zoom em cada linha) antes de usar na
   peça final — o mesmo princípio de "nunca aceitar o primeiro resultado
   sem checklist" que já vale para logo e texto gerado por IA.
5. Dados fictícios devem ser claramente não reais (nomes comuns
   genéricos, números de telefone que não formem um número real válido
   conhecido) — não precisa ser aleatório ao ponto de parecer bugado, só
   não pode ser rastreável a uma pessoa real.

Esse processo 100% Pillow continua valendo quando a tela vai ser usada
como está (sem passar pela Via C de novo). **Quando a tela vai ser
redesenhada pelo ChatGPT (ver atualização 2026-08-19 acima), o processo
muda:**

1. **Nunca anexe o print cru (com PII real) ao ChatGPT.** Mesmo
   instruindo o modelo a trocar nomes/telefones por dado fictício, mandar
   uma tela com dado real pra um serviço externo é o único cenário que
   pode vazar PII de verdade — sem necessidade, já que existe alternativa
   sem esse risco.
2. **Anexe a versão já anonimizada** (`Goalfy/Prints telas goalfy/
   anonimizado/*-ANONIMIZADO.png`) só como referência **estrutural**
   (colunas, cards, posição dos badges de status) — nunca peça pro modelo
   preservar o blur.
3. **No mesmo prompt, peça explicitamente pra redesenhar o conteúdo
   interno de cada card com texto nítido e legível (nunca borrado),
   usando nomes de empresa/contato totalmente fictícios e plausíveis,
   mantendo a mesma paleta de cores dos badges de status.** Resolve os
   dois problemas de uma vez: elimina o blur sem expor dado real, porque a
   fonte anexada já não tinha PII.
4. Se a screenshot real disponível já estiver nítida e sem PII de pessoa
   física (ex.: só nomes de empresa, sem contato/telefone individual —
   caso de `Gestao de tarefas lista - ANONIMIZADO.png`), pode ser anexada
   direto sem essa instrução extra de redesenho, só pedindo pra manter a
   estrutura.
5. Depois de gerado, rode a revisão obrigatória normalmente: letra por
   letra em cada card, confirmando que nenhum nome/empresa/dado da
   screenshot original sobrevive no resultado.

Validado em 2026-08-19 (Goalfy, `crm-1-brasil-customizacao` e
`gestao-de-tarefas`) — ambos sem blur e sem PII no resultado final.

## Regra fixa: toda peça sai sempre em Feed + Stories

Validado em 2026-08-11 (Goalfy). Por padrão, **toda arte gerada por este
processo é entregue em duas versões**: Feed (quadrado, 1080x1080px) e
Stories/Reels (vertical, 1080x1920px) — não só o formato que o usuário
pediu originalmente, a menos que ele diga explicitamente que só precisa de
um. Não faça isso redimensionando/cortando a peça já pronta (perde
elementos ou aperta o layout) — gere cada formato separadamente pela
mesma via (ChatGPT via navegador, reaproveitando a mesma referência e o
mesmo texto), pedindo pra reorganizar a composição pro novo formato (mais
compacto no quadrado, com mais respiro vertical no formato alongado), e
rode a revisão completa (checklist + logo) em cada um individualmente —
são peças diferentes, não a mesma peça redimensionada.

## Regra fixa: nomear e checar sobreposição antes de entregar

Validado em 2026-08-11 (Goalfy). Dois problemas reais nessa etapa final:

1. **Confusão de arquivo no Downloads do usuário.** Cada clique em
   "Baixar imagem" no editor do ChatGPT salva uma cópia crua (sem logo,
   sem correção de cor) direto na pasta Downloads do usuário, com nome
   genérico tipo `ChatGPT Image <data>.png`. Se o arquivo final (com logo
   e cor corrigida) for salvo com nome parecido ou não copiado de volta
   pra essa mesma pasta, o usuário abre o arquivo errado e acha que uma
   etapa (o logo, por exemplo) "sumiu" — quando na verdade só nunca
   entrou naquele arquivo específico. Sempre salve a versão final com um
   nome claramente diferente (prefixo `<marca>-<projeto>-FINAL`, `-FEED`,
   `-STORY`) na mesma pasta que o usuário usa, e informe o nome exato do
   arquivo certo na entrega.
2. **Sobreposição geométrica do logo com outro elemento.** Conferir que o
   arquivo do logo (PNG oficial) está correto e é a versão certa pro fundo
   NÃO é suficiente — é preciso também medir se a caixa (bounding box) do
   logo colide com a caixa de outro elemento (CTA, headline, foto). Antes
   de posicionar o logo, meça por pixel a faixa vazia real onde ele vai
   entrar (não assuma que "canto superior esquerdo" está sempre livre —
   depende de onde a headline começa em cada composição/formato
   específico) e só então defina a posição.

## Metas de qualidade consolidadas (usar com `/goal`)

Todas as regras fixas acima (referência como premissa base, logo,
anonimização, tipografia oficial, etc.) estão consolidadas num checklist
único e verificável em `references/metas-qualidade-criativo.md`. Para
revisar/ajustar um criativo de forma autônoma até tudo passar, use o
comando nativo do Claude Code:

```
/goal revisar o criativo em <caminho> contra Skills/ad-art-brief/references/metas-qualidade-criativo.md e ajustar até todas as metas passarem
```

## Revisão obrigatória antes de declarar "pronto" (não pular, não delegar ao usuário)

Falha real registrada em 2026-08-11 (Goalfy, "gestão de atividades de
equipe"): uma peça gerada por `gerar_arte.py` sem alta fidelidade saiu com
logo ausente, sem CTA e com texto de apoio/cards ilegível ou com erro
ortográfico grave em quase todo texto pequeno/médio (ex. "não são mais
quiões", "Tarches conciualies", um post-it com glifo que nem é letra
latina) — e foi entregue ao usuário como se estivesse pronta. A causa não
foi a checklist (`references/metas-qualidade-criativo.md`) estar
incompleta; foi o processo pedir para o **usuário** conferir visualmente
em vez de o agente rodar a checklist antes de considerar a tarefa
concluída.

Regra fixa a partir de agora, para **qualquer** via de geração (Via A,
Via B, ou `gerar_arte.py` exploratório):

1. Depois de gerar/editar a arte e antes de escrever qualquer coisa como
   "arte pronta", "aqui está o criativo" ou seguir para a legenda, rode
   você mesmo, no chat, a revisão completa de
   `references/metas-qualidade-criativo.md` contra o arquivo final —
   liste cada item aplicável como PASSA ou FALHA com a evidência
   concreta (medição, ou a transcrição exata do texto lido letra por
   letra), do mesmo jeito que uma revisão feita a pedido do usuário.
2. Preste atenção especial ao item 10 (texto gerado por IA): leia em voz
   alta (mentalmente, letra por letra) todo texto que apareça na peça,
   por menor que seja — headline, subheadline, CTA, labels de card,
   post-its, texto de interface simulada. Qualquer palavra sem sentido,
   erro ortográfico ou glifo estranho é FALHA automática do item, mesmo
   que pareça "decorativo".
3. Confirme também os itens estruturais que são fáceis de esquecer
   numa geração por IA: logo presente e é o PNG oficial (item 3), CTA
   presente se o formato pede um (item 8).
4. **Se qualquer item aplicável falhar, corrija antes de entregar** —
   regenere, edite (`images.edit` com `input_fidelity="high"`), ou
   sobreponha texto/logo reais com Pillow, conforme a falha. Repita a
   revisão até todos os itens aplicáveis passarem.
5. Só existem duas saídas aceitáveis para esta etapa: (a) todos os itens
   aplicáveis passam e você entrega a peça como pronta, ou (b) uma falha
   exige uma decisão que só o usuário pode tomar (ex.: manter foto real
   de cliente em vez de anonimizar) — nesse caso, pare e pergunte
   especificamente sobre essa decisão, mas não apresente a peça como
   "pronta" enquanto isso estiver em aberto.
6. Pedir para o usuário "abrir e conferir visualmente" deixa de ser um
   passo válido de encerramento — é, no máximo, um convite para revisão
   extra depois que a sua própria revisão já passou.

## Checklist final

- [ ] A headline da arte foi calibrada pelo perfil de marca (`brand-voice`),
      não decidida por conta própria.
- [ ] A headline passa no teste standalone (funciona sozinha, sem o resto
      do criativo).
- [ ] A headline não usa "-" como pontuação ou marcador.
- [ ] O prompt de imagem usa a paleta/tipografia real do documento de
      identidade da marca — nenhum hex ou fonte foi inventado.
- [ ] Onde o documento de identidade tem campo `⚠️ PREENCHER`, o brief usa
      a direção provisória documentada e avisa que é provisório.
- [ ] O prompt especifica a proporção/formato correto para o destino
      (Feed, Stories, etc.).
- [ ] O elemento central da composição está alinhado com a "Personalidade
      visual" da marca (nunca banco de imagens genérico para Goalfy, nunca
      palco/palestrante para Hapo Educação).
- [ ] A headline da arte não antecipa o que a legenda (etapa seguinte, já
      com a arte pronta) vai dizer.
- [ ] Independente da via de geração, a revisão obrigatória (seção acima)
      foi rodada pelo próprio agente contra
      `references/metas-qualidade-criativo.md`, item por item, com todo
      texto legível checado letra por letra — não apenas assumida ou
      delegada ao usuário — antes de seguir para a legenda.
- [ ] Se a arte inclui o logo da marca, o logo final é o arquivo PNG
      oficial sobreposto via Pillow (ver "Regra fixa de logo" acima), não
      o logo redesenhado pela IA — nunca aceitar o redesenho da IA como
      versão final do logo.

## Quando NÃO usar

- **Ainda não existe uma narrativa decidida** → use `creative-concept`
  primeiro.
- **A arte já está pronta e o pedido é a legenda do post** → use
  `ad-creative-copy` ou `social-post-copy`.
- **O pedido é só um gancho/abertura, sem contexto de arte** → use
  `hooks-library`.
- **O pedido é a estrutura visual de uma landing page** → use
  `landing-page-design`.
