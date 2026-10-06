# Orquestrador da Creative Engine

## Papel

Converter briefing/fatos e padrões qualificados em uma seleção editorial revisável: `CREATIVE_BLUEPRINT`. Não gera roteiro final, falas, cenas detalhadas nem prompts. Mantém a ordem narrativa no template UGC existente e entrega escolhas compatíveis às camadas de montagem.

## Entrada conceitual

```text
PRODUCT
OBJECTIVE
AUDIENCE
UGC_FORMAT
EMOTIONAL_ANGLE
TRIGGER
HOOK
RETENTION
CAMERA
NATIVE_STYLE
PROOF
PAYOFF
CTA
```

- `PRODUCT`, `OBJECTIVE`, `UGC_FORMAT`, `HOOK`, `RETENTION`, `CAMERA`, `PROOF`, `PAYOFF`, `CTA` seguem definições/limites do [GLOSSARIO_CANONICO](../../GLOSSARIO_CANONICO.md) e dos módulos já existentes.
- `AUDIENCE`, `EMOTIONAL_ANGLE`, `TRIGGER` e `NATIVE_STYLE` são dimensões desta ficha conceitual, não novos aliases canônicos. Marcar desconhecido quando não houver briefing.
- `PROOF` só recebe fonte real, claim delimitado e qualificação conforme o glossário. Não copiar alegação observada em referência como prova.
- Cada seleção carrega classe `EVIDENCE / PRINCIPLE / HYPOTHESIS / EXPERIMENTAL` e localizador/origem quando houver. Ausência de origem fica como lacuna.

## Processo de seleção

1. **Validar entrada:** separar fato fornecido, preferência editorial, inferência e campo ausente. Não completar campo ausente.
2. **Definir arco:** apontar um `UGC_TEMPLATE` compatível em [UGC_TEMPLATES](../../UGC_TEMPLATES/README.md). A Creative Engine recomenda; o template existente continua sendo a estrutura narrativa.
3. **Escolher um eixo de atenção:** um trigger principal e uma família de hook. Combinação adicional só se cada sinal reforçar o mesmo interesse.
4. **Desenhar progressão:** escolher zero ou poucos mecanismos de retenção que se encaixam em beats do template. Cada promessa precisa de payoff identificável. Não instalar pattern interrupt por padrão.
5. **Integrar ação/produto:** usar demonstração quando há ação real e legível. Separar demonstração de `PROOF`; selecionar fonte/prova somente quando fornecida e apropriada.
6. **Selecionar câmera/movimento:** capturar o beat necessário com dimensões específicas. Encaminhar escolhas concretas a [CAMERA_AND_PHOTOGRAPHY](../../CAMERA_AND_PHOTOGRAPHY/README.md), `VIDEO_DIRECTION/` e `MODULE_CARDS/`.
7. **Avaliar native feel:** usar [NATIVE_FEEL](../05_ANTI_PROPAGANDA/NATIVE_FEEL.md) e [AD_LOOK_RISK](../05_ANTI_PROPAGANDA/AD_LOOK_RISK.md) como filtro qualitativo, mantendo divulgação/transparência.
8. **Avaliar score:** registrar dimensões, cobertura, alertas e lacunas conforme [CREATIVE_SCORE](../06_SCORING/CREATIVE_SCORE.md). Não tratar score como performance.
9. **Revisar conflitos:** remover mecanismos duplicados/incompatíveis; evitar empilhamento. Validar claims, promessa, prova, privacidade, segurança e CTA/destino.
10. **Entregar blueprint:** proposta editorial abstrata para aprovação/seleção UGC posterior. Não expandir para falas ou roteiro final.

## Formato de saída conceitual — CREATIVE_BLUEPRINT

