# UGC_TEMPLATES

Templates narrativos reutilizáveis para conteúdo comercial UGC/TikTok Shop. Esta pasta reúne duas camadas: componentes de roteiro neste README e estruturas por formato em `VIDEO_TEMPLATES/`. Os blocos são independentes de modelo e devem receber fatos aprovados sobre cada produto.

Use os nomes e significados de [`GLOSSARIO_CANONICO.md`](../GLOSSARIO_CANONICO.md). `UGC_FORMAT` é a classe editorial; `UGC_TEMPLATE` identifica a ficha narrativa escolhida. São conceitos distintos. Os 15 templates continuam autônomos: não há herança obrigatória e cada ficha mantém sua estrutura narrativa, restrições, exemplos e campos locais.

## Campos compartilhados e campos locais

As fichas referenciam os contratos globais; não herdam seus valores. `OBJECTIVE`, `PRODUCT`, `PRODUCT_CATEGORY`, `HOOK`, `SCRIPT`, `DIALOGUE`, `ACTION`, `LOCATION`, `CAMERA`, `LIGHTING`, `MOOD`, `DURATION` e `CTA` são nomes compartilhados definidos no glossário e preenchidos conforme o briefing e os módulos de montagem. `UGC_FORMAT` é informado pela seleção editorial; `UGC_TEMPLATE` é identificado pela ficha selecionada. Nenhum dos dois substitui o outro.

`STYLE` é uma escolha visual opcional, quando aplicável, e aponta para `STYLE_PRESETS/`; não é um campo local repetido em cada inventário. `RETENTION`, `BENEFIT`, `VERIFIED_BENEFIT` e `PROOF` continuam condicionais e seguem seus contratos globais quando o conteúdo exigir. `MODEL_ADAPTATION` pertence à etapa posterior de adaptação: não é campo nem módulo do template.

Em cada ficha, **Campos específicos desta ficha** lista somente placeholders locais que completam a narrativa daquele formato. A lista não repete campos compartilhados. **Módulos necessários** e **Módulos opcionais** indicam a aplicabilidade narrativa de cada módulo; não são sinônimos da lista de placeholders. Condições expressas no texto da própria ficha continuam valendo (por exemplo, fala, produto ou CTA opcionais) e devem ser respeitadas ao preencher.

Para compor a peça, use [`MODULE_CARDS/ORCHESTRATION.md`](../MODULE_CARDS/ORCHESTRATION.md) e [`PROMPT_ASSEMBLY.md`](../PROMPT_ASSEMBLY.md). Referenciar esses contratos evita duplicação; não cria dependência de herança nem remove a autonomia de leitura das fichas.

## Posição no fluxo oficial

Consulte [`PROMPT_ASSEMBLY.md`](../PROMPT_ASSEMBLY.md) para o fluxo completo. O template UGC é escolhido depois do briefing/análise de referência e antes de `HOOKS_RETENTION_CTA/`: ele define o formato e o arco narrativo. Hooks, retenção e CTA são encaixados nesse arco; os cards estruturam os componentes preenchidos; `VIDEO_PROMPTS/` serializa as decisões em uma instrução audiovisual. Não use um template UGC como substituto da análise da referência, da direção ou da composição final.

## Escolher um template

1. Defina o objetivo em `MODULE_CARDS/OBJECTIVE.md`.
2. Selecione em `VIDEO_TEMPLATES/` o `UGC_TEMPLATE` principal que melhor serve o `OBJECTIVE`; o próprio arquivo selecionado é a referência do template. Registre separadamente o `UGC_FORMAT` (classe editorial) quando necessário. Combine estruturas apenas quando a narrativa realmente exigir.
3. Preencha campos variáveis com dados confirmados. Remova campos não aplicáveis e placeholders ainda vazios.
4. Combine com `MODULE_CARDS/ORCHESTRATION.md` os campos compartilhados aplicáveis e os campos locais listados na ficha. Quando houver acabamento visual, selecione `STYLE` em `STYLE_PRESETS/`; `MODEL_ADAPTATION` é resolvido depois, na etapa de `MODEL_ADAPTERS/`.
5. Depois de resolver o conteúdo e os componentes, use `VIDEO_DIRECTION/` para execução e `CAMERA_AND_PHOTOGRAPHY/` para captura; `VIDEO_PROMPTS/` é a etapa posterior de composição/serialização, não uma segunda fonte de arco narrativo. Não copie as bibliotecas completas para o roteiro.

Cada ficha especifica seus módulos necessários e opcionais. “Necessário” significa necessário para montar aquele formato narrativo; ainda assim, retire qualquer campo que não se aplique à peça concreta.

## Proveniência e qualificação

Templates consomem decisões editoriais feitas para a nova peça e fatos de produto qualificados. Uma observação, interpretação ou hipótese de `REFERENCE_ANALYSIS/` não pode preencher automaticamente fala, ação, benefício ou afirmação factual. Padrões reutilizáveis só chegam ao template depois de abstraídos e remodelados; a referência permanece antecedente rastreável, não evidência do produto novo.

Mantenha `BENEFIT` como ideia editorial e use `VERIFIED_BENEFIT` apenas quando `PROOF` sustentar o claim no escopo registrado. Preserve `DATA_SOURCE` e `SOURCE_QUALIFICATION`; não complete fontes ou limites ausentes. Use `TESTIMONIAL` somente para relato real, autorizado e fiel ao contexto, sem generalização. Consulte a matriz de elegibilidade em [`GLOSSARIO_CANONICO.md`](../GLOSSARIO_CANONICO.md).

