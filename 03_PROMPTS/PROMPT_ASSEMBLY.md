# Montagem do prompt final

Este documento define o fluxo oficial para compor prompts de imagem e vídeo com os módulos existentes. É um contrato de montagem, não um prompt de geração. A composição deve preservar uma responsabilidade principal por camada e remover instruções repetidas antes de gerar.

Os significados, aliases autorizados e distinções entre campos estão definidos em [`GLOSSARIO_CANONICO.md`](GLOSSARIO_CANONICO.md). Use `[OBJECTIVE]` nos formulários novos; `[IMAGE_OBJECTIVE]` e `[VIDEO_OBJECTIVE]` permanecem aliases contextuais compatíveis.

## Fluxo oficial de vídeo

```text
INPUT: objetivo + produto/assunto + contexto + fatos e referências disponíveis
→ REFERENCE_ANALYSIS (somente quando houver referência a analisar)
→ UGC_TEMPLATE
→ HOOKS_RETENTION_CTA
→ MODULE_CARDS
→ VIDEO_DIRECTION
→ CAMERA_AND_PHOTOGRAPHY + STYLE_PRESETS
→ VIDEO_PROMPTS
→ MODEL_ADAPTER
→ PROMPT FINAL
```

1. **Input:** reúna objetivo, produto ou assunto, contexto de uso, público quando pertinente e fatos aprovados. Marque o que ainda não está confirmado; não complete lacunas como fatos.
2. **Reference analysis (opcional):** quando houver uma referência, use `REFERENCE_ANALYSIS/` para registrar observações, interpretações e padrões reutilizáveis. Leve adiante apenas um conceito remodelado e seus fatos aprovados; a referência não é um pedido para copiá-la.
3. **UGC template:** selecione um template principal em `UGC_TEMPLATES/VIDEO_TEMPLATES/`. Ele define formato e arco narrativo. Combine templates somente quando a peça realmente exigir mais de um arco.
4. **Hooks, retenção e CTA:** em `HOOKS_RETENTION_CTA/`, escolha a abertura, os mecanismos que organizam expectativa/progressão e a próxima ação. Encaixe-os nas etapas do template; não crie um roteiro paralelo. Use um hook e um CTA principal; retenção é opcional e deve servir ao arco.
5. **Module cards:** use `MODULE_CARDS/` para estruturar e preencher os componentes selecionados — produto, objetivo, roteiro, diálogo, ação, local, duração, mood, câmera, luz, estilo e adaptação. Os cards registram e completam decisões das etapas anteriores; não criam outro template ou uma segunda versão do roteiro.
6. **Video direction:** use `VIDEO_DIRECTION/` para descrever como pessoas, objetos e ações se comportam no tempo: atuação, gestos, pausas, ritmo e continuidade. Não repita a mensagem do roteiro nem instruções de captura.
7. **Camera, photography e style:** use `CAMERA_AND_PHOTOGRAPHY/` para enquadramento, perspectiva/lente, movimento de câmera, luz, profundidade e composição. Use no máximo um preset pertinente de `STYLE_PRESETS/` para acabamento. Cada dimensão deve aparecer uma vez, na formulação mais específica.
8. **Video prompts:** selecione uma estrutura compatível em `VIDEO_PROMPTS/` como mecanismo de composição/serialização: transfira para ela as decisões já preenchidas nas etapas anteriores e produza uma instrução audiovisual ordenada. Essa camada não escolhe o arco narrativo, hook, retenção, atuação ou conteúdo; esses vêm das respectivas camadas. Omita ou adapte trechos genéricos que repetiriam ou contrariariam as decisões selecionadas.
9. **Model adapter:** adapte a composição final à interface, versão e capacidades verificadas, usando `MODEL_ADAPTERS/README.md`. Separe texto, referências e parâmetros estruturados quando houver campos próprios. Preserve a intenção editorial e as restrições; não presuma capacidades.
10. **Prompt final:** entregue a composição resultante, sem placeholders vazios, alternativas não resolvidas, duplicações ou instruções incompatíveis.

## Fluxo oficial de imagem

```text
INPUT: objetivo + produto/assunto + contexto + fatos e referências disponíveis
→ REFERENCE_ANALYSIS (somente quando houver referência a analisar)
→ MODULE_CARDS
→ IMAGE_PROMPTS
→ CAMERA_AND_PHOTOGRAPHY + STYLE_PRESETS
→ MODEL_ADAPTER
→ PROMPT FINAL
```

