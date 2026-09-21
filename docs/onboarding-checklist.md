# Checklist de onboarding — o que pedir no dia do handoff

Este repositório, o `goalfy-brand-system` e a pasta do Drive já contêm o
código, a documentação e os assets de marca. **Nada aqui é segredo.** O que
falta são credenciais e acessos que pertencem ao Jian pessoalmente (contas,
tokens, chaves de API) — por decisão explícita, esses itens **não foram
compartilhados com antecedência**. A próxima pessoa deve pedir cada um deles
diretamente ao Jian no momento da transição, e o Jian deve revogar/trocar
qualquer credencial que não for possível transferir de forma limpa (ver nota
no fim).

## 1. Acesso a repositórios (GitHub)

Pedir para ser adicionado como colaborador (ou pedir transferência de
ownership) em:

- [ ] `jiancarlo-ship-it/hapo-handoff` (este repositório)
- [ ] `jiancarlo-ship-it/hapo-marketing-dashboard`
- [ ] `jiancarlo-ship-it/ad-art-chatgpt-pipeline`
- [ ] `jiancarlo-ship-it/goalfy-brand-system`

## 2. Dashboard de Ads (Render)

O app `hapo-marketing-dashboard` já está no ar. Para acessar/editar/redeployar:

- [ ] Acesso à conta/serviço no [Render](https://render.com) onde está
      hospedado (ou pedir para o Jian adicionar como colaborador no time do
      Render, ou transferir o serviço)
- [ ] Os valores reais das variáveis de ambiente já configuradas lá (não
      precisa recriar do zero, só copiar/confirmar):
  - `META_ACCESS_TOKEN` — token do Meta Marketing API (ver item 3)
  - `GEMINI_API_KEY` — chave do Google Gemini (ver item 4)
  - `GOALFY_PREVENDAS_URL` / `GOALFY_VENDAS_URL` — links do Goalfy (ver item 5)
  - `UPSTASH_REDIS_REST_URL` / `UPSTASH_REDIS_REST_TOKEN` — cache (ver item 6)

## 3. Token do Meta Ads

Usado tanto pelo dashboard quanto pela skill `meta-ads-hapo`.

- [ ] Pedir um **System User Token** novo (não reaproveitar o do Jian) em
      `business.facebook.com` → Configurações do negócio → Usuários do
      sistema → Gerar novo token, com permissão `ads_read` (dashboard) ou
      escopo de gestão completa (se for também editar campanhas via skill),
      para as contas Goalfy, Hapo Educação e Hapo Marketing.

## 4. Google Gemini API key

- [ ] Gerar uma chave própria em [aistudio.google.com/apikey](https://aistudio.google.com/apikey)
      — usada pela aba "Insights" do dashboard.

## 5. Links de relatório do Goalfy (funil e vendas)

- [ ] Pedir ao Jian (ou a um admin do Goalfy) um link novo de exportação do
      board de pré-vendas e do board de vendas — cada um tem um `apiKey`
      (JWT) próprio, escopo ADMIN. Ver `comercial/config-links-goalfy.md`
      neste repo para o formato esperado e como os scripts usam isso.
- [ ] **Nunca commitar esse link em nenhum repositório**, nem privado.

## 6. Upstash Redis (opcional, mas recomendado)

- [ ] Criar conta própria (gratuita) em [upstash.com](https://upstash.com) →
      Redis → novo database → aba REST API → copiar os dois valores.
      Sem isso, a aba "Análise Comercial" do dashboard fica lenta toda vez
      que o serviço Render "acorda" depois de ficar parado (plano free tem
      disco efêmero).

## 7. Google Drive — pasta de criativos

- [ ] Pedir acesso à pasta `Hapo - Handoff Jian/Criativos e Videos` no
      Google Drive do Jian (ele precisa compartilhar essa pasta
      especificamente com o e-mail da próxima pessoa).

## 8. Conta do ChatGPT (para o pipeline de artes)

O `ad-art-chatgpt-pipeline` depende de gerar a cena base num chat do ChatGPT
web com geração de imagem (GPT-4o/image) — **não** usa a API paga da OpenAI.

- [ ] A próxima pessoa precisa da própria conta ChatGPT com acesso a geração
      de imagem (plano pago da OpenAI, não é algo que se "transfere" — é só
      assinar).

## 9. Ambiente Claude Code / skills

- [ ] As skills (`ad-art-brief`, `ad-creative-copy`, `meta-ads-hapo`) estão
      neste repo em `skills/` — a próxima pessoa precisa copiá-las para a
      pasta local de skills do seu próprio Claude Code
      (`~/.claude/skills/<nome-da-skill>/`) ou perguntar como isso está
      configurado no ambiente de time, se houver um.
- [ ] O `contas.yaml` da skill `meta-ads-hapo` neste repo já vem filtrado só
      com as marcas do Grupo Hapo (Goalfy, Hapo Educação, Hapo Marketing) —
      se a próxima pessoa também assumir outras contas da agência, vai
      precisar do `contas.yaml` completo, que não está aqui.

---

## Nota sobre revogação

Qualquer credencial acima que **não** dê para transferir de forma limpa
(ex.: token de sistema vinculado à conta pessoal do Jian no Meta Business
Manager) deve ser **revogada** depois que a nova credencial estiver
funcionando — não deixar as duas ativas indefinidamente.
