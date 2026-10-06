# Orquestração de HOOK, RETENTION e CTA

Use esta camada depois de escolher o formato narrativo em `UGC_TEMPLATES/VIDEO_TEMPLATES/`. Ela não substitui o roteiro: conecta abertura, desenvolvimento e próxima ação.

Consulte [`GLOSSARIO_CANONICO.md`](../GLOSSARIO_CANONICO.md) para os significados. `RETENTION` é uma lista opcional e ordenada de mecanismos/etapas selecionados; `OBSERVED_RETENTION` pertence à análise de referência. `HOOK` é conteúdo, enquanto o nome da ficha indica o mecanismo. `CTA` é a ação final; `DESTINATION` é o local onde ela será realizada.

Sua posição no fluxo completo é definida por [`PROMPT_ASSEMBLY.md`](../PROMPT_ASSEMBLY.md): após o template UGC e antes de estruturar/preencher os componentes nos `MODULE_CARDS/`. A tabela desta página é um checklist de decisões editoriais, não a ordem completa de montagem nem um bloco adicional para duplicar no prompt final.

## Proveniência das escolhas

Esta camada recebe o arco UGC, o objetivo da nova peça, padrões abstratos já remodelados e fatos de produto elegíveis. Não use hook, CTA, fala, resultado ou claim observados na referência como conteúdo novo por padrão. Uma observação pode inspirar uma estrutura somente após a remodelagem editorial, sem carregar sua alegação como fato.

Promessas em `HOOK` devem corresponder ao que a peça pode mostrar ou sustentar. Claims sobre produto/benefício seguem a fonte e qualificação de `PROOF`; uma fonte insuficiente, indireta, não verificada ou inadequada não autoriza apresentá-los como fatos. `BENEFIT` não é `VERIFIED_BENEFIT`. A proveniência acompanha as decisões até os cards e serializadores conforme [`GLOSSARIO_CANONICO.md`](../GLOSSARIO_CANONICO.md).

## Composição

```text
[UGC_TEMPLATE]
+ [HOOK]
+ [RETENTION]
+ [PRODUCT]
+ [ACTION]
+ [CTA]
```

1. **HOOK:** apresenta uma pergunta, situação ou ação inicial.
2. **UGC_TEMPLATE:** define o arco do vídeo e o tipo de conteúdo.
3. **RETENTION:** organiza a entrega de informação ao longo desse arco.
4. **PRODUCT e ACTION:** dão contexto e material observável às etapas do template.
5. **CTA:** encerra com uma única próxima ação coerente.

O template UGC continua sendo a fonte da estrutura narrativa. O hook e a retenção são encaixados em suas etapas; não gere um segundo roteiro copiando o template.

## Como combinar sem repetir

- Escolha **um hook principal**. Se o template já começa com uma pergunta ou abertura visual, use-a como hook em vez de acrescentar outra.
- Associe cada mecanismo de retenção a uma etapa existente do roteiro. Evite inserir ganchos novos que interrompam a mesma informação repetidamente.
- Escreva `[ACTION]` como ação observável. Não replique nela o texto falado de `[SCRIPT]` ou `[DIALOGUE]`.
- Use **um CTA principal**. Um CTA secundário é opcional, deve ser breve e não pode competir com o objetivo.
- Use `[PRODUCT]` apenas com dados confirmados e só repita seu nome quando melhorar a compreensão.

## Regras de coerência

- O desenvolvimento deve responder à pergunta ou cumprir a expectativa aberta pelo hook.
- A promessa de um hook deve se referir ao que o vídeo realmente mostrará, não a resultado presumido do produto.
- Toda afirmação de produto, benefício, comparação, avaliação ou resultado precisa de informação aprovada e evidência adequada ao contexto.
- Ajuste intensidade e quantidade de mecanismos de retenção ao mood e ao formato: um tutorial calmo pode progredir por etapas claras; uma peça dinâmica não precisa de interrupções constantes.
- Prefira revelar informação útil, demonstrar uma etapa relevante ou concluir uma ideia. Não force suspense sem payoff.
- Mudanças de plano devem ser motivadas por mudança de informação ou ação. A direção de câmera pertence a `CAMERA_AND_PHOTOGRAPHY/`; gestos e atuação pertencem a `VIDEO_DIRECTION/`.
- Não inclua instruções de rosto, corpo, cabelo, pele, aparência ou identidade nesta camada.

## Campos para montagem

```text
HOOK: [HOOK]
RETENTION: [RETENTION]
UGC_TEMPLATE: [UGC_TEMPLATE]
PRODUCT: [PRODUCT]
ACTION: [ACTION]
CTA: [CTA]
```

Placeholders são em inglês, ASCII, maiúsculas e `SNAKE_CASE`. Remova campos vazios antes de adaptar a composição ao modelo escolhido. Parâmetros e capacidades do modelo são tratados em `MODEL_ADAPTATION` e `MODEL_ADAPTERS/`, sem presumir suporte.
