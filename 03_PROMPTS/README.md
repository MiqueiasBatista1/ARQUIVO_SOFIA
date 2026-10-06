# Biblioteca modular de prompts

Biblioteca reutilizável para criação de imagens e vídeos, com foco em UGC e TikTok Shop. Os módulos podem ser combinados conforme o modelo, a cena e o objetivo de cada peça.

## Estrutura

- `IMAGE_PROMPTS/`: bases de prompts de imagem por formato, contexto e local.
- `VIDEO_PROMPTS/`: estruturas de vídeo por formato narrativo ou demonstração.
- `CAMERA_AND_PHOTOGRAPHY/`: linguagem de enquadramento, câmera, lente, luz e composição.
- `VIDEO_DIRECTION/`: direção de ações, atuação e ritmo diante da câmera.
- `UGC_TEMPLATES/`: componentes e roteiros de conteúdo UGC.
- `HOOKS_RETENTION_CTA/`: estruturas modulares de abertura, progressão de atenção e chamadas para ação.
- `REFERENCE_ANALYSIS/`: método para decompor referências em observações, mecanismos e conceitos originais.
- `STYLE_PRESETS/`: camadas de estilo visual combináveis.
- `PROMPT_ASSEMBLY.md`: contrato de montagem e ordem das camadas.
- `GLOSSARIO_CANONICO.md`: nomes, definições, aliases autorizados e distinções dos campos compartilhados.
- `MODEL_ADAPTERS/README.md`: ficha neutra para adaptar o prompt a cada modelo.
- `MODULE_CARDS/`: fichas práticas para compor módulos reutilizáveis.
- `MODULE_CARDS/ORCHESTRATION.md`: fluxo para selecionar, preencher e combinar fichas.

Cada arquivo de módulo apresenta opções independentes. Escolha uma base, preencha os campos comuns definidos em `PROMPT_ASSEMBLY.md`, acrescente somente os módulos relevantes e remova instruções incompatíveis entre si.

## Convenção de placeholders

Use placeholders em inglês, ASCII, maiúsculos e `SNAKE_CASE`, sempre entre colchetes. Prefira os nomes de `GLOSSARIO_CANONICO.md`, como `[OBJECTIVE]`, `[PRODUCT]`, `[UGC_FORMAT]`, `[UGC_TEMPLATE]`, `[HOOK]`, `[RETENTION]`, `[SCRIPT]`, `[DIALOGUE]`, `[ACTION]`, `[VIDEO_DIRECTION]`, `[SCENE]`, `[LOCATION]`, `[CAMERA]`, `[LIGHTING]`, `[STYLE]`, `[DURATION]`, `[MODEL_PROFILE]`, `[MODEL_ADAPTATION]` e `[CTA]`. `[IMAGE_OBJECTIVE]` e `[VIDEO_OBJECTIVE]` são aliases contextuais documentados. Não use o mesmo identificador para conceitos distintos; por exemplo, `[SCENE]` (situação visual) e `[LOCATION]` (lugar físico) têm sentidos próprios.

Não deixe placeholders sem substituir no prompt enviado ao modelo. Quando uma informação não se aplicar, remova o trecho correspondente. Não junte alternativas/conceitos diferentes dentro de um token com barra; consulte o glossário para tokens compostos legados e exceções ainda pendentes.

## Montagem sugerida

**Imagem:** produto/assunto + objetivo + base de imagem + ação/cena/local + câmera/fotografia + estilo + parâmetros do modelo.

**Vídeo:** produto + objetivo + formato UGC + hook/roteiro + ação/direção + câmera + iluminação + cenário + estilo + diálogo/áudio + perfil do modelo.

Use `PROMPT_ASSEMBLY.md` como ordem de referência e `GLOSSARIO_CANONICO.md` como fonte dos significados dos campos. Um bloco pode ficar vazio ou ser omitido quando não se aplicar; não repita a mesma instrução em camadas diferentes.

Escreva instruções positivas, concretas e observáveis. Descreva o que deve aparecer, acontecer ou ser ouvido. Evite empilhar adjetivos vagos, instruções redundantes ou comandos que se contradizem.

## Adaptar para diferentes modelos

1. Preserve a intenção e os fatos do prompt; adapte a forma, não invente detalhes de produto, pessoa ou marca.
2. Consulte a interface e a documentação atuais do modelo escolhido para saber como informar proporção, duração, resolução, imagem de referência, áudio, seed, negative prompt e demais parâmetros. Os nomes e limites variam por modelo e versão.
3. Separe texto descritivo de parâmetros estruturados quando a ferramenta oferecer campos próprios. Mantenha instruções essenciais no texto se o modelo não oferecer campos dedicados.
4. Para modelos de vídeo, especifique duração, sequência temporal, ação, continuidade, movimento de câmera e áudio/dialogue de forma explícita. Divida em planos quando uma tomada única não for adequada.
5. Para modelos de imagem, priorize sujeito/objeto, ação ou pose, cenário, composição, iluminação e acabamento. Indique proporção e referência visual nos controles próprios quando disponíveis.
6. Preencha uma ficha em `MODEL_ADAPTERS/README.md` para registrar modelo, versão, parâmetros, capacidades verificadas e transformação aplicada. Mantenha a ficha separada do conteúdo-base e não presuma suporte a recursos sem confirmação na interface do modelo.

Os exemplos são bases editoriais independentes de fornecedor. Não presumem suporte a recursos específicos de Veo, Seedance ou qualquer outro modelo.

## Escopo editorial

O roteiro define mensagem e ordem narrativa; a direção define comportamento observável; câmera/fotografia define captura e luz; estilo define acabamento; o perfil do modelo traduz parâmetros e formato de entrada. Consulte os arquivos de montagem para evitar misturar essas responsabilidades.

## Limites desta biblioteca

Esta etapa não define aparência física da Sofia. Não acrescente descrições de rosto, corpo, cabelo ou outros traços físicos dela. Se uma produção futura precisar preservar a identidade, use apenas referências e instruções de identidade aprovadas no fluxo apropriado do projeto; esta biblioteca não substitui a fonte oficial. Não altere a identidade visual oficial por meio de presets.

Para alegações comerciais, depoimentos, comparações e demonstrações, use somente fatos e experiências reais aprovados. Não apresente resultados encenados como prova real nem invente eficácia, avaliações, preços ou características do produto.
