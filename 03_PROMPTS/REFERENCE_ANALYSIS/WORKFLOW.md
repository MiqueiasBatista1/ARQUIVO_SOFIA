# Fluxo: referência a conceito original

Os campos com prefixo `OBSERVED_` são registros da referência, não campos de criação. As definições e separação entre observação, interpretação e hipótese estão em [`GLOSSARIO_CANONICO.md`](../GLOSSARIO_CANONICO.md) e `EVIDENCE_RULES.md`.

## 1. REFERÊNCIA → OBSERVAÇÃO

Identifique a fonte autorizada e o material disponível em `[REFERENCE_CONTEXT]`. Registre apenas sinais diretamente perceptíveis e localizáveis em `[EVIDENCE_LOCATOR]`. Marque o que estiver incompleto como lacuna.

## 2. OBSERVAÇÃO → DESMONTAGEM

Preencha os 20 campos de `ANALYSIS_TEMPLATE.md`. Separe conteúdo verbal, ação, produto, imagem, som e estrutura narrativa. Não analise aparência ou identidade de pessoas.

## 3. DESMONTAGEM → PADRÃO

Compare os beats observados e formule uma regra abstrata em `[REUSABLE_PATTERNS]`. O padrão deve descrever uma relação funcional, não reproduzir palavras ou sequência visual singular.

## 4. PADRÃO → MECANISMO

Proponha uma explicação em `[INTERPRETED_MECHANISM]`, ligada a uma evidência observada. Marque confiança e alternativas plausíveis. Se a explicação não puder ser confirmada pela referência, registre-a como hipótese.

## 5. MECANISMO → TEMPLATE

Encaminhe o padrão para módulos existentes em `PATTERN_TO_MODULES.md`. Formule uma estrutura em placeholders; não transporte as falas, claims, identidade, ativos ou detalhes exclusivos da referência.

## 6. TEMPLATE → REMODELAGEM

Substitua contexto, produto, situação, hook, ação, progressão, diálogo, captura e CTA por escolhas originais. Registre em `[REMODELING_OPPORTUNITIES]` o que mudou e por quê.

## 7. REMODELAGEM → NOVO CONCEITO

Combine a estrutura adaptada com `MODULE_CARDS/ORCHESTRATION.md` e o template UGC adequado. O novo conceito deve funcionar como peça independente, sem depender da referência para ser compreendido.

## 8. NOVO CONCEITO → HIPÓTESE A TESTAR

Antes de avaliar resultado, registre uma hipótese individual em `[HYPOTHESIS]` e seus parâmetros `[VARIABLE]`, `[COMPARISON]` e `[SUCCESS_CRITERION]`. `[HYPOTHESES_TO_TEST]` em `ANALYSIS_TEMPLATE.md` é uma coleção de possíveis hipóteses; não é alias de uma hipótese individual. Não atribua desempenho previsto nem observado sem dados coletados e contexto de comparação.

## Contrato de passagem e proveniência

Esta seção esclarece a qualificação das informações entre etapas sem alterar a ordem acima. Para cada achado relevante, mantenha `source_type`, `source_id` quando existir, `origin_stage`, `evidence_status`, `confidence_level` quando aplicável, `allowed_consumers` e `generation_input` conforme `ANALYSIS_TEMPLATE.md` e [`GLOSSARIO_CANONICO.md`](../GLOSSARIO_CANONICO.md).

- Os achados brutos ficam em `REFERENCE_ANALYSIS/`; observações, interpretações e hipóteses não seguem diretamente como fatos ou texto de geração.
- Apenas o princípio abstrato classificado como `REUTILIZAVEL`, após remodelagem para o novo contexto, pode informar seleção de `UGC_TEMPLATE`, `HOOK`, `RETENTION` ou outro componente editorial. A decisão nova recebe origem de sua etapa de remodelagem/briefing, mantendo a referência como antecedente rastreável, não como prova.
- Claims e fatos de produto devem vir do briefing/fonte apropriada, não ser copiados da referência. Para benefício factual, aplique a estrutura `PROOF` e a qualificação exigida no glossário.
- Registros observacionais podem ser consultados por `REFERENCE_ANALYSIS` e revisão; decisões criativas elegíveis seguem para templates, hooks e cards. Serializadores recebem somente decisões qualificadas. Não passe o pacote bruto de análise como instrução de geração.
- Em cada derivação, preserve a relação com a origem e registre a etapa produtora. Derivar ou herdar um valor não o verifica nem muda sua classe. Se não houver identificador, fonte ou confiança sustentada, mantenha a lacuna em vez de criar metadado fictício.
