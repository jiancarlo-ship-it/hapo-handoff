# Identidade visual por marca — resumo rápido

Consolidado a partir dos documentos completos de cada marca. Este arquivo é
um atalho de consulta — se algo parecer desatualizado, confira o documento
completo listado em cada seção antes de montar o brief.

---

## Goalfy

Fonte completa: `brand-systems/` deste repo não tem a Goalfy — ela tem
**repositório próprio**: [`goalfy-brand-system`](https://github.com/jiancarlo-ship-it/goalfy-brand-system)
(tokens extraídos 1:1 do site ao vivo, fontes e logo em `assets/`).

- **Personalidade visual**: autoridade técnica sem frieza. Executivo, não
  burocrático. Universo visual de "sala de operações comerciais", nunca
  startup de produto consumer.
- **Paleta oficial** (confirmada, extraída de goalfy.com.br em ago/2026 —
  ver `src/styles/tokens.css` no repo `goalfy-brand-system`): roxo de marca
  `#7F23F7` (primary) / `#8C31FF` (secondary) / `#5D29A1` (botão). Fundo
  escuro ou claro conforme o token de superfície, destaque em cor vibrante
  única para o dado/número principal, evitar gradientes coloridos.
- **Tipografia oficial** (confirmada): **Red Hat Text** — nunca uma
  aproximação genérica tipo Poppins. Arquivos reais em `assets/fonts/` no
  repo `goalfy-brand-system`, peso máximo 700.
- **Elemento central preferido**: número/dado grande em destaque, ou
  interface real do Goalfy em uso (nunca mockup idealizado).
- **Evitar**: banco de imagens genérico, pessoas sorrindo forçado, estética
  de startup consumer, gradientes coloridos (leem como infoproduto).
- **Logo**: canto superior esquerdo ou inferior, nunca centralizado em
  destaque. Arquivo real em `assets/logo/` no repo `goalfy-brand-system`.

> Nota: os documentos antigos (`Goalfy/Contexto e Identidade/IDENTIDADE_VISUAL.md`)
> ainda marcam paleta/tipografia como `⚠️ PREENCHER` — isso ficou
> desatualizado depois que o design system foi extraído do site real em
> ago/2026. Os valores acima são os corretos.

## Hapo Educação

Fonte completa: [`brand-systems/hapo-educacao/IDENTIDADE_VISUAL.md`](../../../brand-systems/hapo-educacao/IDENTIDADE_VISUAL.md)

- **Personalidade visual**: aplicação prática com energia contida — nem o
  friozão executivo da Goalfy, nem a euforia do infoproduto. Universo
  visual de "sala de imersão com pessoas trabalhando", nunca palco com
  palestrante.
- **Paleta**: ainda não tem hex oficial próprio confirmado — pendência real,
  não decidida no handoff. Direção provisória: pode ser mais clara/quente
  que a Goalfy, mas sem saturação que remeta a infoproduto; a diferenciação
  da Goalfy precisa ser perceptível, mantendo o grupo reconhecível.
- **Tipografia**: decidido no handoff (21/09/2026) — usa a mesma da Hapo
  Assessoria/marca mãe: **SF Pro Display** (materiais premium) ou
  **Nunito Sans** (Canva/digital). Deixou de ser pendência.
- **Elemento central preferido**: entregável concreto da imersão (créditos,
  agente de IA), ou cena real de alunos trabalhando no computador — nunca
  posando.
- **Evitar**: banco de imagens de "pessoas estudando felizes", auditório
  com palestrante, abertura com logo animado.
- **Logo**: presente mas não dominando o layout. Arquivo real em
  `brand-systems/hapo-educacao/assets/`.

## Hapo Assessoria (hapo.marketing)

Não tem documento de identidade visual próprio — usa a identidade da marca
mãe do Grupo Hapo. Fonte completa: [`brand-systems/grupo-hapo-marca-mae/README.md`](../../../brand-systems/grupo-hapo-marca-mae/README.md)

- **Paleta oficial** (hex reais, não provisórios):

  | Nome | Hex | Uso |
  |------|-----|-----|
  | Dark Energy | `#0D0E0E` | Cor principal da identidade |
  | Marte | `#E84A18` | Detalhes, fundos e acentos |
  | Light | `#F2F2F2` | Complementar / fundos |
  | Mercúrio | `#666666` | Textos secundários |

- **Tipografia**: SF Pro Display (materiais premium/Adobe) ou Nunito Sans
  (Canva e plataformas digitais).
- **Personalidade**: autoridade visionária com clareza prática. Formal,
  séria, realista com visão de futuro, exclusiva, profissional.
- **Identidade fotográfica**: bastidores reais, reuniões, processos
  autênticos. Evitar banco de imagens (stock), poses artificiais,
  composições genéricas.
- **Elemento de apoio**: a seta (`assets/seta.png`) representa evolução
  diária — coerente com o fechamento de CTA da Assessoria usar seta (ver
  `Skills/brand-voice/references/perfil-hapo-assessoria.md`).
- **Proibido**: esticar/distorcer/inclinar o logo, sombras/contornos/
  efeitos no logo, cores fora da paleta oficial, imagens de stock ou poses
  artificiais.
- **Ícones**: Google Material Icons apenas, estilo único sem preenchimento.

---

## Nota sobre campos `⚠️ PREENCHER`

Atualizado no handoff (21/09/2026): Goalfy já tem paleta e tipografia
confirmadas (ver seção acima, fonte é o repo `goalfy-brand-system`) e Hapo
Educação já tem tipografia decidida. Só falta o hex oficial da **paleta de
Hapo Educação**, que continua provisório — ao montar um prompt de imagem
para essa marca, use a direção provisória listada acima e sinalize no brief
entregue ao usuário que aquele ponto é provisório, não decida um hex
específico "chutado" como se fosse oficial.