1. Reúna objetivo, produto ou assunto, contexto e fatos aprovados. Se houver referência a analisar, aplique a etapa opcional de `REFERENCE_ANALYSIS/` e use somente o conceito remodelado.
2. Preencha os `MODULE_CARDS/` aplicáveis, como produto, objetivo, ação/pose observável, cena, local e mood. Para imagem estática, descreva o instante visual, não uma sequência temporal.
3. Escolha uma base em `IMAGE_PROMPTS/` para compor/serializar o assunto e a situação. Transfira as decisões dos cards e retire instruções genéricas repetidas.
4. Complete captura em `CAMERA_AND_PHOTOGRAPHY/` e acabamento em `STYLE_PRESETS/`, escolhendo configurações compatíveis e sem duplicar dimensões já cobertas pela base.
5. Adapte a composição a um modelo e interface verificados em `MODEL_ADAPTERS/README.md`; mantenha parâmetros estruturados separados quando a ferramenta permitir.
6. Entregue o prompt final sem placeholders vazios ou instruções incompatíveis.

## Responsabilidade por camada

| Camada | Responsabilidade principal | Não substitui |
| --- | --- | --- |
| `REFERENCE_ANALYSIS/` | Entender uma referência e separar observação, interpretação, abstração e hipótese. | Conteúdo original ou prompt de cópia. |
| `UGC_TEMPLATES/` | Definir formato e arco narrativo do vídeo. | Hook/retention/CTA, direção ou composição audiovisual. |
| `HOOKS_RETENTION_CTA/` | Definir abertura, mecanismos de progressão e próxima ação dentro do arco. | Roteiro completo ou direção técnica. |
| `MODULE_CARDS/` | Estruturar e preencher os componentes selecionados para a montagem. | Nova camada narrativa ou serializador final. |
| `VIDEO_DIRECTION/` | Descrever execução visual e temporal de ações, atuação e fala. | Enquadramento, luz ou intenção narrativa. |
| `CAMERA_AND_PHOTOGRAPHY/` | Definir captura, enquadramento, perspectiva/lente, movimento de câmera, luz e composição. | Atuação ou acabamento geral. |
| `STYLE_PRESETS/` | Definir acabamento/estética visual. | Identidade, conteúdo narrativo ou parâmetros de câmera/luz. |
| `VIDEO_PROMPTS/` | Compor/serializar decisões selecionadas em uma instrução audiovisual. | `UGC_TEMPLATES/`, `REFERENCE_ANALYSIS/` ou `VIDEO_DIRECTION/`. |
| `IMAGE_PROMPTS/` | Compor/serializar decisões visuais em uma instrução de imagem. | Análise de referência ou decisões de captura/estilo. |
| `MODEL_ADAPTERS/` | Adaptar formato e parâmetros a capacidades verificadas. | Alteração de intenção editorial ou invenção de capacidades. |

## Elementos compartilhados e específicos

| Compartilhados entre imagem e vídeo | Específicos de vídeo | Específicos de imagem |
| --- | --- | --- |
| Objetivo, produto/assunto, fatos/contexto, análise opcional de referência, ação/pose observável, cena, local, câmera/fotografia, iluminação, estilo, adaptação do modelo e restrições factuais. | Template UGC, hook, retenção, CTA, roteiro temporal, diálogo/áudio, duração, ritmo, movimento ao longo do tempo, continuidade e direção de atuação. | Composição de um estado/quadro estático, pose/ação no instante capturado, formato/corte e bases de `IMAGE_PROMPTS/`. Não usar roteiro, fala, duração, continuidade ou movimento temporal. |

Um elemento compartilhado só deve ser repetido se a repetição tiver função explícita no resultado final. Converter um plano de vídeo em imagem significa preservar o estado visual e as escolhas fotográficas aplicáveis, removendo a sequência temporal, fala e movimento.

## Campos de montagem

Use estes formulários para reunir decisões antes da serialização. São checklists de montagem, não campos-base herdados pelos templates UGC; cada template permanece autônomo. Remova campos que não se aplicam e não envie os rótulos ou tokens vazios ao modelo. `MODEL_ADAPTATION` representa a etapa posterior de adaptação, não um campo narrativo que cada template precise repetir.

### Vídeo

```text
PRODUCT: [PRODUCT]
OBJECTIVE: [OBJECTIVE]
CONTEXT: [CONTEXT]
UGC_FORMAT: [UGC_FORMAT]
UGC_TEMPLATE: [UGC_TEMPLATE]
HOOK: [HOOK]
RETENTION: [RETENTION]
SCRIPT: [SCRIPT]
DIALOGUE: [DIALOGUE]
CTA: [CTA]
BENEFIT: [BENEFIT]
VERIFIED_BENEFIT: [VERIFIED_BENEFIT]
PROOF: [PROOF]
ACTION: [ACTION]
VIDEO_DIRECTION: [VIDEO_DIRECTION]
LOCATION: [LOCATION]
CAMERA: [CAMERA]
LIGHTING: [LIGHTING]
STYLE: [STYLE]
DURATION: [DURATION]
VIDEO_PROMPT_STRUCTURE: [VIDEO_PROMPT_STRUCTURE]
MODEL_PROFILE: [MODEL_PROFILE]
MODEL_ADAPTATION: [MODEL_ADAPTATION]
```

