# Psicologia do espectador

## Objetivo

Esta camada organiza a análise dos mecanismos psicológicos que uma referência parece mobilizar por meio de elementos observáveis do vídeo. Ela ajuda a descrever como atenção, interesse, progressão, confiança e ação podem estar sendo trabalhados, sem afirmar o que uma pessoa específica pensou, sentiu ou fez.

O framework não tenta “ler a mente” do espectador. As respostas internas do público só podem ser confirmadas com evidência apropriada, como pesquisa ou métricas de audiência; a inspeção da peça permite formular hipóteses calibradas, não declarar efeitos.

## Posição no pipeline

```text
REFERÊNCIA
→ VIDEO_INGESTION
→ EVIDÊNCIAS
→ PSICOLOGIA DO ESPECTADOR
→ VIRALIDADE / RETENÇÃO / CONVERSÃO
→ MECANISMOS DE UGC
→ REMODELAGEM
→ SOFIA
```

`VIDEO_INGESTION` fornece material e localizadores observáveis. Esta camada interpreta esse material como hipóteses psicológicas. As etapas seguintes podem considerar essas hipóteses ao selecionar mecanismos de UGC e remodelar uma peça original. Esta documentação não altera os contratos ou módulos existentes.

## Evidência e interpretação

**Evidência observável** descreve o que pode ser apontado na referência: por exemplo, uma pergunta falada, um close, texto na tela, uma demonstração, uma mudança de cena ou uma chamada para ação, preferencialmente com início e fim. **Interpretação** explica o que esses sinais podem favorecer, como curiosidade ou confiança. A interpretação deve permanecer identificada como hipótese e não pode ser reescrita como reação comprovada do público. Consulte [EVIDENCE_RULES.md](EVIDENCE_RULES.md).

## Viralidade, retenção e conversão

São objetivos relacionados, mas distintos. Viralidade trata da possibilidade de circulação e compartilhamento; retenção trata da progressão e da permanência ao longo da peça; conversão trata da passagem para uma ação desejada. Uma estrutura pode parecer desenhada para sustentar atenção sem haver dado de retenção, e atenção ou compartilhamento não comprovam compra. O [FRAMEWORK.md](FRAMEWORK.md) descreve essas relações sem tratá-las como resultados garantidos.

## Relação com UGC e remodelagem

A camada pode informar a escolha de mecanismos para UGC: por exemplo, uma demonstração progressiva, uma resposta a uma objeção ou uma recompensa clara. Na remodelagem, transportam-se o mecanismo e sua lógica, criando expressão original e compatível com a Sofia. Não se copiam frases, personagens, cenários ou sequências distintivas da referência.

## Status

**FRAMEWORK v1 — documentação inicial.** Define dimensões, regras de evidência e um mapa conceitual para análise futura. Não implementa análise automática, não define schema oficial e não mede desempenho. As hipóteses devem ser validadas com dados quando houver essa possibilidade.

## Documentos

- [FRAMEWORK.md](FRAMEWORK.md) — dimensões e relações entre mecanismos.
- [EVIDENCE_RULES.md](EVIDENCE_RULES.md) — separação entre observação e hipótese, confiança e remodelagem.
- [ANALYSIS_MAP.md](ANALYSIS_MAP.md) — campos conceituais para uma análise futura.
