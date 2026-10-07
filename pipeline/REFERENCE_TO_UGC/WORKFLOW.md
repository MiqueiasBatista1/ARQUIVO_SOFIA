# Workflow de REFERENCE_TO_UGC

Este workflow transforma evidências de uma referência em uma proposta UGC original. Cada etapa mantém explícitas as entradas, decisões e incertezas; uma inferência não se torna fato por passar de etapa.

## 1. RECEBER REFERÊNCIA

- **Entrada:** vídeo ou referência identificável, origem e `reference_id` quando disponível.
- **Processamento conceitual:** confirmar que o material é acessível e identificar o escopo analisável (vídeo completo, trecho, áudio, texto ou frames disponíveis).
- **Saída:** referência delimitada e rastreável.
- **Cuidados:** registrar lacunas, qualidade e partes ausentes. Não completar cenas, falas ou contexto por suposição.

## 2. COLETAR EVIDÊNCIAS

- **Entrada:** referência delimitada e materiais observáveis.
- **Processamento conceitual:** descrever ações, falas, texto, transições e duração com localizadores quando possível; separar o que é visto/ouvido de alegações feitas no próprio vídeo.
- **Saída:** observações localizáveis, incluindo incertezas.
- **Cuidados:** uma alegação observada na referência não é fato confirmado nem prova sobre outro produto.

## 3. IDENTIFICAR MECANISMOS PSICOLÓGICOS

- **Entrada:** evidências observáveis.
- **Processamento conceitual:** formular hipóteses sobre curiosidade, atenção, identificação, desejo, confiança ou outras dimensões pertinentes, ligando cada uma aos sinais observados.
- **Saída:** hipóteses psicológicas justificadas e limitações.
- **Cuidados:** não afirmar o que o espectador pensou, sentiu ou fez sem evidência apropriada.

## 4. IDENTIFICAR MECANISMOS DE CONTEÚDO

- **Entrada:** evidências e interpretações psicológicas.
- **Processamento conceitual:** abstrair a lógica reutilizável da peça usando [MECANISMOS_UGC](../MECANISMOS_UGC/README.md). Distinguir mecanismo de estrutura, formato e contexto.
- **Saída:** um ou mais mecanismos candidatos, com sinais que os sustentam.
- **Cuidados:** não tratar hook, POV, unboxing, antes/depois ou rotina isoladamente como mecanismo. Se não houver base suficiente, registrar “indeterminado”.

## 5. DEFINIR OBJETIVO

- **Entrada:** briefing da nova peça e necessidade de comunicação.
- **Processamento conceitual:** escolher o objetivo prioritário (por exemplo, atenção, retenção, confiança, compartilhamento ou conversão) e objetivos secundários quando úteis.
- **Saída:** objetivo e critério futuro de avaliação.
- **Cuidados:** objetivo é intenção de otimização. Não o inferir automaticamente a partir do desempenho percebido da referência.

## 6. DEFINIR PRODUTO / CONTEXTO

- **Entrada:** briefing factual aprovado, público/contexto pertinente e objetivo.
- **Processamento conceitual:** identificar produto, uso, estágio da jornada, necessidade e fatos ou provas que podem ser comunicados.
- **Saída:** contexto novo, limites factuais e lacunas explícitas.
- **Cuidados:** não transferir benefício, preço, resultado, avaliação ou experiência da referência. Sem base factual aprovada, não apresentar claim como fato.

## 7. SELECIONAR MECANISMOS

- **Entrada:** mecanismos candidatos, objetivo e contexto/produto novos.
- **Processamento conceitual:** aplicar os critérios de [SELECAO_MECANISMOS.md](SELECAO_MECANISMOS.md); selecionar principal e secundários apenas se tiverem função clara.
- **Saída:** mecanismo(s) escolhidos e justificativa vinculada à evidência e ao novo objetivo.
- **Cuidados:** não usar pontuação automática nem presumir que combinar mecanismos melhora performance.

