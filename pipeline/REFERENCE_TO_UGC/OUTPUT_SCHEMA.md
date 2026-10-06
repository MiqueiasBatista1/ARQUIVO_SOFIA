# Output schema — conceito UGC remodelado

O contrato machine-readable está em schemas/ugc_output.schema.json; validação Python em schemas/contracts.py. Todos os campos são obrigatórios como chaves. Campos sem fato aprovado podem ser null somente onde o schema permite.

| Campo | Conteúdo esperado |
| --- | --- |
| reference_id | Identificador da análise de origem |
| content_type, ugc_template | Tipo de conteúdo e template UGC selecionado |
| hook, problem, mechanism | Abertura, contexto do novo conceito e mecanismo abstrato |
| product, core_benefit | Produto/benefício aprovados; null se desconhecidos |
| scene_structure | Beats originais com finalidade e ação |
| dialogue, actions | Fala aprovada e ações observáveis originais |
| camera, lighting, location, emotion | Direção da nova peça, não cópia da referência |
| retention_devices, cta, duration_seconds | Progressão, chamada e duração estimada |
| adaptation_notes | Observações para futuro modelo/ferramenta |
| originality_notes | Mudanças feitas e elementos da referência descartados |

A validação rejeita chaves ausentes/desconhecidas, textos obrigatórios vazios, cenas incompletas e duração inválida. Valida forma, não veracidade factual nem originalidade semântica.