```yaml
creative_blueprint:
  objective: "[OBJECTIVE]"
  product: "[PRODUCT or N/A]"
  audience_context: "[AUDIENCE or UNKNOWN]"
  ugc_format: "[UGC_FORMAT]"
  ugc_template_candidate: "[existing UGC_TEMPLATE]"
  emotional_angle: "[EMOTIONAL_ANGLE or UNKNOWN]"
  attention:
    trigger: "[TRIGGER]"
    evidence_status: "[EVIDENCE | PRINCIPLE | HYPOTHESIS | EXPERIMENTAL]"
    hook_family: "[HOOK FAMILY]"
    hook_mode: "[VERBAL | VISUAL | BEHAVIORAL | COMBINED]"
    0_3s_review: "[decision/checklist result; no mandatory cuts]"
  retention:
    selected_mechanisms: ["[zero or few existing-compatible mechanisms]"]
    sequence_fit: "[template beats / UNKNOWN]"
    payoff: "[observable or informational delivery]"
  camera:
    framing: "[decision or UNKNOWN]"
    distance_perspective: "[decision or UNKNOWN]"
    movement: "[decision or NONE/UNKNOWN]"
    rationale: "[narrative legibility]"
  native_review:
    classification: "[NATIVE | NATIVE COM RISCO | AD-LIKE | UNKNOWN]"
    observable_signals: ["[signals]"]
    disclosure_check: "[required/contextual review]"
  evidence:
    proof: "[source-backed PROOF or NONE]"
    limitations: ["[unknowns/qualifications]"]
  cta: "[CTA or NONE]"
  score:
    total: "[score / applicable maximum / coverage]"
    alerts: ["[alerts]"]
  open_decisions: ["[unresolved editorial decisions]"]
```

Placeholders acima descrevem a ficha de decisão; não são prompt nem conteúdo pronto para geração. Campos opcionais podem ser omitidos no uso real, mas ausência de evidência deve ser preservada. `NONE` é decisão editorial; `UNKNOWN` é lacuna de informação.

## Exemplo estrutural abstrato

```text
Objetivo: venda
Trigger: problema reconhecível (EXPERIMENTAL, exigir problema real)
Hook: situação contextual + ação imediata coerente
Retention: progressão simples + payoff identificado
Camera: plano próximo somente se detalhe/ação exigir
Native: situação real e linguagem compatível; disclosure preservado
Proof: demonstração/dado elegível, sem ampliar seu escopo
CTA: ação alinhada à resolução e destino real
```

Isto apenas ilustra relações entre campos; não escolhe produto, audiência, fala ou roteiro.

## Relação com fluxo oficial e bibliotecas

```text
REFERENCE_ANALYSIS (opcional)
→ REFERENCE_PATTERNS / evidência remodelada
→ CREATIVE ENGINE (seleção + revisão + blueprint)
→ escolha/preenchimento de UGC_TEMPLATE
→ HOOKS_RETENTION_CTA
→ MODULE_CARDS
→ VIDEO_DIRECTION
→ CAMERA_AND_PHOTOGRAPHY + STYLE_PRESETS
→ VIDEO_PROMPTS / MODEL_ADAPTER
```

No [PROMPT_ASSEMBLY](../../PROMPT_ASSEMBLY.md), o fluxo oficial continua começando pelo template UGC antes de hooks/retenção/cards. A engine é uma etapa de planejamento que recomenda template e componentes; ao executar montagem, seguir a ordem oficial sem gerar arco paralelo.

Bibliotecas que a engine seleciona, sem duplicar:

- [Hooks, retenção e CTAs](../../HOOKS_RETENTION_CTA/README.md)
- [Templates UGC](../../UGC_TEMPLATES/README.md)
- [Câmera/fotografia](../../CAMERA_AND_PHOTOGRAPHY/README.md) e [direção](../../VIDEO_DIRECTION/README.md)
- [Cards de composição](../../MODULE_CARDS/ORCHESTRATION.md)

## Critérios de rejeição/revisão

- Claim sem fonte adequada ou alegação copiada da referência → não aprovar como fato.
- Hook promete resultado fora da evidência ou que o corpo não entrega → revisar/remover promessa.
- Trigger de urgência sem prazo/estoque confirmado → não usar.
- Demonstração interpretada como prova geral → limitar ou acrescentar evidência independente.
- Retention depende de suspense sem payoff → reconstruir progressão.
- Múltiplos mecanismos competem → escolher o que serve ao arco e remover duplicação.
- Score alto com lacunas, baixa cobertura ou bloqueador factual → não considerar aprovado.

Ver [ENGINE_PRINCIPLES](../00_SISTEMA/ENGINE_PRINCIPLES.md), [STATUS](../00_SISTEMA/STATUS.md), [HOOK_FORMULA](../02_HOOKS/HOOK_FORMULA.md) e [RETENTION_SEQUENCE](../03_RETENCAO/RETENTION_SEQUENCE.md).
