# UGC_FORMAT

**Use quando:** escolher a convenção de conteúdo que organiza a peça, como demonstração, unboxing, tutorial ou review.

`UGC_FORMAT` é a classe editorial. `UGC_TEMPLATE` identifica a ficha narrativa selecionada em `UGC_TEMPLATES/VIDEO_TEMPLATES/`; os campos são relacionados, não aliases. Use a distinção definida em [`GLOSSARIO_CANONICO.md`](../GLOSSARIO_CANONICO.md).

**Combine com:** `OBJECTIVE` para decidir a função da peça; `SCRIPT` para ordenar as etapas; `CAMERA`, `ACTION` e `DIALOGUE` para executá-las. Consulte `VIDEO_PROMPTS/` para bases de cada formato.

**Bloco reutilizável:**

```text
Formato UGC: [UGC_FORMAT]. Siga as convenções desse formato e mantenha a apresentação adequada ao objetivo [OBJECTIVE].
Template UGC selecionado: [UGC_TEMPLATE].
```

**Exemplo preenchido:** `UGC_FORMAT = demonstração curta de produto`.
