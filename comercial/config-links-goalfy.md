# Links de relatório do Goalfy (funil e vendas)

Os scripts em `scripts/` (`puxar_relatorio.py` etc.) puxam dados direto do
Goalfy via um link de download com `apiKey` (JWT) de escopo **ADMIN** embutido
na URL. Esse link **não está neste repositório** — nunca deve ir para nenhum
repositório git, nem privado, porque quem tiver a URL consegue baixar os
relatórios sem outro tipo de login.

## Como conseguir um novo link

1. No Goalfy, como admin, gerar o link de exportação do board/relatório de
   funil (pré-vendas) e do board de vendas.
2. Cada link tem um `apiKey` próprio — guardar em local seguro (não em texto
   puro em pasta sincronizada/compartilhada). O formato usado antes era um
   arquivo local `.md` fora do controle de versão, com a anotação
   `sensível: true` no topo.
3. Os scripts em `scripts/` esperam esse link como input — ver o cabeçalho de
   `puxar_relatorio.py` para o formato exato esperado.

Se o download começar a falhar com 401/403, o token expirou e um novo link
precisa ser gerado.