## 8. ESCOLHER ESTRUTURA

- **Entrada:** mecanismos selecionados, prova disponível e limites do contexto.
- **Processamento conceitual:** organizar a sequência de abertura, progressão, tensão ou questão, demonstração, recompensa/resolução e encerramento conforme aplicável.
- **Saída:** beats ou etapas originais da nova peça.
- **Cuidados:** a estrutura pode abstrair uma relação lógica, mas não deve reproduzir a ordem distintiva de cenas da referência.

## 9. ESCOLHER FORMATO UGC

- **Entrada:** estrutura, objetivo, contexto, recursos e preferências editoriais.
- **Processamento conceitual:** escolher um template existente em [`03_PROMPTS/UGC_TEMPLATES/`](../../03_PROMPTS/UGC_TEMPLATES/README.md) e declarar separadamente o formato UGC aplicável.
- **Saída:** formato e template compatíveis com a estrutura.
- **Cuidados:** template/formato executa a estrutura; não é o mecanismo. Respeitar os módulos obrigatórios, condicionais e restrições do template escolhido.

## 10. REMODELAR

- **Entrada:** mecanismo e estrutura abstratos, formato escolhido e briefing novo.
- **Processamento conceitual:** manter a lógica útil e reconstruir produto, contexto, falas, ações, cenas, ritmo e expressão para a nova peça, seguindo [REMODELAGEM.md](REMODELAGEM.md).
- **Saída:** conceito criativo original com rastreabilidade da referência e registro do que foi substituído.
- **Cuidados:** não copiar frases, diálogos, personagem, identidade, cenário distintivo, sequência idêntica ou ativos desnecessários.

## 11. ADAPTAR PARA SOFIA

- **Entrada:** conceito remodelado e orientações aprovadas de identidade/personagem.
- **Processamento conceitual:** adequar voz, presença, ações e naturalidade à Sofia, sem criar fatos biográficos, experiência pessoal, opinião ou testemunho não aprovados.
- **Saída:** versão interpretável/executável pela Sofia, com experiência e claims devidamente qualificados.
- **Cuidados:** não redefinir a identidade oficial nem simular experiência real. Usar apenas informação e caracterização autorizadas.

## 12. PRODUZIR SAÍDA

- **Entrada:** decisões anteriores, evidências, limites factuais e adaptação para Sofia.
- **Processamento conceitual:** preencher o contrato editorial descrito em [UGC_OUTPUT.md](UGC_OUTPUT.md), preservando campos desconhecidos e provenance.
- **Saída:** estrutura UGC original documentada, pronta para revisão e posterior execução por template.
- **Cuidados:** esta documentação define um contrato conceitual, não um schema técnico nem uma instrução para gerar conteúdo automaticamente.

## 13. VALIDAR

- **Entrada:** saída conceitual completa e referência rastreável.
- **Processamento conceitual:** verificar originalidade da execução, consistência entre mecanismo/psicologia/estrutura/formato/objetivo, fidelidade factual, prova, limites, adaptação para Sofia e compatibilidade com o template.
- **Saída:** proposta aprovada para próxima etapa ou lista de lacunas/correções.
- **Cuidados:** validação editorial não mede performance. Resultados só podem ser declarados após teste próprio e registro de métricas/contexto conforme [EVIDENCE_RULES.md](EVIDENCE_RULES.md).

## Distinções fundamentais

**PSICOLOGIA ≠ MECANISMO ≠ ESTRUTURA ≠ FORMATO ≠ PERSONAGEM.** Psicologia é a razão hipotética; mecanismo é a lógica reutilizável; estrutura é sua sequência; formato é o modo de execução UGC; personagem é quem executa. **OBJETIVO** é o que se pretende otimizar e **CONTEXTO** é a situação à qual a peça pertence; nenhum deles substitui os demais níveis.
