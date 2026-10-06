# ORCHESTRATION

Esta ficha orienta a seleção e montagem das demais fichas. Use-a como checklist de composição, não como mais um bloco repetido no prompt final.

O fluxo completo e sua ordem oficial estão em [`PROMPT_ASSEMBLY.md`](../PROMPT_ASSEMBLY.md). Os cards estruturam e preenchem decisões já selecionadas: em vídeo, escolha o template UGC e encaixe hook, retenção e CTA antes de completar os cards; em imagem, use apenas os componentes visuais aplicáveis. Esta página é um checklist de seleção e combinação, não um serializador final nem uma base herdada pelos templates UGC, que permanecem autônomos. A adaptação de modelo continua na etapa posterior definida no fluxo oficial.

Use [`GLOSSARIO_CANONICO.md`](../GLOSSARIO_CANONICO.md) para definições. `IMAGE_OBJECTIVE` e `VIDEO_OBJECTIVE` são aliases contextuais de `OBJECTIVE`; `UGC_FORMAT` e `UGC_TEMPLATE`, `SCRIPT` e `DIALOGUE`, `ACTION` e `VIDEO_DIRECTION`, `STYLE` e `MOOD`, `MODEL_PROFILE` e `MODEL_ADAPTATION` permanecem campos distintos.

## Proveniência dos valores

Os cards recebem valores diretos do briefing, derivados de decisões editoriais ou verificados em fontes de produto; identifique sua origem e classe conforme o contrato do glossário. Quando um campo vier de remodelagem de referência, preserve a ligação à origem, mas registre como produtora a etapa que tomou a nova decisão. Os cards não consomem achados brutos `OBSERVADO`, `INTERPRETADO` ou `HIPOTESE` como fatos nem os convertem em claims.

`BENEFIT` continua sendo uma ideia editorial. Use `VERIFIED_BENEFIT` somente com `PROOF` adequado ao claim e à sua abrangência. Não invente `DATA_SOURCE`, `SOURCE_QUALIFICATION`, `TESTIMONIAL`, `source_id` ou estado de evidência. Se a fonte for insuficiente, indireta, não verificada ou inadequada, registre o limite e não eleve o campo a benefício verificado.

Preencha somente os campos pertinentes do checklist; proveniência acompanha o campo ao longo da composição, mas não precisa ser repetida como prosa no prompt final. Herança de campos comuns entre templates permanece possibilidade futura, sem obrigatoriedade introduzida aqui.

## Quando usar

Use ao transformar um briefing de imagem ou vídeo UGC/TikTok Shop em uma instrução final para um modelo. Comece pelo objetivo e selecione somente os módulos necessários.

## Como combinar

Para **imagem**, escolha `PRODUCT` + `OBJECTIVE` + `ACTION` + `LOCATION` + `CAMERA` + `LIGHTING` + `MOOD`/`STYLE`. Omita `UGC_FORMAT`, `HOOK`, `SCRIPT`, `DIALOGUE` e `DURATION`, a menos que o fluxo de trabalho exija esses campos como metadados.

Para **vídeo**, escolha `PRODUCT` + `OBJECTIVE` + `UGC_FORMAT` + `UGC_TEMPLATE` + `HOOK` + `RETENTION` quando aplicável + `SCRIPT` + `ACTION` + `VIDEO_DIRECTION` quando aplicável + `CAMERA` + `LIGHTING` + `LOCATION` + `MOOD` e/ou `STYLE` sem os confundir + `DURATION` quando exigida. Acrescente `DIALOGUE` quando houver fala, `BENEFIT`/`VERIFIED_BENEFIT` com seus sentidos distintos e `PROOF` somente quando houver suporte real. O serializador e a adaptação seguem o fluxo oficial.

