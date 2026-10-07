# Mapa conceitual de análise

Este documento descreve campos que poderão orientar uma análise futura. Os nomes são rótulos conceituais, não contrato de dados. **O exemplo JSON é apenas conceitual: não é schema oficial e não deve ser usado como implementação.**

Cada análise deve preservar a ligação entre sinais observados, interpretação e nível de confiança descritos em [EVIDENCE_RULES.md](EVIDENCE_RULES.md). Um campo pode ficar sem evidência suficiente; não se deve preencher por suposição.

| Campo | O que deverá ser registrado |
|---|---|
| `attention` | Sinais que podem destacar ou direcionar foco, com seus localizadores quando possível. |
| `curiosity` | Pergunta, lacuna ou detalhe que parece criar interesse, e se há resposta identificável. |
| `identification` | Situação, necessidade, rotina ou público que a peça representa ou nomeia. |
| `emotion` | Sinais expressivos observáveis e hipótese calibrada sobre o tom que podem sugerir. |
| `tension` | Questão, problema ou resultado pendente que organiza expectativa. |
| `retention` | Estrutura de progressão e encadeamento observável; não métrica presumida de permanência. |
| `reward` | Resposta, resultado, utilidade ou fechamento oferecido e quando aparece. |
| `desire` | Benefício ou experiência futura representada e sua base observável. |
| `trust` | Sinais de transparência, especificidade, consistência ou credibilidade apresentados. |
| `risk` | Objeções, condições, limites ou incertezas que são abordados ou permanecem sem resposta. |
| `proof` | Demonstrações, dados, depoimentos ou resultados mostrados, com origem e contexto se disponíveis. |
| `action` | CTA ou próximo passo apresentado, sua clareza e momento. |
| `sharing` | Elemento útil, significativo ou explicitamente compartilhável, sem prever que será compartilhado. |
| `virality_role` | Papel hipotético do mecanismo no percurso de circulação/compartilhamento, sem previsão de alcance. |
| `conversion_role` | Papel hipotético na consideração ou ação, sem afirmar compra ou conversão. |
| `confidence` | HIGH, MEDIUM ou LOW conforme a qualidade da evidência que apoia a leitura; não é chance de sucesso. |
| `evidence` | Descrição verificável do sinal e, quando possível, intervalos de tempo e fonte. |
| `interpretation` | Hipótese funcional ligada à evidência, com linguagem calibrada e limitações relevantes. |
| `remodeling` | Como transportar o mecanismo para uma execução UGC original e quais condições precisam ser preservadas. |

## Exemplo JSON conceitual

```json
{
  "mechanism": "curiosity",
  "time": {
    "start": "00:00",
    "end": "00:02"
  },
  "evidence": "Pergunta direta acompanhada por um close do produto.",
  "interpretation": "Pode favorecer curiosidade; hipótese para validação, sem dado de reação do público.",
  "confidence": "HIGH",
  "virality_role": "Pode abrir o percurso de atenção e curiosidade; não prevê compartilhamento.",
  "conversion_role": "Pode contextualizar uma dúvida relevante, caso a resposta tenha relação com a decisão.",
  "remodeling": "Criar uma pergunta original e relevante, seguida de demonstração e resposta verificável."
}
```

O exemplo ilustra apenas uma forma de pensar sobre os campos. `mechanism` e `time` aparecem para contextualizar o item, mas a estrutura, os tipos, a obrigatoriedade e a validação dos dados permanecem indefinidos. Qualquer schema futuro exige especificação própria e aprovação fora deste documento conceitual.
