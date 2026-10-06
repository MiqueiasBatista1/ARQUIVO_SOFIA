# Creative Score — heurística interna

## Finalidade e limites

Checklist comparativo para detectar lacunas antes de encaminhar um `CREATIVE_BLUEPRINT`. Não mede resposta de público e não prevê viralidade, alcance, retenção, conversão ou vendas. Escala e bandas são **EXPERIMENTAIS**; não foram calibradas contra métricas.

## Escala por dimensão

- **0 — ausente/contraditório:** elemento necessário ao objetivo não aparece ou trabalha contra ele.
- **1 — fraco:** aparece, mas está vago, tardio, desconectado ou difícil de compreender.
- **2 — razoável:** é compreensível e funcional, com lacuna ou dependência relevante.
- **3 — forte:** claro, específico ao objetivo, integrado e sustentado por informação disponível.

`ND` = evidência insuficiente para avaliar; não equivale a zero. `N/A` = dimensão não aplicável ao objetivo/formato. Não preencher lacunas por suposição.

## Dimensões (máximo 27)

| Dimensão | 0 | 1 | 2 | 3 |
| --- | --- | --- | --- | --- |
| ATTENTION | Nenhum elemento inicial relacionado ao objetivo. | Começo pouco conectado/vago. | Contexto reconhecível, com motivo de continuidade limitado. | Interesse relevante imediatamente legível, sem promessa indevida. |
| HOOK | Ausente ou contradiz o conteúdo. | Genérico/confuso. | Família e contexto claros, mas payoff/conexão parcial. | Hook claro e coerente com formato, objetivo e corpo. |
| CURIOSITY | Sem questão/interesse quando necessários. | Lacuna vaga ou sem resposta clara. | Pergunta/detalhe relevante com resposta prevista. | Curiosidade específica, legítima e paga pela peça. |
| RETENTION | Sem progressão; beats repetem ou não se conectam. | Progressão irregular ou dependente de suspense artificial. | Unidades claras com um ponto fraco. | Cada beat avança ação/compreensão e entrega resoluções coerentes. |
| VISUAL DYNAMICS | Imagem não ajuda a entender ação/foco. | Variação ou legibilidade insuficiente. | Captura legível, algumas escolhas de plano/ação pertinentes. | Mudanças visuais motivadas por informação e ação, legíveis ao formato. Não exige muitos cortes. |
| NATIVE FEEL | Forma interrompe ou contradiz objetivo/contexto. | Sinais AD-like dominam sem justificativa narrativa. | Há valor de conteúdo, mas alguns sinais de ruptura comercial. | Integração e forma coerentes com objetivo; transparência comercial preservada. |
| PRODUCT INTEGRATION | Produto aparece sem função ou com claim não sustentado. | Produto interrompe o conteúdo ou contexto é fraco. | Produto tem função narrativa/demonstrativa, com lacunas de integração/prova. | Presença necessária, contexto claro, fatos/claims qualificados. Usar N/A se não houver produto. |
| PAYOFF | Promessa não é cumprida ou resolução ausente. | Entrega parcial/vaga. | Resolução presente, mas conexão/promessa é incompleta. | Responde ao hook, mostra resultado observável ou conclui ideia sem exceder evidência. |
| CTA | Contradiz o objetivo, é enganoso ou interrompe conteúdo sem justificativa. | Ação/destino pouco claros ou prematuros. | Ação pertinente, mas posicionamento/clareza podem melhorar. | Ação específica, verdadeira e alinhada à resolução/destino. Usar N/A se CTA não for objetivo. |

Para uma dimensão marcada `N/A`, retirar seus 3 pontos possíveis do denominador. Se `ND` em qualquer dimensão aplicável, registrar score parcial e cobertura, não fingir avaliação completa.

## Cálculo

```text
SCORE = soma dos pontos das dimensões avaliáveis
MÁXIMO APLICÁVEL = 3 × número de dimensões aplicáveis
COBERTURA = dimensões avaliadas ÷ dimensões aplicáveis
PERCENTUAL HEURÍSTICO = SCORE ÷ MÁXIMO APLICÁVEL × 100
```

Registrar `SCORE / MÁXIMO APLICÁVEL`, percentual e dimensões N/A/ND. Sem dimensão aplicável ou sem cobertura suficiente, não calcular faixa.

Bandas iniciais para triagem **EXPERIMENTAL**:

- **0–33%:** revisar fundamentos antes de avançar.
- **34–66%:** corrigir lacunas e reavaliar.
- **67–100%:** blueprint editorialmente coerente para próxima etapa, ainda sujeito a revisão factual/humana.

As bandas não são benchmarks nem aprovação de publicação. Qualquer problema de veracidade, consentimento, segurança ou divulgação aplicável é bloqueador editorial independente do score.

## Alertas automáticos de revisão

| Alerta | Sinal de acionamento | Ação de revisão |
| --- | --- | --- |
| Hook fraco | ATTENTION ou HOOK ≤ 1 | Reexaminar relevância/contexto e clareza; não adicionar gatilhos por acumulação. |
| Início explicativo demais | Introdução explica contexto extenso antes de mostrar assunto/interesse | Identificar a informação mínima que orienta; preservar contexto necessário. |
| Produto com aparência de anúncio/interrupção | PRODUCT INTEGRATION ≤ 1 ou sinal forte em AD_LOOK_RISK | Reavaliar função narrativa e objetivo; venda direta pode ser intencional. |
| Ausência de progressão | RETENTION ≤ 1 | Reordenar beats ou remover repetição; não inserir suspense automático. |
| Retenção só pela fala | Informação não pode ser acompanhada visualmente quando ação/detalhe importa | Rever legibilidade, ação ou plano. Fala-only é válido quando conteúdo é verbal. |
| CTA precoce | CTA ocorre antes de payoff/valor sem razão de formato | Reposicionar ou justificar com objetivo. |
| Excesso de elementos | Múltiplos gatilhos, hooks, planos ou promessas competem | Selecionar somente mecanismo necessário. |
| Falta de payoff | PAYOFF ≤ 1 ou promessa sem entrega | Remover/limitar promessa ou planejar entrega verdadeira. |

## Registro recomendado

```text
ATTENTION: [0–3 / N/A / ND] — evidência/justificativa curta
HOOK: [...]
CURIOSITY: [...]
RETENTION: [...]
VISUAL DYNAMICS: [...]
NATIVE FEEL: [...]
PRODUCT INTEGRATION: [...]
PAYOFF: [...]
CTA: [...]
SCORE: [total / máximo aplicável] — cobertura: [avaliadas/aplicáveis]
ALERTAS: [lista ou nenhuma]
STATUS: heurística editorial; não é previsão
```

## Proveniência e status

As quatro referências sustentam ocorrências de abertura contextual, progressão, demonstração em alguns formatos, enquadramento vertical/frontal em amostras e fechamentos distintos. Não sustentam pesos, bandas, causalidade nem performance. Todo o score, bandas e acionamentos são **EXPERIMENTAIS** até avaliações inter-rater e comparação com resultados contextualizados. Ver [STATUS](../00_SISTEMA/STATUS.md) e [limitações do corpus](../../../06_GERADOS/reference_analysis/COMPARATIVO_4_VIDEOS.md).
