# Metas de qualidade — criativo de anúncio (checklist verificável)

Consolidado a partir do teste real Goalfy "Pare de perder leads no seu
CRM" (2026-08-07/08), onde cada meta abaixo foi a causa de uma rodada de
correção. Use esta lista para revisar QUALQUER criativo gerado pelo
sistema (`gerar_arte.py`, `montar_template.py` + `renderizar_html.py`, ou
edição de alta fidelidade) antes de considerar pronto. Cada meta é
binária (passa/falha) e, sempre que possível, verificável por medição
direta na imagem — não por impressão visual solta.

Para rodar isso de forma autônoma (ajustar e regenerar até tudo passar),
use o comando nativo do Claude Code:
```
/goal revisar o criativo em <caminho> contra Skills/ad-art-brief/references/metas-qualidade-criativo.md e ajustar até todas as metas passarem
```

## 1. Fidelidade à referência (se existir uma)

- [ ] **Alinhamento medido, não assumido.** Para headline/subheadline/CTA,
      calcule a bounding box de cada linha na referência e compare
      centros. Linhas de larguras diferentes com centros ~iguais (±10px)
      = centralizado. Bordas esquerdas iguais = alinhado à esquerda.
      Replique o mesmo padrão medido, não uma convenção genérica.
- [ ] **Tamanho da headline proporcional ao canvas.** Meça a largura da
      linha mais longa da headline na referência ÷ largura do canvas.
      A peça nova deve reproduzir essa mesma proporção (±10 pontos
      percentuais), não um tamanho de fonte arbitrário.
- [ ] **Margens e espaçamento vertical proporcionais**, não só copiados
      em pixels absolutos se o canvas mudar de tamanho — sempre como
      proporção do canvas (%), medida na referência.

## 2. Tipografia

- [ ] **Fonte oficial da marca, não uma aproximação visual.** Procure uma
      pasta de fontes oficiais da marca (ex. `<Marca>/fonts/`) antes de
      cair no fallback genérico (Poppins) do template. Se usar o
      fallback, avise explicitamente que é aproximação.
- [ ] **Peso dentro do limite real da marca** (nunca inventar peso 800/900
      se a fonte oficial só vai até 700 — checar o `README.md`/licença da
      pasta de fontes).

## 3. Logo e margens gerais — verificado automaticamente

- [ ] **Sempre o arquivo PNG/SVG oficial compositado por cima**, nunca o
      logo redesenhado por uma IA de imagem (gpt-image-1 e similares não
      reproduzem logos pequenos de forma confiável, mesmo com o arquivo
      como referência).
- [ ] **Versão certa pro fundo** (clara em fundo escuro, escura em fundo
      claro), conforme documentado na identidade visual da marca.
- [ ] **Respiro e margens verificados automaticamente pelo sistema**, não
      por inspeção visual: rode
      `python tools/gerar-arte-anuncio/verificar_margens.py --config <config.json>`
      (ou deixe rodar sozinho — `montar_template.py` já chama isso no
      final de toda montagem de template). Ele mede, direto no config
      (não na imagem), pra cada elemento (painel, headline, CTA):
      margem até as 4 bordas do canvas ≥ 3,5% do lado menor do canvas, e
      respiro entre o logo e qualquer outro elemento ≥ 2,8% do lado
      menor. A pilha de cards é exceção de propósito (fica perto do
      canto por estilo, ver referência aprovada) — só o respiro dela
      contra o logo é checado, não a margem de borda.
- [ ] **Se a checagem falhar**, ajustar as coordenadas no config (nunca
      só na saída renderizada) e rodar de novo — os limites (`MINIMO_BORDA_PCT`,
      `MINIMO_LOGO_PCT` em `verificar_margens.py`) foram calibrados contra
      a peça aprovada como referência; se uma peça nova exigir um limite
      diferente por um motivo real de layout, ajustar a constante ali
      (documentando o motivo), não ignorar a falha.

## 4. Contraste entre elementos e fundo

- [ ] **Nenhum elemento principal (notebook, telefone, painel, pessoa) pode
      ter cor quase igual à do fundo.** Validado em 2026-08-08 (Goalfy,
      "gestão de atividades de equipe"): a primeira geração saiu com o
      notebook quase da mesma cor do fundo escuro, ficando difícil de
      distinguir a composição. Antes de aprovar, confira mentalmente (ou
      medindo a diferença de luminosidade) se o elemento central se
      destaca claramente do fundo — se não destacar, ajuste a cor do
      fundo OU do elemento (não os dois iguais), e considere reforçar
      sombra/contorno do elemento principal para separá-lo do fundo.
- [ ] Isso vale nas duas direções: fundo escuro precisa de elemento claro
      o suficiente pra se destacar, fundo claro precisa que o elemento
      tenha um tom mais escuro/saturado ou uma sombra bem definida.

## 5. Elementos decorativos

- [ ] **Todo elemento decorativo tem função clara na composição** (ancora
      hierarquia, preenche vazio, reforça a marca). Se um elemento da
      referência original (ex. esferas 3D) não se integrar bem à nova
      composição, remover em vez de manter só porque "a referência
      tinha".

## 6. Pilha/cluster de cards (se o formato envolver isso)

- [ ] **Aglomerado orgânico** (várias camadas, tamanhos/ângulos variados),
      nunca uma coluna espaçada uniformemente.
- [ ] **Contido dentro do canvas** — nenhum card vazando da borda.
- [ ] **Sem sobreposição que torne o texto principal ilegível** — cards
      podem se sobrepor parcialmente (é autêntico ao estilo), mas o
      texto de cada card precisa ser lido pelo menos parcialmente/de
      forma reconhecível.

