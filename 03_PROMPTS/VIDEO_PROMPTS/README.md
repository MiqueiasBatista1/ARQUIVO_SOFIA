# VIDEO_PROMPTS

Estruturas de composição/serialização audiovisual. O fluxo oficial está em [`PROMPT_ASSEMBLY.md`](../PROMPT_ASSEMBLY.md). Escolha aqui uma base compatível **depois** de decidir o arco em `UGC_TEMPLATES/`, a abertura/progressão/CTA em `HOOKS_RETENTION_CTA/`, os componentes nos `MODULE_CARDS/` e a execução em `VIDEO_DIRECTION/` e `CAMERA_AND_PHOTOGRAPHY/`.

Os nomes e aliases autorizados estão em [`GLOSSARIO_CANONICO.md`](../GLOSSARIO_CANONICO.md). `UGC_FORMAT` classifica a peça e `UGC_TEMPLATE` aponta para seu arco; nenhum substitui esta etapa de serialização. `BENEFIT` e `VERIFIED_BENEFIT` também são distintos: use o segundo quando a frase representar um benefício confirmado.

Transfira para a base as decisões já tomadas; para cenas com vários momentos, serializar significa indicar a ordem e duração aproximada de cada plano. Estas bases não escolhem nem substituem o template narrativo, análise de referência ou direção. Remova instruções genéricas que dupliquem ou contrariem decisões anteriores. Acrescente `[DURATION]`, `[LOCATION]`, `[CAMERA]`, `[LIGHTING]`, `[MOOD]` e, quando houver fala, `[DIALOGUE]`, somente quando aplicáveis. Não solicite declarações pessoais fictícias como se fossem experiências reais.

## Proveniência no prompt composto

Receba somente decisões criativas elegíveis e fatos qualificados das camadas anteriores. Não serialize registros brutos de observação, interpretação ou hipótese como fatos/instruções e não invente `CLAIM`, `PROOF`, `DATA_SOURCE`, `SOURCE_QUALIFICATION` ou `TESTIMONIAL`. Claim observado numa referência não é confirmação. `BENEFIT` permanece ideia editorial; `VERIFIED_BENEFIT` exige suporte apropriado e qualificado no escopo usado. Preserve os vínculos de proveniência junto à composição para a adaptação, sem necessariamente expor metadados como texto do prompt. Regras completas em [`GLOSSARIO_CANONICO.md`](../GLOSSARIO_CANONICO.md).

### UGC
```text
Vídeo UGC vertical de [DURATION] sobre [PRODUCT]. Em [LOCATION], [SUBJECT] apresenta [HOOK], mostra [ACTION] em formato de demonstração e encerra com [CTA]. Linguagem direta e ritmo natural. Fala: [DIALOGUE]. Câmera [CAMERA], luz [LIGHTING].
```

### Product demonstration
```text
Vídeo vertical de demonstração de [PRODUCT], duração [DURATION]. Mostre em ordem: produto e contexto; [DEMONSTRATION_STEP_1]; [DEMONSTRATION_STEP_2]; detalhe observável [PRODUCT_DETAIL]. Use apenas ações compatíveis com o produto e informações confirmadas. Câmera [CAMERA], fala/áudio [DIALOGUE].
```

### Talking to camera
```text
Plano de [DURATION] com [SUBJECT] falando diretamente à câmera sobre [TOPIC]. Abertura: [HOOK]. Mensagem principal: [KEY_POINT]. Encerramento: [CTA]. Entrega conversacional, pausas naturais e contato visual coerente. Câmera [CAMERA], áudio limpo, fala: [DIALOGUE].
```

### Unboxing
```text
Vídeo vertical de unboxing de [PRODUCT], duração [DURATION]. Registre abertura da embalagem, itens realmente incluídos e primeira inspeção, na sequência. Mantenha mãos, objetos e embalagem consistentes entre planos; não adicione itens que não constem em [PACKAGE_CONTENTS]. Narração opcional: [DIALOGUE].
```

### Review
```text
Review em vídeo de [PRODUCT] com duração [DURATION]. Organize em: contexto de uso [CONTEXT], observações verificáveis [OBSERVATIONS], limitações relevantes [LIMITATIONS] e conclusão [CONCLUSION]. Apresente opinião como opinião e alegações como fatos somente quando confirmadas. Fala: [DIALOGUE].
```

### Before/after
```text
Vídeo comparativo de [DURATION] entre [BEFORE_STATE] e [AFTER_STATE], sob condições comparáveis de enquadramento, iluminação e intervalo [TIMEFRAME]. Identifique o que está sendo mostrado e não atribua causalidade ou resultado ao [PRODUCT] sem evidência apropriada. Transição simples, texto/áudio [DIALOGUE].
```

### Tutorial
```text
Tutorial vertical de [DURATION] para [TASK] usando [PRODUCT]. Mostre materiais necessários, etapas numeradas [STEPS] e resultado esperado realista. Mantenha cada ação visível antes de avançar. Instrução falada: [DIALOGUE].
```

### Get ready with me
```text
Vídeo GRWM de [DURATION] acompanhando [ROUTINE] para [OCCASION]. Apresente etapas em ordem, integre [PRODUCT] no ponto apropriado e inclua comentários [DIALOGUE]. Cortes suaves, ritmo [PACE], clima [MOOD].
```

### Lifestyle
```text
Vídeo lifestyle vertical de [DURATION] sobre [ACTIVITY] em [LOCATION]. Construa uma sequência de momentos observáveis que inclua [PRODUCT] de modo orgânico, sem interromper a ação. Câmera [CAMERA], luz [LIGHTING], áudio ambiente [AUDIO], clima [MOOD].
```

### Product recommendation
```text
Recomendação em vídeo de [DURATION] para [AUDIENCE] considerando [NEED]. Apresente [PRODUCT] e explique o benefício confirmado [VERIFIED_BENEFIT]. Contextualize a recomendação para esse público e necessidade sem afirmar adequação universal; apresente separadamente as limitações pertinentes [LIMITATIONS]. Feche com [CTA]. Fala: [DIALOGUE].
```

### Testimonial
```text
Vídeo testimonial de [DURATION] baseado exclusivamente no relato real aprovado [TESTIMONIAL]. Preserve o sentido da fala, identifique contexto e período de uso quando informados e não acrescente resultados, endossos ou detalhes pessoais. Apresentação [MOOD], fala [DIALOGUE].
```

### Storytelling
```text
Vídeo vertical de [DURATION] com arco breve: contexto [CONTEXT], necessidade ou desafio [PROBLEM], decisão ou descoberta [DISCOVERY], experiência observada [EXPERIENCE] e fechamento [ENDING]. Integre [PRODUCT] apenas onde fizer sentido. Não invente testemunho. Narração/fala [DIALOGUE], ritmo [PACE].
```