## Templates de vídeo

| Ficha | Uso principal |
| --- | --- |
| [DEMONSTRACAO](VIDEO_TEMPLATES/01_DEMONSTRACAO.md) | Mostrar etapas de uso observáveis |
| [PROBLEMA_SOLUCAO](VIDEO_TEMPLATES/02_PROBLEMA_SOLUCAO.md) | Contextualizar uma necessidade e apresentar o produto como opção |
| [PRIMEIRO_TESTE](VIDEO_TEMPLATES/03_PRIMEIRO_TESTE.md) | Registrar uma primeira experiência real, sem antecipar resultado |
| [ROTINA](VIDEO_TEMPLATES/04_ROTINA.md) | Integrar produto a uma rotina verdadeira ou encenada como demonstração |
| [GRWM](VIDEO_TEMPLATES/05_GRWM.md) | Organizar uma rotina de preparação por etapas |
| [UNBOXING](VIDEO_TEMPLATES/06_UNBOXING.md) | Mostrar embalagem e itens efetivamente incluídos |
| [REVIEW](VIDEO_TEMPLATES/07_REVIEW.md) | Apresentar avaliação baseada em experiência real e contextualizada |
| [COMPARACAO](VIDEO_TEMPLATES/08_COMPARACAO.md) | Comparar opções sob critérios e condições explícitos |
| [STORYTELLING](VIDEO_TEMPLATES/09_STORYTELLING.md) | Contar uma sequência narrativa com contexto e desfecho |
| [RESPOSTA_A_COMENTARIO](VIDEO_TEMPLATES/10_RESPOSTA_A_COMENTARIO.md) | Responder a comentário/pergunta real e autorizado |
| [SITUACAO_COTIDIANA](VIDEO_TEMPLATES/11_SITUACAO_COTIDIANA.md) | Apresentar produto dentro de um momento cotidiano |
| [TESTEMUNHO](VIDEO_TEMPLATES/12_TESTEMUNHO.md) | Adaptar um relato real autorizado sem alterar seu sentido |
| [CREATOR_ESPONTANEO](VIDEO_TEMPLATES/13_CREATOR_ESPONTANEO.md) | Usar tom conversacional e execução leve sem fingir experiência |
| [ANTES_DEPOIS](VIDEO_TEMPLATES/14_ANTES_DEPOIS.md) | Exibir estados comparáveis com contexto e sem causalidade indevida |
| [VENDA_DIRETA](VIDEO_TEMPLATES/15_VENDA_DIRETA.md) | Comunicar proposta, informações aprovadas e CTA comercial |

## Componentes reutilizáveis

Use estes blocos quando forem necessários, em vez de reescrever seus conceitos em cada template.

### Hooks

- **Pergunta:** `[HOOK]` pode começar com uma pergunta relevante para `[AUDIENCE]`.
- **Situação reconhecível:** introduza `[SITUATION]` sem exagerar o problema.
- **Observação:** abra com uma dúvida ou informação que será esclarecida no vídeo.
- **Demonstração primeiro:** comece mostrando `[ACTION]` com `[PRODUCT]` e contextualize em seguida.

### Problema ou necessidade

```text
Contextualize [PROBLEM] em uma frase concreta e relevante para [AUDIENCE]. Não intensifique a situação com medo ou urgência artificial.
```

### Descoberta do produto

```text
Apresente [PRODUCT] e explique o contexto [DISCOVERY_CONTEXT]. Não atribua experiência ou recomendação a uma pessoa se isso não for real e aprovado.
```

### Demonstração

```text
Mostre [ACTION] em etapas visíveis: [STEP_1], [STEP_2], [STEP_3]. Siga as instruções confirmadas de uso. Fala opcional: [DIALOGUE].
```

### Benefício e suporte

`[BENEFIT]` é uma ideia de benefício; `[VERIFIED_BENEFIT]` é um claim validado. São campos distintos. Não apresente `BENEFIT` como fato sem validação. Quando um claim precisar de suporte, use o objeto `[PROOF]` definido em `GLOSSARIO_CANONICO.md`, preenchendo somente elementos existentes. `DATA_SOURCE` identifica a fonte de dados; `SOURCE_QUALIFICATION` registra escopo/limites; `TESTIMONIAL` é apenas um relato real e autorizado e não equivale a `PROOF`.

### CTA

```text
[CTA]
```

O CTA pode convidar a consultar os detalhes do produto na página da loja. Preço, disponibilidade, condições e destino só entram quando confirmados para a publicação.

## Regras de preenchimento

- Placeholders seguem inglês, ASCII, maiúsculas e `SNAKE_CASE` entre colchetes. Não use alternativas dentro do mesmo token.
- `[SCRIPT]` representa a progressão narrativa; `[DIALOGUE]` contém as palavras faladas. Se forem iguais, mantenha a fala uma única vez.
- Hooks, CTAs e exemplos são estruturas de linguagem, não evidência de experiência ou eficácia.
- Reviews, primeiro teste, testemunhos e respostas devem partir de conteúdo real e autorizado. Demonstrações e comparações não devem sugerir resultado, superioridade ou causalidade sem suporte.
- Não invente características, benefícios, itens de embalagem, preços, escassez ou disponibilidade de `[PRODUCT]`.
- Adapte o prompt ao modelo apenas depois de selecionar sua interface e versão; consulte `MODEL_ADAPTERS/` sem presumir capacidades.
