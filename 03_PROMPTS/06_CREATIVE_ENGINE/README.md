# CREATIVE ENGINE

## Finalidade

Camada editorial reutilizável de engenharia de criativos curtos. Ajuda a escolher gatilhos e hooks, planejar progressão e linguagem audiovisual, avaliar risco de aparência publicitária e revisar um blueprint antes da montagem UGC.

Fluxo conceitual: `REFERÊNCIA → PADRÕES → CREATIVE ENGINE → UGC`.

## Relação com as bibliotecas existentes

- `../04_UGC/REFERENCE_PATTERNS.md` registra abstrações de referência; `../04_UGC/PATTERN_AUDIT.md` registra suas limitações. Esta engine usa esses achados como evidência local, não os substitui nem os apaga.
- `../HOOKS_RETENTION_CTA/HOOKS/` já contém 11 famílias de hooks; `RETENTION/` já contém 10 módulos e `CTAS/` contém 8 fichas. As bibliotecas abaixo classificam/selecionam possibilidades e apontam para esses módulos, sem criar outro sistema de roteiro/CTA.
- `../CAMERA_AND_PHOTOGRAPHY/`, `../VIDEO_DIRECTION/` e `../MODULE_CARDS/CAMERA.md` descrevem captura e execução. Esta camada trata a função editorial potencial e encaminha as escolhas para essas camadas.
- `../UGC_TEMPLATES/VIDEO_TEMPLATES/` contém 15 arcos narrativos. O blueprint da engine recomenda compatibilidade; não substitui nem preenche o template.
- `../PROMPT_ASSEMBLY.md` preserva o fluxo oficial: template UGC, hooks/retenção/CTA, cards, direção, captura/estilo e serialização. A engine é etapa de planejamento editorial antes do preenchimento, sem alterar esse contrato.

## O que a engine faz

- separa evidência observada, princípios editoriais, hipóteses e recursos experimentais;
- escolhe mecanismos compatíveis com objetivo, público/contexto, formato e prova disponível;
- ajuda a desenhar a janela 0–3 s sem exigir cortes ou fórmula fixa;
- relaciona retenção, ação, câmera e integração comercial ao arco;
- aplica revisão qualitativa anti-propaganda;
- calcula score heurístico de prontidão e expõe lacunas/alertas;
- devolve um `CREATIVE_BLUEPRINT` para seleção editorial posterior.

## O que não faz

- não cria ideia, roteiro, fala final, copy, UGC de creator específico ou conteúdo para Sofia;
- não gera prompts de imagem/vídeo nem chama APIs;
- não confirma claims, provas, depoimentos ou adequação regulatória;
- não prevê performance, viralidade, conversão ou retenção;
- não altera vídeos, transcrições, análises ou módulos existentes;
- não substitui UGC_TEMPLATE, direção, câmera/fotografia, STYLE_PRESETS ou MODEL_ADAPTERS.

## Arquivos

- [Princípios](00_SISTEMA/ENGINE_PRINCIPLES.md) · [Status](00_SISTEMA/STATUS.md)
- [Biblioteca de gatilhos](01_GATILHOS/TRIGGER_LIBRARY.md)
- [Biblioteca de hooks](02_HOOKS/HOOK_LIBRARY.md) · [Fórmula](02_HOOKS/HOOK_FORMULA.md) · [Janela 0–3 s](02_HOOKS/HOOK_0_3S.md)
- [Biblioteca de retenção](03_RETENCAO/RETENTION_LIBRARY.md) · [Sequência](03_RETENCAO/RETENTION_SEQUENCE.md)
- [Câmera](04_CAMERA_MOVIMENTO/CAMERA_LIBRARY.md) · [Movimento](04_CAMERA_MOVIMENTO/MOVEMENT_LIBRARY.md)
- [Native feel](05_ANTI_PROPAGANDA/NATIVE_FEEL.md) · [Risco ad-like](05_ANTI_PROPAGANDA/AD_LOOK_RISK.md)
- [Scoring](06_SCORING/CREATIVE_SCORE.md)
- [Orquestração](07_ORQUESTRACAO/CREATIVE_ORCHESTRATOR.md)

## Status atual

Biblioteca editorial inicial, não calibrada em testes de público. Ocorrências de contexto no hook, progressão, perspectiva pessoal e fechamento têm evidência descritiva nas quatro referências. Hooks/retention avançados, pattern interrupts, movimento, anti-propaganda e score permanecem **EXPERIMENTAL**. Consulte `00_SISTEMA/STATUS.md`.

## Próximos testes necessários

1. Revisar os quatro vídeos continuamente para confirmar cortes, sincronização fala–ação, movimento e CTAs visuais.
2. Testar hipóteses de mecanismo uma variável por comparação adequada; registrar público, plataforma, exposição, janela e métrica antes de interpretar resultado.
3. Calibrar consistência entre avaliadores do score e verificar se suas dimensões ajudam decisões editoriais; não treinar limiares com as quatro referências.
4. Reavaliar exemplos de risco publicitário por formato/plataforma e contexto de divulgação, sem pressupor que estilo nativo esconda intenção comercial.

## Convenção

`VALIDADO` qualifica presença observada no conjunto de referências. `PRINCÍPIO` é orientação editorial explícita. `HIPÓTESE` deve ter variável, comparação e resultado observável. `EXPERIMENTAL` precisa de teste próprio. Nenhum status aqui valida claims comerciais.
