# Regras de evidência e classificação

Use estas definições em todo formulário de análise. Uma mesma ideia pode passar por várias classes, mas deve ser reescrita e rotulada ao mudar de classe.

O contrato de proveniência e consumidores está em [`GLOSSARIO_CANONICO.md`](../GLOSSARIO_CANONICO.md); use-o junto destas regras.

## OBSERVADO

Algo diretamente visível, legível ou audível na referência fornecida. Registre trecho/timestamp, fonte e lacunas. Prefira descrição concreta: “há uma pergunta falada na abertura” em vez de “o vídeo prende a atenção”.

## INTERPRETADO

Uma leitura sobre intenção, função ou mecanismo que não está explicitamente declarada. Apresente como interpretação, cite o que motivou a leitura e indique confiança. Uma interpretação não prova que o recurso funcionou.

## HIPÓTESE

Uma previsão que pode ser testada numa nova peça ou experimento. Formule variável, versão de comparação, resultado mensurável e critério antes de concluir. Não transforme visualizações ou engajamento sem fonte/contexto em evidência.

## REUTILIZÁVEL

Um princípio abstrato de estrutura, como “apresentar a pergunta antes da explicação” ou “mostrar cada etapa no momento em que é mencionada”. Remova redação, ritmo distintivo, composição exata, ativos, identidade, produto e contexto próprios da referência.

## NÃO COPIAR

Marque elementos particulares que precisam ser substituídos na criação original: falas ou texto distintivos, sequência expressiva específica, identidade e aparência do creator, marca, embalagem, música, grafismos, cenário identificável e outros ativos do original. A análise não deve reproduzir esses elementos como instrução para a nova peça.

## Métricas e alegações

- Não classifique referência como viral, vencedora, eficaz ou de alta performance sem dados verificáveis e contexto de medição.
- Se métricas forem fornecidas, registre valor, origem, data, janela temporal e definição disponível. Não infira causalidade a partir de correlação.
- Não invente diálogos, cenas, duração, enquadramentos, objetivos ou fatos que não estejam no material.
- Diferencie fala promocional da referência de fato verificado; uma alegação presente no vídeo não se torna verdadeira por ter sido observada.
- Quando o material for parcial, sem áudio ou de baixa qualidade, registre `[UNKNOWN_OR_MISSING]` ou descrição equivalente e limite as conclusões.

## Passagem de evidência para criação

- `OBSERVADO` descreve apenas o que a referência permite localizar. Um claim ouvido ou texto visto continua sendo um claim observado; não é fato confirmado, `PROOF` nem autorização para repetir a alegação.
- `INTERPRETADO` e `HIPOTESE` permanecem na análise/revisão editorial. Podem motivar uma decisão ou experimento novo, desde que sejam explicitamente remodelados; não entram como fatos, claims ou instruções da nova peça.
- `REUTILIZAVEL` só pode seguir como princípio abstrato depois de remover conteúdo, contexto, ativos e expressão particulares da referência e reescrevê-lo para o briefing novo.
- `CLAIM` é uma afirmação proposta sobre produto/conteúdo. Para ser apresentado como fato, precisa de suporte apropriado ao seu escopo; a classificação ou confiança de uma observação não valida o claim.
- `PROOF` registra o suporte real de um claim. Use `DATA_SOURCE` para a fonte documental/dados, `SOURCE_QUALIFICATION` para seus limites e `TESTIMONIAL` somente para relato real e autorizado quando aplicável. `EVIDENCE_LOCATOR` localiza material observado; sozinho, não constitui prova de claim de produto.
- `SOURCE_QUALIFICATION` deve explicitar fonte insuficiente, indireta, não verificada ou inadequada. Nesses casos, não use o suporte para declarar `VERIFIED_BENEFIT` nem para gerar o claim como fato.
- `BENEFIT` pode permanecer como ideia editorial, mas não como alegação factual. `VERIFIED_BENEFIT` exige evidência apropriada que sustente aquele benefício e seu escopo específicos.
- Não invente fonte, qualificação, evidência, testemunho, ID, confiança ou status. Quando faltar informação, mantenha a lacuna identificada.

Somente decisões criativas remodeladas e informações de produto qualificadas podem seguir para `UGC_TEMPLATES/`, `HOOKS_RETENTION_CTA/`, `MODULE_CARDS/` e os serializadores. Consulte a matriz de elegibilidade no glossário; consumidores posteriores preservam a proveniência e não reclassificam o registro.
