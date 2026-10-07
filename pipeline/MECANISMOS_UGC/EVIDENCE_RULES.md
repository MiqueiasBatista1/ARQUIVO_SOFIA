# Regras de evidência e validação

## Princípio

Separe o que a peça mostra, a interpretação estrutural, a hipótese psicológica ou de performance e o resultado medido. Evidência de que uma lógica foi executada não prova que o público respondeu a ela nem que causou um resultado.

Mantenha também separados os níveis taxonômicos definidos em [CLASSIFICACAO.md](CLASSIFICACAO.md): psicologia, mecanismo, estrutura, formato, contexto e objetivo. Um formato ou recurso presente não é, por si, evidência de mecanismo completo ou de eficácia.

## Quatro níveis de afirmação

### EVIDÊNCIA

Descrição verificável do que a fonte mostra ou diz. Registre origem e, quando possível, localizador temporal.

**Exemplo:** “O vídeo mostra aplicação do produto por 5 segundos.”

### INTERPRETAÇÃO

Leitura estrutural do material observável. Identifique a estrutura, o formato e o mecanismo provável sem atribuir intenção não confirmada.

**Exemplo:** “A aplicação mostrada é compatível com uma demonstração do uso.”

### HIPÓTESE

Proposição não validada sobre psicologia ou objetivo: o que o mecanismo pode favorecer e qual dado seria necessário para avaliar isso.

**Exemplo:** “A demonstração pode apoiar confiança e reduzir incerteza sobre o modo de uso.”

### RESULTADO VALIDADO

Resultado observado em testes próprios ou dados apropriados, com contexto suficiente: conteúdo e mecanismo usados, público ou amostra, plataforma, período, métrica, comparação/referência e limitações. Resultado observado não prova causalidade automaticamente; outras diferenças podem explicar o desempenho.

**Exemplo:** “Nos testes próprios descritos em [referência], a variante que usou demonstração apresentou [métrica] frente a [comparação], no período e público indicados.”

## Registro prático

```text
EVIDÊNCIA:
Fonte/localizador: [referência, arquivo ou teste; timestamp se disponível]
Descrição observável:

INTERPRETAÇÃO:
Mecanismo provável, estrutura e formato observados:

HIPÓTESE:
Psicologia/objetivo possível e dado necessário para avaliar:

RESULTADO VALIDADO:
Teste, comparação, contexto, métrica e limitações; ou “ainda não disponível”:
```

Não invente timestamps, métricas, reações do público, intenção do criador ou contexto ausente. Uma análise de referência pode sustentar que uma estrutura está presente; não classifique sua eficácia com base apenas nisso.

## Status do catálogo

- 🟢 **TESTADO** — há resultado próprio registrado, contextualizado e pertinente ao mecanismo. Declare escopo, métrica e condições; não generalize além dos dados. “Testado” não significa eficácia universal nem garantia.
- 🟡 **EXPERIMENTAL** — mecanismo conceitual, hipótese, observação estrutural sem validação de desempenho suficiente ou evidência inconclusiva. É o status padrão.
- 🔴 **DESCARTADO** — decisão documentada de não usar/priorizar o mecanismo em um escopo, com razão e contexto. Não significa que falhará em todos os casos.

Altere status com justificativa, evidência pertinente, escopo e versão/data. A validação deve corresponder ao mecanismo, não apenas ao formato, tema, hook ou recurso estrutural usado. Resultados inconclusivos não são validação positiva.

## Linguagem

Não escreva como fato:

- “esse mecanismo sempre funciona”;
- “garante viralidade”;
- “garante vendas”;
- “ativa determinada substância cerebral”;
- “o algoritmo entrega mais”.

Prefira “pode favorecer”, “é compatível com”, “hipótese a validar” e “nos testes observados, sob estas condições”. Não atribua estado interno, efeito neurobiológico, causalidade ou decisão do algoritmo sem evidência apropriada. Mantenha limitações e explicações alternativas junto às conclusões.
