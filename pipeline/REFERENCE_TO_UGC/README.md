# REFERENCE_TO_UGC

## Objetivo

REFERENCE_TO_UGC conecta a análise de uma referência, as hipóteses da psicologia do espectador, os mecanismos reutilizáveis e os templates UGC para propor uma estrutura original, adaptável à Sofia.

Sua regra central é: **PRESERVAR O MECANISMO. SUBSTITUIR A EXECUÇÃO.** O módulo não é um copiador de vídeos. É um sistema editorial de **ANÁLISE + SELEÇÃO + RECONSTRUÇÃO + ADAPTAÇÃO**.

## Função na arquitetura

```text
REFERÊNCIA
→ EVIDÊNCIAS
→ PSICOLOGIA DO ESPECTADOR
→ MECANISMOS
→ OBJETIVO
→ SELEÇÃO
→ REMODELAGEM
→ ESTRUTURA UGC
→ ADAPTAÇÃO PARA SOFIA
→ SAÍDA
```

- **REFERENCE_ANALYSIS — O QUE A REFERÊNCIA FAZ.** Registra elementos observáveis e padrões possíveis, preservando origem e limites.
- **PSICOLOGIA_ESPECTADOR — POR QUE O MECANISMO PODE FUNCIONAR.** Relaciona sinais observáveis a hipóteses psicológicas; não declara estados internos do público como fatos sem evidência apropriada.
- **MECANISMOS_UGC — QUAL MECANISMO REUTILIZÁVEL ESTÁ POR TRÁS.** Nomeia a lógica de conteúdo que pode ser reconstruída em novos contextos.
- **REFERENCE_TO_UGC — COMO TRANSFORMAR O MECANISMO EM UMA NOVA ESTRUTURA.** Seleciona, remodela e registra a proveniência, as decisões criativas e as limitações.
- **UGC_TEMPLATES — EM QUAL FORMATO EXECUTAR.** Oferece estruturas narrativas existentes, como demonstração, problema/solução, primeiro teste, rotina, GRWM, unboxing, review e storytelling. O mecanismo não determina sozinho o template.
- **SOFIA — QUEM EXECUTA.** A adaptação deve respeitar a identidade e as orientações já aprovadas para Sofia; este módulo não redefine sua identidade.

Hook, estrutura e formato não são sinônimos de mecanismo. Objetivo é o que se pretende otimizar, não um resultado comprovado. A sequência visual, a fala e os elementos específicos da referência não são transportados como instruções de execução.

## Exemplo de relação entre camadas

```text
REFERENCE: antes/depois de maquiagem
PSICOLOGIA: curiosidade + desejo + recompensa (hipóteses)
MECANISMO: progressão de transformação
ESTRUTURA: estado inicial → processo → resultado contextualizado
FORMATO: demonstração UGC
SOFIA: experiência pessoal e opinião natural, somente se verdadeiras e aprovadas
SAÍDA: novo roteiro original, sem copiar a sequência visual da referência
```

## Escopo desta documentação

Os seis documentos desta camada descrevem o workflow e o contrato editorial conceitual. Eles não criam automação, integração de IA/Groq, banco de dados ou schema técnico. Artefatos e código preexistentes nesta pasta não são redefinidos por esta documentação.

## Documentos

- [WORKFLOW.md](WORKFLOW.md) — etapas de análise, seleção, remodelagem e validação.
- [SELECAO_MECANISMOS.md](SELECAO_MECANISMOS.md) — critérios e matriz conceitual de seleção.
- [REMODELAGEM.md](REMODELAGEM.md) — o que transportar, substituir e não copiar.
- [UGC_OUTPUT.md](UGC_OUTPUT.md) — contrato conceitual editorial de saída.
- [EVIDENCE_RULES.md](EVIDENCE_RULES.md) — separação de evidência, interpretação, hipótese e resultado.
