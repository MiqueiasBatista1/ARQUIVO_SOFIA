# Template de análise de referência

Use uma cópia deste formulário por referência. Preencha apenas o que for observável ou sustentado por evidência identificada. Para os campos 2–15, descreva o conteúdo percebido; para 16–20, classifique explicitamente interpretação, abstração, remodelagem ou hipótese conforme `EVIDENCE_RULES.md`.

## Identificação e intenção aparente

1. **CONTEXTO_DA_REFERENCIA** — `[REFERENCE_CONTEXT]`  
   Origem informada, identificador, formato/duração verificáveis, data de acesso e limites do material analisado. Não infira alcance ou desempenho.

2. **OBJETIVO_OBSERVADO** — `[OBSERVED_OBJECTIVE]`  
   Objetivo declarado no material ou objetivo comunicativo aparente. Rotule como observado se declarado; caso inferido, marque como interpretação e registre evidência.

## Conteúdo e progressão observados

3. **HOOK** — `[OBSERVED_HOOK]`  
   Abertura verbal ou visual, com timestamp ou indicação de trecho. Registre a fala literalmente apenas quando necessário e permitido; caso contrário, resuma.

4. **ESTRUTURA_DE_RETENCAO** — `[OBSERVED_RETENTION]`  
   Como a informação progride, quais perguntas são abertas e onde são respondidas. Não atribua intenção como fato.

5. **ROTEIRO** — `[OBSERVED_SCRIPT]`  
   Sequência concisa de beats narrativos, em ordem e com referências temporais quando disponíveis.

6. **DIALOGO** — `[OBSERVED_DIALOGUE]`  
   Resumo ou transcrição de falas efetivamente audíveis; marque trechos inaudíveis como desconhecidos.

7. **ACAO** — `[OBSERVED_ACTION]`  
   Ações visíveis que avançam ou ilustram a narrativa, sem inferir estados internos.

8. **DEMONSTRACAO_DO_PRODUTO** — `[OBSERVED_PRODUCT_DEMO]`  
   O que é mostrado sobre o produto e em que ordem. Separe demonstração observável de alegações faladas.

## Linguagem audiovisual observada

9. **CAMERA** — `[OBSERVED_CAMERA]`  
   Características aparentes de captura que possam ser percebidas; não alegue equipamento ou lente específicos sem evidência.

10. **ENQUADRAMENTO** — `[OBSERVED_FRAMING]`  
    Distância e organização do quadro, com mudança de trecho se houver.

11. **MOVIMENTO** — `[OBSERVED_MOVEMENT]`  
    Movimento aparente de câmera ou assunto. Não prescreva movimento futuro nesta análise.

12. **ILUMINACAO** — `[OBSERVED_LIGHTING]`  
    Qualidade, direção e variação de luz perceptíveis; origem só quando evidente.

13. **AMBIENTE** — `[OBSERVED_ENVIRONMENT]`  
    Contexto visual/sonoro relevante, sem catalogar aparência ou identidade de pessoas.

14. **RITMO** — `[OBSERVED_PACING]`  
    Densidade e espaçamento das falas, ações e transições. Registre contagens apenas se medidas no material.

15. **CTA** — `[OBSERVED_CTA]`  
    Próxima ação solicitada, se houver; diferencie fala, texto na tela e elemento visual.

## Abstração e próximos passos

16. **MECANISMO_PERSUASIVO** — `[INTERPRETED_MECHANISM]`  
    Leitura possível de como a estrutura pode influenciar compreensão/atenção. Inclua evidência de apoio e grau de confiança; não declare eficácia comprovada.

17. **PADROES_REUTILIZAVEIS** — `[REUSABLE_PATTERNS]`  
    Regras abstratas transferíveis, sem copiar frases, sequência distintiva, identidade visual ou ativos do original.

18. **ELEMENTOS_QUE_NAO_DEVEM_SER_COPIADOS** — `[NON_COPYABLE_ELEMENTS]`  
    Elementos expressivos, de marca, autorais, pessoais ou contextuais que devem ser substituídos; inclua fala literal, identidade do creator, música e grafismos próprios quando pertinentes.

19. **OPORTUNIDADES_DE_REMODELAGEM** — `[REMODELING_OPPORTUNITIES]`  
    Formas de reconstruir o mecanismo com novo contexto, linguagem, ação, evidência e execução.

20. **HIPOTESES_A_TESTAR** — `[HYPOTHESES_TO_TEST]`  
    Hipótese falsificável, variável a alterar, resultado observável e critério de comparação. Não antecipe resultados.

## Registro por campo

Use este bloco para cada achado quando for necessário manter rastreabilidade:

```text
CAMPO: [FIELD_NAME]
CLASSIFICACAO: [EVIDENCE_CLASS]
CONTEUDO: [FIELD_CONTENT]
TRECHO_OU_TIMESTAMP: [EVIDENCE_LOCATOR]
FONTE: [EVIDENCE_SOURCE]
CONFIANCA: [CONFIDENCE_LEVEL]
LACUNAS: [UNKNOWN_OR_MISSING]
source_type: [SOURCE_TYPE]
source_id: [SOURCE_ID]
origin_stage: [ORIGIN_STAGE]
evidence_status: [EVIDENCE_STATUS]
allowed_consumers: [ALLOWED_CONSUMERS]
generation_input: [GENERATION_INPUT]
```

Em `CLASSIFICACAO`, escreva um rótulo em texto simples: `OBSERVADO`, `INTERPRETADO`, `HIPOTESE`, `REUTILIZAVEL` ou `NAO_COPIAR`. Esses rótulos são valores, não placeholders. Não use um rótulo de observação para uma inferência.

Os metadados em minúsculas seguem o contrato de proveniência de [`GLOSSARIO_CANONICO.md`](../GLOSSARIO_CANONICO.md). `evidence_status` repete a classificação existente (`CLASSIFICACAO`/`EVIDENCE_CLASS`) para facilitar a passagem entre camadas; não é uma classificação nova. `source_id` só recebe identificador real associado a `REFERENCE_CONTEXT`; se ausente, registre a lacuna em `UNKNOWN_OR_MISSING`. `confidence_level` aplica-se a interpretações, não valida claims. `allowed_consumers` e `generation_input` devem respeitar a matriz do glossário. Para referência bruta, geração é `no`; somente padrões abstratos remodelados podem inspirar uma decisão editorial nova, sem transferir a evidência original como fato.
