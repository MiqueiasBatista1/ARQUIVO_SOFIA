# MODEL_ADAPTERS

Fichas de tradução entre o prompt modular e a interface de cada modelo. Preencha somente após verificar a versão e os controles disponíveis na ferramenta. Não inclua prompts-base duplicados aqui; registre diferenças de entrada e parâmetros.

Consulte [`GLOSSARIO_CANONICO.md`](../GLOSSARIO_CANONICO.md): `MODEL_PROFILE` contém dados verificados da configuração; `MODEL_ADAPTATION` registra a transformação aplicada ao prompt. O perfil não substitui a adaptação. A ficha abaixo registra ambos sem presumir capacidades.

## Ficha reutilizável

Copie este formulário para documentar uma configuração de modelo. Mantenha as fichas específicas dentro desta pasta.

```yaml
model_profile:
  model_name: "[MODEL_NAME]"
  model_version: "[MODEL_VERSION]"
  verified_at: "[YYYY-MM-DD]"
  task: "[TASK_TYPE]"
  input_mode: "[INPUT_MODE]"
  parameters:
    aspect_ratio: "[ASPECT_RATIO]"
    duration: "[DURATION_PARAMETER]"
    resolution: "[RESOLUTION]"
    audio: "[AUDIO_SUPPORT]"
    negative_prompt: "[NEGATIVE_PROMPT_SUPPORT]"
    other: "[OTHER_VERIFIED_PARAMETERS]"
  capabilities_verified:
    - "[VERIFIED_CAPABILITY]"
  known_limits:
    - "[KNOWN_LIMIT]"
  notes: "[NOTES]"
model_adaptation:
  - "[MODEL_ADAPTATION]"
```

Compatibilidade: fichas existentes com os campos antigos na raiz continuam legíveis como registro legado de `MODEL_PROFILE`. `prompt_transform` é alias legado somente para a lista de transformações agora chamada `model_adaptation`; não é alias do perfil inteiro. Migre uma ficha apenas quando ela for revisada, sem inventar campos ou capacidades.

Preencha `TASK_TYPE` e `INPUT_MODE` com texto simples, por exemplo `video` ou `text_to_video`; esses valores são conteúdo descritivo do perfil, não placeholders aninhados. `INPUT_MODALITY` em `REFERENCE_ANALYSIS/MODEL_ADAPTATION.md` descreve a modalidade de entrada da análise e não é tratado aqui como alias automático de `INPUT_MODE`.

Use `unknown` quando a informação ainda não foi verificada. Use `unsupported` apenas quando a versão/configuração tiver sido verificada e não oferecer o recurso. Registre o que a interface realmente permite; nomes de parâmetros não são presumidos pela biblioteca.

## Processo de adaptação

1. Selecione uma base e os módulos necessários em `PROMPT_ASSEMBLY.md`; use os nomes do glossário canônico.
2. Confirme modelo, versão, tarefa e formato de entrada pretendidos.
3. Separe prompt textual de parâmetros estruturados e mídias de referência.
4. Adapte ordem, granularidade temporal e campos ao que a versão aceita; não remova restrições essenciais de factualidade ou identidade.
5. Registre capacidades, limitações e transformação nesta ficha ou em uma cópia preenchida.
6. Remova placeholders vazios e confira se a adaptação não duplicou instruções.

## Compatibilidade

Esta pasta é deliberadamente neutra em relação a Veo, Flow, Seedance e outros modelos. Não há fichas específicas enquanto versões e interfaces não forem verificadas. Atualize a ficha quando a versão ou o fluxo de entrada mudar.

## Preservação de proveniência

O adaptador recebe uma composição elegível e preserva o vínculo de proveniência de cada claim, `BENEFIT`/`VERIFIED_BENEFIT`, `PROOF`, `DATA_SOURCE`, `SOURCE_QUALIFICATION` e `TESTIMONIAL` aplicável. Pode reorganizar ou serializar a representação para capacidades verificadas do modelo; não pode mudar o conteúdo, escopo, fonte, `evidence_status`, `confidence_level`, qualificação ou autorização, nem promover hipótese/claim não verificado a fato.

Não sintetize fonte, suporte ou testemunho quando a interface não tiver campo próprio. Os metadados podem acompanhar a composição como registro auxiliar sem serem inseridos no texto destinado ao modelo. `MODEL_PROFILE` descreve capacidades de modelo verificadas e não é proveniência de uma alegação de produto. Consulte [`GLOSSARIO_CANONICO.md`](../GLOSSARIO_CANONICO.md) para elegibilidade e dependências.
