# REFERENCE_TO_UGC

Camada de ponte entre ingestão, análise estruturada e um novo conceito UGC. Não copia nem gera conteúdo automaticamente. Esta entrega inclui contratos, validação e um transformador determinístico que liga um rascunho original à referência analisada.

## Estrutura

- schemas/: contrato da análise recebida e schema do conceito UGC completo.
- adapters/video_ingestion.py: bridge de IngestionOutput para uma semente compatível com 03_PROMPTS/REFERENCE_ANALYSIS.
- adapters/interfaces.py: porta futura para serviço de rascunho; nenhuma IA/API está conectada.
- schemas/contracts.py: valida a análise e a saída, preservando reference_id.
- templates/ugc_concept.template.json: formulário vazio de conceito.
- tests/: testes unitários do contrato e transformação.

## Uso

1. Receba IngestionOutput e converta em evidências candidatas.
2. Revise e complete a ficha conforme 03_PROMPTS/REFERENCE_ANALYSIS/ANALYSIS_TEMPLATE.md e EVIDENCE_RULES.md.
3. Forneça a análise estruturada e um rascunho UGC original a transform_reference_to_ugc().
4. A função preserva a referência, valida campos obrigatórios e rejeita análise sem padrões e oportunidades de remodelagem.
5. Encaminhe campos validados para UGC_TEMPLATES, HOOKS_RETENTION_CTA e MODULE_CARDS/ORCHESTRATION.md.

O núcleo não inventa hook, benefício, diálogo ou ação. O rascunho deve ser escrito por uma pessoa ou futuro adapter, com dados aprovados. product e core_benefit aceitam null quando não houver brief factual; benefício não pode ser inferido da referência. Traduções derivadas permanecem separadas das observações e da transcrição original.
