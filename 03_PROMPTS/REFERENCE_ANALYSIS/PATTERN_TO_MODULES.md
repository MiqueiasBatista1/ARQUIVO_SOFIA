# Encaminhar padrões para módulos existentes

Use este mapa para transformar achados abstratos em blocos de criação. Ele não contém um segundo catálogo de hooks, CTAs ou templates.

Este mapa não autoriza a cópia direta de achados brutos. `OBSERVADO`, `INTERPRETADO` e `HIPOTESE` não são entradas factuais de criação; apenas um padrão abstrato `REUTILIZAVEL`, remodelado para o novo contexto, pode orientar uma decisão editorial. Claims, benefícios verificados e provas precisam de fontes próprias e qualificação conforme [`GLOSSARIO_CANONICO.md`](../GLOSSARIO_CANONICO.md) e [`EVIDENCE_RULES.md`](EVIDENCE_RULES.md).

| Achado de referência | Destino na biblioteca | Como transferir |
| --- | --- | --- |
| Padrão abstrato de abertura, após remodelagem | `HOOKS_RETENTION_CTA/HOOKS/` | Selecione estrutura compatível e escreva conteúdo novo; a fala/claim observado não é transferido. |
| Princípio abstrato de progressão, após remodelagem | `HOOKS_RETENTION_CTA/RETENTION/` | Reaproveite a função geral, não o timing ou evento distintivo da referência. |
| Nova ação editorial para a peça | `HOOKS_RETENTION_CTA/CTAS/` | Escolha CTA compatível com novo objetivo e destino real; não copie a solicitação observada. |
| Padrão abstrato de arco, após remodelagem | `UGC_TEMPLATES/VIDEO_TEMPLATES/` | Selecione estrutura apropriada; substitua eventos, claims e conteúdo. |
| Ação ou demonstração | `MODULE_CARDS/ACTION.md`, `VIDEO_DIRECTION/` | Reescreva em ações observáveis seguras e relevantes ao novo contexto. |
| Enquadramento, movimento, luz ou ambiente | `CAMERA_AND_PHOTOGRAPHY/` | Descreva a função visual em termos gerais; crie nova composição e execução. |
| Ritmo ou intensidade | `MODULE_CARDS/DURATION.md`, `VIDEO_DIRECTION/` | Ajuste ao novo roteiro e mood, sem imitar cadência singular. |
| Produto ou objetivo da nova peça | `MODULE_CARDS/PRODUCT.md`, `MODULE_CARDS/OBJECTIVE.md` | Use dados aprovados da nova peça; não transfira claims da referência. Uma alegação observada não é `DATA_SOURCE` nem `PROOF`. |
| Novo conceito combinado | `MODULE_CARDS/ORCHESTRATION.md` e `PROMPT_ASSEMBLY.md` | Monte os módulos e remova duplicações. |

Registre em `[REUSABLE_PATTERNS]` o princípio geral e em `[NON_COPYABLE_ELEMENTS]` o que deve ser substituído. Não converta automaticamente todo detalhe observado em instrução de geração.
