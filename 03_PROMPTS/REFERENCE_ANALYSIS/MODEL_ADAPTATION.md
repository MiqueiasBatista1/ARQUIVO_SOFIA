# Adaptação da análise para modelos

Esta camada separa a análise editorial dos controles de qualquer gerador. Veo/Flow, Seedance e outros modelos não têm capacidades presumidas aqui.

Esta ficha registra condições para adaptar/analisar a entrada da referência; ela não é o `MODEL_PROFILE` nem o `MODEL_ADAPTATION` da montagem de geração. `INPUT_MODALITY` e `INPUT_MODE` continuam distintos enquanto os schemas tiverem escopos diferentes. Veja [`GLOSSARIO_CANONICO.md`](../GLOSSARIO_CANONICO.md).

## Ficha de adaptação

```yaml
model_name: "[MODEL_NAME]"
model_version: "[MODEL_VERSION]"
verified_at: "[VERIFIED_AT]"
input_modality: "[INPUT_MODALITY]"
output_task: "[OUTPUT_TASK]"
analysis_input: "[ANALYSIS_INPUT]"
prompt_structure: "[PROMPT_STRUCTURE]"
parameters_verified: "[PARAMETERS_VERIFIED]"
limitations: "[KNOWN_LIMITATIONS]"
```

## Regras

1. Analise somente material fornecido e acessível no fluxo autorizado; não presuma que o modelo consiga abrir links, assistir a vídeo ou interpretar áudio.
2. Verifique modelo, versão, modalidade de entrada e campos disponíveis na interface usada. Registre `unknown` quando não confirmado.
3. Mantenha observações, interpretações e hipóteses como campos separados, mesmo que a interface peça uma única instrução textual.
4. Para geração, envie apenas o novo conceito remodelado e seus módulos selecionados; não use a referência como pedido de cópia.
5. Separe texto de parâmetros estruturados e referências visuais quando a interface oferecer campos específicos. Não presuma suporte a imagem de referência, timestamps, duração, áudio ou negative prompt.
6. Preserve incertezas e lacunas. Um modelo não deve completar falas, métricas, características de produto ou eventos ausentes como se fossem fatos.

A adaptação altera o formato de entrada, não o status de evidência nem a autoria do conceito.