## 7. Screenshot real de produto (se usar)

- [ ] **Recortada para remover espaços vazios/colunas esparsas** antes de
      colar no painel.
- [ ] **Nenhum dado sensível real sem tratamento**: nome, telefone e foto
      de clientes reais devem ser fictícios por padrão. Fotos reais só
      ficam se o usuário confirmar explicitamente — nesse caso, garantir
      que o texto fictício nunca sobrepõe a foto (medir a borda real da
      foto antes de posicionar qualquer caixa de texto por cima).

## 8. CTA

- [ ] **Botão dimensionado ao texto**, não uma largura arbitrária —
      padding lateral generoso (~40 a 70px de cada lado do texto em
      canvas 1080px, escalar proporcionalmente), nunca um pílula muito
      mais larga que o texto exige.
- [ ] **Uma frase imperativa só**, sem emoji/seta (salvo se o perfil de
      marca definir diferente).
- [ ] **Sem ponto final no CTA da arte** (validado 2026-08-11).

## 9. Copy e regras de marca

- [ ] **Checar `Skills/brand-voice/references/perfil-<marca>.md`** antes
      de escrever qualquer texto — ordem fixa de menção de produtos
      (ex. Goalfy: sempre CRM, Automações, WhatsApp, IA nessa ordem),
      vocabulário vedado, fechamento de CTA característico, etc.
- [ ] **Texto de apoio (subheadline) numa linha só quando couber no
      espaço disponível** e com tamanho legível mas proporcional à
      referência (não maior "pra garantir legibilidade" nem menor "pra
      caber" sem antes tentar ajustar largura da caixa).
- [ ] **Sem ponto final na headline nem no texto de apoio/subheadline**
      impressos na arte (validado 2026-08-11) — só o corpo da legenda do
      post e, quando fizer sentido, o CTA de legenda usam ponto final.

## 10. Geração por IA de imagem (quando usada)

- [ ] **Nunca aceitar texto médio/grande (headline, subheadline, CTA)
      gerado por IA sem verificação de ortografia/gramática letra por
      letra** — preferir sempre texto real (HTML/CSS) ou, se vier de
      edição de alta fidelidade, sobrepor por cima com texto real depois.
- [ ] **Se usar `images.edit`, sempre com `input_fidelity="high"`** e um
      prompt de mudança pontual sobre uma referência real — nunca
      redescrever a cena inteira do zero a cada rodada.
- [ ] **Texto pequeno/decorativo (cards de fundo, linhas de interface
      inventada) pode ficar ilegível** — isso é aceito como ruído visual
      autêntico, não vale gastar rodadas de geração corrigindo isso.

## 11. Resolução final da arte (independente da resolução da referência)

- [ ] **A arte final sai sempre em alta resolução, mesmo quando a
      referência usada era um print de baixa qualidade** (validado em
      2026-08-18, Goalfy — referências vindas de screenshots da Biblioteca
      de Anúncios do Meta, comprimidas/pequenas). Resolução da referência
      nunca é herdada pela peça final: exportar sempre no tamanho oficial
      do formato (Feed 1080×1080px, Stories/Reels 1080×1920px), baixando a
      imagem gerada em resolução total (não o preview reduzido do chat) e
      sem upscaling artificial de uma fonte pequena — se a via de geração
      permitir pedir mais resolução (ex. ChatGPT via navegador, botão de
      download do editor), sempre usar a maior disponível.
- [ ] **Nenhum elemento colado por cima (logo, screenshot de produto
      anonimizado) pode ficar com resolução visivelmente menor que o
      restante da peça** — se a fonte do elemento (ex. print real do
      produto) for pequena, redimensionar com cuidado e checar serrilhado/
      pixelização antes de aprovar; se ficar visivelmente inferior, avisar
      o usuário em vez de aprovar como está.

## 12. Proporção realista de dispositivos (laptop/notebook)

- [ ] **Tela do notebook nitidamente mais larga que alta, proporção real
      de 16 por 10 (~1.6:1), nunca quase quadrada.** Validado em
      2026-08-20 (Goalfy, "informação duplicada"): sem instrução numérica
      explícita, a Via C desenha a tela do notebook perto de 1:1
      (quadrada/alta demais), porque tenta caber todo o conteúdo pedido
      (ex. 4 linhas de cards por coluna) de forma legível e estica o
      canvas verticalmente para isso. Meça a largura ÷ altura da tela na
      imagem gerada — se sair abaixo de ~1.4:1, é falha deste item, mesmo
      que o prompt já tivesse pedido "proporção widescreen" de forma
      genérica.
- [ ] **A causa raiz é densidade de conteúdo, não só a instrução de
      proporção.** Corrigir só o texto do prompt pedindo a proporção não
      basta se a lista de itens/linhas pedida para a tela do produto for
      grande demais para caber nela sem esticar — reduzir o número de
      linhas/cards pedidos é parte obrigatória da correção, não opcional.
      Ver `SKILL.md`, seção "Regra fixa: proporção realista de tela de
      laptop" para o texto exato de prompt validado.

## Processo de revisão

Ao revisar uma peça contra esta lista: liste cada item marcado como
FALHA com o que exatamente está errado (não "parece ruim" — aponte a
medição ou o elemento específico), ajuste o config/prompt correspondente,
regenere, e repita até todos os itens aplicáveis passarem. Itens que não
se aplicam ao formato da peça (ex. não há screenshot de produto) são
simplesmente ignorados, não contam como falha.
