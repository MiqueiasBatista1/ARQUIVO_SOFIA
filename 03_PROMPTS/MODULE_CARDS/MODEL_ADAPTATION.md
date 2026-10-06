# MODEL_ADAPTATION

**Use quando:** traduzir a montagem genérica para a entrada e os controles de um modelo específico. Registre o modelo e a versão realmente selecionados.

`MODEL_ADAPTATION` é a transformação da composição. `MODEL_PROFILE` são os dados verificados do modelo e configuração; não são intercambiáveis. `PROMPT_TRANSFORM` é aceito como alias legado apenas para a lista de transformações em `MODEL_ADAPTERS/`. Consulte [`GLOSSARIO_CANONICO.md`](../GLOSSARIO_CANONICO.md).

**Combine com:** todos os módulos já preenchidos e `MODEL_ADAPTERS/README.md`. Esta ficha adapta a forma de entrada; não substitui o conteúdo nem adiciona capacidades presumidas.

**Bloco reutilizável:**

```text
Perfil do modelo: [MODEL_PROFILE]. Adaptação: [MODEL_ADAPTATION]. Separe texto, referências e parâmetros conforme os campos disponíveis e verificados; mantenha todas as instruções essenciais.
```

**Compatibilidade:** fichas antigas podem registrar `[MODEL_NAME]` e `[MODEL_VERSION]` separadamente como dados do `MODEL_PROFILE`. `PROMPT_TRANSFORM` é nome legado apenas para a transformação indicada por `[MODEL_ADAPTATION]`.

**Exemplo preenchido:** `MODEL_ADAPTATION = enviar o prompt como texto e configurar a duração no campo próprio, se disponível; confirmar a interface antes de gerar`.