### Imagem

```text
PRODUCT: [PRODUCT]
OBJECTIVE: [OBJECTIVE]
CONTEXT: [CONTEXT]
ACTION: [ACTION]
SCENE: [SCENE]
LOCATION: [LOCATION]
IMAGE_PROMPT_BASE: [IMAGE_PROMPT_BASE]
CAMERA: [CAMERA]
LIGHTING: [LIGHTING]
STYLE: [STYLE]
MODEL_PROFILE: [MODEL_PROFILE]
MODEL_ADAPTATION: [MODEL_ADAPTATION]
```

`[OBJECTIVE]` é o campo canônico compartilhado; os nomes legados `[VIDEO_OBJECTIVE]` e `[IMAGE_OBJECTIVE]` são aliases contextuais. `[MODEL_PROFILE]` identifica modelo/versão/capacidades verificadas; `[MODEL_ADAPTATION]` descreve a transformação da composição para essa interface. `BENEFIT` e `VERIFIED_BENEFIT` têm sentidos distintos; use `PROOF` conforme a estrutura em `GLOSSARIO_CANONICO.md`, somente com suporte real disponível.

## Proveniência e passagem entre camadas

A proveniência acompanha conteúdo relevante desde a fonte até o prompt final, sem alterar os fluxos oficiais acima. Use `source_type`, `source_id` quando existente, `origin_stage`, `evidence_status`, `confidence_level` quando aplicável, `allowed_consumers` e `generation_input` conforme [`GLOSSARIO_CANONICO.md`](GLOSSARIO_CANONICO.md). Em análise de referência, `evidence_status` reutiliza `EVIDENCE_CLASS`; não crie um sistema de classificação paralelo.

`REFERENCE_ANALYSIS/` produz observações localizadas, interpretações, hipóteses e padrões abstratos. Observações, interpretações e hipóteses não passam diretamente como fatos ou instruções de geração. Somente um padrão reutilizável remodelado pode orientar uma decisão editorial nova; produto, claims e benefícios factuais precisam de fonte apropriada independente. Briefing e decisões editoriais qualificadas alimentam templates, hooks e cards; estes passam decisões criativas elegíveis aos serializadores. Os serializadores compõem o material, sem criar sua evidência ou proveniência.

`BENEFIT` é ideia editorial e não deve ser apresentado como fato. `VERIFIED_BENEFIT` exige `PROOF` apropriado ao claim e ao escopo exato utilizado. O registro de suporte relaciona claim, tipo de evidência e, quando aplicável, `DATA_SOURCE`, `SOURCE_QUALIFICATION`, `EVIDENCE_LOCATOR` e `TESTIMONIAL` real/autorizado. Fonte insuficiente, indireta, não verificada ou inadequada não autoriza apresentar o claim como fato. Uma fala/alegação observada numa referência não é automaticamente prova.

`MODEL_ADAPTERS/` recebe a composição elegível e um `MODEL_PROFILE` verificado. Pode transformar a representação para a interface confirmada, mas deve preservar conteúdo, escopo e proveniência; não altera fonte, classe/status, confiança, qualificação ou autorização, e não preenche lacunas. Metadados de proveniência podem acompanhar o prompt como registro auxiliar sem serem expostos como instrução ao modelo. Consulte o glossário para a matriz de consumidores permitidos.

## Resolução de conflitos e deduplicação

1. Fatos fornecidos e restrições aprovadas do produto prevalecem sobre exemplos genéricos e hipóteses de referência.
2. Use um template UGC principal, um hook principal, um CTA principal e um preset de estilo por peça/plano, salvo transição intencional.
3. O template define o arco; hooks/retention/CTA encaixam mecanismos nesse arco; cards capturam componentes; direção define execução; captura e estilo definem aparência; a base de prompt apenas compõe essas decisões.
4. Preserve uma única instrução por dimensão. Se roteiro e diálogo forem o mesmo texto, inclua-o uma só vez. Não repita em direção a ação já definida no roteiro, nem em estilo uma escolha de câmera/luz já resolvida.
5. Segurança, uso correto e veracidade prevalecem sobre conveniência narrativa. Se o modelo não suportar um requisito, adapte a forma ou encaminhe o requisito para edição sem mudar a intenção.
6. Remova placeholders vazios e encaminhe parâmetros estruturados aos campos próprios da ferramenta quando existirem.