Cada ficha explica sua finalidade e aponta módulos complementares. `CAMERA` e `LIGHTING` usam as opções de `CAMERA_AND_PHOTOGRAPHY/`; `STYLE` usa `STYLE_PRESETS/`. `UGC_FORMAT` classifica a peça e `UGC_TEMPLATE` identifica o arco escolhido em `UGC_TEMPLATES/`. `HOOK`, `RETENTION` e `CTA` recebem escolhas de `HOOKS_RETENTION_CTA/`. `VIDEO_PROMPTS/` não é fonte dessas decisões: use-a somente depois dos cards para compor/serializar o material já preenchido. Não copie bibliotecas inteiras para a montagem.

Para compatibilidade, `[IMAGE_OBJECTIVE]` e `[VIDEO_OBJECTIVE]` são aliases contextuais de `[OBJECTIVE]`. `[MODEL_PROFILE]` guarda metadados verificados do modelo; `[MODEL_ADAPTATION]` descreve a transformação da composição para essa interface. `RETENTION` é uma seleção/lista de mecanismos, não métrica de resultado. Consulte `GLOSSARIO_CANONICO.md` para aliases e distinções.

## Sequência operacional

1. Receba produto, objetivo e contexto confirmados; quando houver referência, conclua sua análise e remodelagem antes da seleção narrativa.
2. Para vídeo, receba o template UGC e as escolhas de hook, retenção e CTA; para imagem, omita esses elementos temporais/narrativos.
3. Preencha os componentes aplicáveis sem repetir o conteúdo em campos diferentes.
4. Descreva ações e execução; escolha local, captura e iluminação compatíveis.
5. Selecione mood e preset de estilo coerentes, sem usar ambos para repetir uma instrução.
6. Em vídeo, defina duração e ajuste ação/fala ao tempo disponível.
7. A composição final ocorre em `VIDEO_PROMPTS/` (vídeo) ou `IMAGE_PROMPTS/` (imagem); depois adapte ao modelo verificado.
8. Remova módulos não aplicáveis, placeholders vazios e instruções duplicadas ou conflitantes.

## Montagem dos campos

Use os formulários de vídeo ou imagem em [`PROMPT_ASSEMBLY.md`](../PROMPT_ASSEMBLY.md) como referência única para reunir os campos da montagem final. Esta ficha orienta a seleção e combinação dos cards; não duplica o inventário de campos nem estabelece herança para os templates. Remova campos não aplicáveis e placeholders vazios. `[SCRIPT]` descreve a progressão narrativa; `[DIALOGUE]` contém as palavras exatas. Se forem iguais, mantenha o texto apenas uma vez.

## Exemplo genérico de montagem

Exemplo ilustrativo com produto genérico. Não representa testemunho nem afirma desempenho comprovado.

```text
Produto: organizador compacto para pequenos itens. Preserve sua aparência conforme a referência fornecida.
Objetivo: mostrar visualmente uma etapa de uso em uma situação cotidiana.
Formato UGC: demonstração curta de produto.
Hook: “Quer ver uma forma simples de começar esta organização?”
Roteiro: apresentar o produto, mostrar uma etapa de uso e encerrar convidando o público a consultar os detalhes.
Diálogo: “Veja esta demonstração do organizador compacto e confira os detalhes do produto.”
Ação: colocar pequenos itens dentro do organizador e mostrá-los acomodados.
Câmera: plano médio fixo, com o produto visível sobre a mesa.
Iluminação: luz suave de janela, com sombras discretas.
Local: mesa de trabalho em um ambiente doméstico organizado.
Tom: prático, calmo e informativo.
Estilo: captura casual de smartphone, com acabamento natural.
Duração: aproximadamente 15 segundos.
Adaptação ao modelo: confirmar modelo, versão e campos de entrada; inserir duração e demais parâmetros nos controles próprios quando disponíveis.
```

Antes de gerar, substitua os dados de exemplo pelos dados reais, confirme fatos e capacidades do modelo e retire qualquer campo não aplicável. Não acrescente descrições de aparência ou identidade de pessoas nesta camada.
