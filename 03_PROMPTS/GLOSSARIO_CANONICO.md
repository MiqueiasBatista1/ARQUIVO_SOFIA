# Glossário canônico de campos

Este documento define os nomes e significados compartilhados pela biblioteca `03_PROMPTS`. É a referência normativa para preencher e combinar as camadas. Os valores continuam em linguagem natural quando um campo não exige enumeração. Esta documentação não define identidade de pessoas, não verifica claims automaticamente e não presume capacidades de modelos.

## Regras de uso

- Use o nome canônico como campo de saída nos formulários de montagem.
- Nomes declarados como alias são aceitos durante a migração; preserve-os onde removê-los possa quebrar uma referência existente. Aliases não autorizados não devem ser inferidos pela semelhança dos nomes.
- Campos `OBSERVED_*` pertencem à análise da referência. Eles descrevem material observado e não substituem campos de criação sem uma etapa explícita de remodelagem.
- Um campo opcional pode ser omitido quando não se aplicar. Campo condicional só é obrigatório sob a condição indicada.
- `PROOF` só pode registrar suporte realmente fornecido, observável ou documentado. Não completar fonte, testemunho, qualificação, métrica ou evidência ausente.
- Os campos comuns repetidos nos 15 templates UGC continuam válidos localmente. Este glossário não os torna herança obrigatória; a possibilidade de herdar campos no futuro fica separada desta implementação.

## Campos canônicos

| Nome canônico | Definição | Não significa | Origem normal | Consumidor normal | Obrigatoriedade | Aliases autorizados | Não aliases |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `OBJECTIVE` | Resultado comunicativo pretendido para a peça. Texto curto. | Roteiro, benefício ou CTA. | Briefing; `MODULE_CARDS/OBJECTIVE.md`. | Template e montagem final. | Obrigatório para gerar uma peça. | `IMAGE_OBJECTIVE` ou `VIDEO_OBJECTIVE` quando o escopo de mídia precisar ficar explícito. | `OBSERVED_OBJECTIVE`, que é analítico. |
| `PRODUCT` | Produto específico tratado na peça, com fatos e referências aprovados. Texto descritivo. | Categoria, claim ou qualquer assunto visual. | Briefing/fonte aprovada; `MODULE_CARDS/PRODUCT.md`. | Template, ação e bases de prompt. | Condicional: obrigatório quando a peça trata de um produto. | Nenhum alias geral. | `PRODUCT_CATEGORY`, `SUBJECT`, `COMPARISON_ITEM`. |
| `UGC_FORMAT` | Classe editorial da peça, como demonstração, review ou unboxing. Rótulo/enumeração. | Identificador da ficha narrativa concreta. | Seleção editorial; `MODULE_CARDS/UGC_FORMAT.md`. | Template, cards e montagem. | Condicional: obrigatório quando a peça é UGC. | Nenhum. | `UGC_TEMPLATE`, bases de `VIDEO_PROMPTS/`. |
| `UGC_TEMPLATE` | Identificador do arco narrativo escolhido em `UGC_TEMPLATES/VIDEO_TEMPLATES/`. Referência a uma ficha. | Classe editorial ou prompt audiovisual serializado. | Seleção de template UGC. | `HOOKS_RETENTION_CTA/`, cards e montagem. | Condicional: obrigatório quando se escolhe um template UGC. | Nenhum. | `UGC_FORMAT`. |
| `HOOK` | Conteúdo verbal ou visual escolhido para abrir o vídeo. Texto/instrução. | Categoria do mecanismo de hook ou abertura observada em referência. | `HOOKS_RETENTION_CTA/HOOKS/`; preenchimento editorial. | Template, roteiro e composição de vídeo. | Opcional; condicional quando o arco usa uma abertura explícita. | Nenhum geral. | `OBSERVED_HOOK`, `HOOK_PROMISE`, nomes dos arquivos de mecanismos. |
| `RETENTION` | Lista ordenada de mecanismos selecionados para organizar expectativa/progressão dentro do arco; cada item pode indicar mecanismo e beat-alvo. | Métrica de retenção, duração ou roteiro paralelo. | `HOOKS_RETENTION_CTA/RETENTION/`. | Template e roteiro serializado. | Opcional. | Nenhum. | `OBSERVED_RETENTION`, `DURATION`, `SCRIPT`. |
| `BENEFIT` | Benefício possível apresentado como ideia editorial ainda não validada. Texto de benefício. | Claim verificado, característica ou evidência. | Ideação/editorial, sujeito a validação antes de ser apresentado como fato. | Roteiro e avaliação factual. | Opcional; não pode ser publicado como afirmação factual sem validação. | Nenhum. | `VERIFIED_BENEFIT`, `VERIFIED_FEATURE`, `PROOF`. |
| `VERIFIED_BENEFIT` | Benefício específico confirmado por informação aprovada e utilizável na peça. Texto de claim. | `BENEFIT` não validado, característica isolada ou evidência. | Dados aprovados de produto e validação editorial. | Roteiro, recomendação e venda direta. | Condicional quando a peça fizer claim de benefício; requer suporte aplicável. | Nenhum. | `BENEFIT`, `VERIFIED_FEATURE`, `PROOF`. |
| `PROOF` | Registro estruturado de suporte para um claim, sem elevar o suporte além do que demonstra. Objeto com `CLAIM`, `EVIDENCE_TYPE` e, conforme aplicável, `DATA_SOURCE`, `SOURCE_QUALIFICATION`, `EVIDENCE_LOCATOR` e `TESTIMONIAL`. | O claim em si, uma evidência inventada ou uma garantia de eficácia universal. | Fonte documentada, demonstração/observação realmente disponível ou relato real autorizado. | Validação do claim e roteiro/template. | Condicional: necessário quando a peça usar claim que exija suporte. | Nenhum alias existente. | `TESTIMONIAL`, `DATA_SOURCE`, `SOURCE_QUALIFICATION`, `ACTION`. São componentes ou tipos de suporte, não o registro completo. |
| `SCRIPT` | Beats narrativos ordenados: o que acontece e em que sequência. Texto ou lista ordenada. | Palavras exatas da fala ou execução gestual detalhada. | Template UGC e `MODULE_CARDS/SCRIPT.md`. | `DIALOGUE`, `ACTION`, `VIDEO_DIRECTION` e serialização. | Condicional: necessário para arco/etapas; pode ser omitido em peça de ação única. | Nenhum. | `DIALOGUE`, `OBSERVED_SCRIPT`, `VIDEO_DIRECTION`. |
| `DIALOGUE` | Palavras exatas para fala ou narração. Texto. | Sequência narrativa completa ou orientação de atuação. | Roteiro/fala aprovada e `MODULE_CARDS/DIALOGUE.md`. | `VIDEO_DIRECTION` e composição de vídeo. | Condicional: obrigatório se houver fala/narração. | Nenhum. | `SCRIPT`, `OBSERVED_DIALOGUE`, `AUDIO`. |
| `ACTION` | O que acontece visivelmente no quadro ou sequência. Texto/lista observável. | Como executar o gesto, movimento de câmera ou ação observada numa referência. | Template, roteiro ou `MODULE_CARDS/ACTION.md`. | `VIDEO_DIRECTION`, fotografia e prompt-base. | Condicional: obrigatório quando há ação visual relevante. | Nenhum. | `OBSERVED_ACTION`, `VIDEO_DIRECTION`, `CAMERA`. |
| `VIDEO_DIRECTION` | Como ação e atuação se executam no tempo: gestos, pausas, expressão, ritmo e continuidade. Instrução ou sequência. | A ação narrativa, o roteiro, a captura ou o estilo. | `VIDEO_DIRECTION/`. | Composição/serialização de vídeo. | Condicional: usar quando há execução temporal, atuação ou continuidade relevante. | Nenhum. | `ACTION`, `SCRIPT`, `CAMERA`, `STYLE`. |
| `SCENE` | Situação visual a representar, incluindo estado e relações entre elementos no quadro. Texto. | Lugar físico ou arco narrativo inteiro. | Briefing/cards/base visual. | `IMAGE_PROMPTS/`, fotografia e montagem. | Condicional quando não puder ser compreendida pelos demais campos. | Nenhum. | `LOCATION`, `CONTEXT`, `ACTION`. |
| `LOCATION` | Lugar físico da cena. Texto/local. | Situação visual, atividade ou contexto narrativo. | Briefing/cards. | Template e base de imagem/vídeo. | Opcional; condicional quando o lugar afeta leitura ou plausibilidade. | `ROOM/AREA` e `SINK/COUNTER/OTHER_AREA` somente como aliases legados para especificar o local/área física. | `SCENE`, `CONTEXT`. |
| `CAMERA` | Configuração desejada de captura por plano, incluindo enquadramento, perspectiva/efeito de lente e movimento de câmera. Texto descritivo. | Luz, atuação corporal ou observação de câmera em referência. | `CAMERA_AND_PHOTOGRAPHY/`. | Base de imagem/vídeo. | Opcional; condicional quando a captura altera legibilidade/intenção. | Nenhum. | `OBSERVED_CAMERA`, `OBSERVED_FRAMING`, `OBSERVED_MOVEMENT`, `LIGHTING`. |
| `LIGHTING` | Condição desejada de luz: qualidade, direção e fonte quando pertinente. Texto/seleção. | Acabamento visual completo ou câmera. | `CAMERA_AND_PHOTOGRAPHY/`. | Base de imagem/vídeo. | Opcional; condicional quando a luz afeta a leitura. | Nenhum. | `OBSERVED_LIGHTING`, `STYLE`, `CAMERA`. |
| `STYLE` | Acabamento/estética visual selecionada, preferencialmente por referência a um preset. Valor de preset/instrução curta. | Mood, identidade, iluminação ou captura. | `STYLE_PRESETS/`. | Base de imagem/vídeo. | Opcional; no máximo um preset principal por peça/plano, conforme documentação existente. | Nomes de presets são valores permitidos, não aliases do campo. | `MOOD`, `CAMERA`, `LIGHTING`, `VIDEO_DIRECTION`. |
| `DURATION` | Tempo editorial pretendido para o vídeo; pode ser total ou distribuído por planos. Texto ou lista temporal. | Parâmetro técnico de uma interface ou período de uso/comparação. | Briefing/card de duração. | Roteiro, direção e serializador de vídeo. | Condicional: obrigatória quando houver limite editorial/de plataforma ou plano temporal. | Nenhum. | `DURATION_PARAMETER`, `TIMEFRAME`, `PACE`. |
| `MODEL_PROFILE` | Objeto de dados verificados da configuração escolhida: nome, versão, tarefa/modalidade, capacidades e parâmetros suportados. | Transformação do prompt ou promessa sobre capacidades não verificadas. | `MODEL_ADAPTERS/` após verificação da interface. | `MODEL_ADAPTATION` e etapa de geração. | Condicional: necessário quando a peça for adaptada a um modelo específico. | `MODEL_NAME` e `MODEL_VERSION` são subcampos, não aliases integrais. | `MODEL_ADAPTATION`, `PROMPT_TRANSFORM`, `INPUT_MODE` como objeto inteiro. |
| `MODEL_ADAPTATION` | Transformação da composição para a entrada/campos verificados do modelo, preservando intenção editorial. Texto ou lista de transformações. | Perfil/capacidades do modelo ou reescrita da intenção. | Processo de adaptação com base em `MODEL_PROFILE`. | Serializador e interface do modelo. | Condicional: necessária antes da geração num modelo específico. | `PROMPT_TRANSFORM` apenas quando designar as transformações aplicadas à composição. | `MODEL_PROFILE`, `PROMPT_STRUCTURE`, `INPUT_MODE`, `INPUT_MODALITY`. |
| `CTA` | Próxima ação solicitada ao público, ajustada ao conteúdo e destino disponíveis. Texto/instrução. | Destino, objetivo ou categoria do CTA. | `HOOKS_RETENTION_CTA/CTAS/`. | Template e composição do vídeo. | Opcional em geral; condicional quando o template/objetivo exigir ação final. | `PRIMARY_CTA` e `SECONDARY_CTA` são subcampos somente no caso combinado. | `DESTINATION`, `OBJECTIVE`, nomes de arquivos de CTA. |
| `DATA_SOURCE` | Fonte documental/dados específica que sustenta informação ou comparação. Referência. | Qualificação da fonte ou evidência em geral. | Registro/fonte aprovada. | `PROOF`, comparação e claims quantitativos. | Condicional quando dados ou números forem usados. | Nenhum. | `SOURCE_QUALIFICATION`, `EVIDENCE_SOURCE`, `TESTIMONIAL`. |
| `SOURCE_QUALIFICATION` | Condições e limites necessários para interpretar a fonte: escopo, período, população, método ou ressalvas. Texto/objeto. | A fonte original, claim ou depoimento. | Revisão da fonte e do claim. | `PROOF`, benefício e comparação. | Condicional quando a interpretação exigir condições/limites. | Nenhum. | `DATA_SOURCE`, `EVIDENCE_LOCATOR`, `LIMITATIONS`. |
| `TESTIMONIAL` | Relato autêntico e autorizado de experiência de uma pessoa, preservado em sentido e contexto. Texto/fonte de relato. | Qualquer diálogo, claim universal ou prova automática de eficácia. | Relator real autorizado; registro editorial fiel. | Template de testemunho/review; `PROOF` quando aplicável. | Condicional: obrigatório somente quando a peça se apresenta como testemunho. | Nenhum. | `PROOF`, `DIALOGUE`, `OBSERVATIONS`, `EXPERIENCE`. |

## Campos de análise de referência

Campos analíticos mantêm prefixos e distinções explícitas. Não são aliases dos campos de criação.

| Família analítica | Campos existentes | Significado |
| --- | --- | --- |
| Observação | `OBSERVED_OBJECTIVE`, `OBSERVED_HOOK`, `OBSERVED_RETENTION`, `OBSERVED_SCRIPT`, `OBSERVED_DIALOGUE`, `OBSERVED_ACTION`, `OBSERVED_PRODUCT_DEMO`, `OBSERVED_CAMERA`, `OBSERVED_FRAMING`, `OBSERVED_MOVEMENT`, `OBSERVED_LIGHTING`, `OBSERVED_ENVIRONMENT`, `OBSERVED_PACING`, `OBSERVED_CTA` | O que o material de referência declara ou permite observar; registrar evidência/localizador e lacunas. |
| Interpretação/hipótese | `INTERPRETED_MECHANISM`, `HYPOTHESIS`, `CONFIDENCE_LEVEL`, `HYPOTHESES_TO_TEST`, `VARIABLE`, `COMPARISON`, `SUCCESS_CRITERION` | Leitura ou teste futuro, nunca fato observado por inferência silenciosa. |
| Proveniência/registro | `REFERENCE_CONTEXT`, `EVIDENCE_LOCATOR`, `EVIDENCE_SOURCE`, `EVIDENCE_CLASS`, `FIELD_NAME`, `FIELD_CONTENT`, `UNKNOWN_OR_MISSING` | Contexto, origem/localizador da evidência, classe e lacunas do registro. |
| Remodelagem | `REUSABLE_PATTERNS`, `NON_COPYABLE_ELEMENTS`, `REMODELING_OPPORTUNITIES` | Abstração e substituição necessárias para criar conceito novo. |

## Aliases e termos que permanecem distintos

Aliases são compatibilidade nominal limitada ao contexto indicado, não autorização para misturar valores ou significados.

| Nome atual | Tratamento | Escopo/motivo |
| --- | --- | --- |
| `IMAGE_OBJECTIVE` | Alias de `OBJECTIVE` | Objetivo da peça de imagem em documentos legados. |
| `VIDEO_OBJECTIVE` | Alias de `OBJECTIVE` | Objetivo da peça de vídeo em documentos legados. |
| `PROMPT_TRANSFORM` | Alias limitado de `MODEL_ADAPTATION` | Somente a lista de transformações realizadas no prompt; não o perfil do modelo. |
| `ROOM/AREA` | Alias contextual de `LOCATION` durante migração | Somente quando indica a área/local físico, não uma categoria de ambiente. |
| `SINK/COUNTER/OTHER_AREA` | Alias contextual de `LOCATION` durante migração | Somente quando indica a área física onde a cena do banheiro ocorre. |
| `VERIFIED_BENEFIT` | **Não alias** de `BENEFIT` | Claim verificado, distinto de ideia/benefício ainda não validado. |
| `UGC_FORMAT` / `UGC_TEMPLATE` | **Não aliases** | Classe editorial versus ficha/arco selecionado. |
| `SCRIPT` / `DIALOGUE` | **Não aliases** | Beats narrativos versus fala literal. |
| `ACTION` / `VIDEO_DIRECTION` | **Não aliases** | O que acontece versus como se executa temporalmente. |
| `SCENE` / `LOCATION` | **Não aliases** | Situação visual versus lugar físico. |
| `MODEL_PROFILE` / `MODEL_ADAPTATION` | **Não aliases** | Dados verificados versus transformação da entrada. |
| `PROOF` / `TESTIMONIAL` | **Não aliases** | Registro de suporte estruturado versus uma forma possível de relato. |
| `STYLE` / `MOOD` | **Não aliases** | Acabamento visual versus tom emocional. |
| `DURATION` / `DURATION_PARAMETER` | **Não aliases** | Tempo editorial versus controle de interface. |
| `DURATION` / `TIMEFRAME` | **Não aliases** | Duração da peça versus período de uso/teste/comparação. |
| `DATA_SOURCE` / `SOURCE_QUALIFICATION` | **Não aliases** | Fonte versus condições/limites para interpretá-la. |
| `PRODUCT` / `SUBJECT` / `PRODUCT_CATEGORY` | **Não aliases** | Produto concreto, foco visual e classe do produto. |
| `CTA` / `DESTINATION` | **Não aliases** | Ação pedida versus local onde ela ocorre. |

`INPUT_MODE` e `INPUT_MODALITY` continuam separados até que o schema de análise e o de perfil de modelo sejam harmonizados. `PROMPT_STRUCTURE` também não é alias automático de `MODEL_ADAPTATION`.

## Proveniência e permissão de consumo

Proveniência acompanha cada observação, claim, evidência ou decisão relevante da origem até o prompt final. Ela é metadado de rastreabilidade; não vira automaticamente texto de geração. Na análise de referência, use o registro por achado abaixo. Nas outras camadas, carregue/adapte os mesmos dados junto do componente ao qual se referem, sem substituir sua fonte por uma cópia sem origem.

| Metadado | Significado e preenchimento |
| --- | --- |
| `source_type` | Tipo real da origem, em texto: por exemplo `reference_material`, `user_brief`, `approved_product_source`, `authorized_testimonial` ou `model_documentation`. Os exemplos não formam uma lista fechada nem validam a fonte. |
| `source_id` | Identificador existente da fonte, quando disponível. Para referência, use o identificador que integra `REFERENCE_CONTEXT`; não invente ID. Se não houver identificador, registre a lacuna existente (`UNKNOWN_OR_MISSING`). |
| `origin_stage` | Etapa/camada onde o valor entrou ou foi produzido, usando os nomes reais do fluxo, por exemplo `INPUT`, `REFERENCE_ANALYSIS`, `UGC_TEMPLATES`, `HOOKS_RETENTION_CTA`, `MODULE_CARDS`, `VIDEO_DIRECTION`, `CAMERA_AND_PHOTOGRAPHY`, `STYLE_PRESETS`, `VIDEO_PROMPTS`, `IMAGE_PROMPTS` ou `MODEL_ADAPTER`. |
| `evidence_status` | Para achados de `REFERENCE_ANALYSIS`, reutilize `EVIDENCE_CLASS` e seus valores existentes (`OBSERVADO`, `INTERPRETADO`, `HIPOTESE`, `REUTILIZAVEL`, `NAO_COPIAR`). Para conteúdo que não seja achado/evidência, marque como não aplicável em texto; não rotule um claim como `OBSERVADO` só porque ele foi ouvido numa referência. |
| `confidence_level` | Reutilize `CONFIDENCE_LEVEL` apenas para interpretações quando houver base para avaliar confiança. Não use confiança para validar claim, fonte ou benefício. |
| `allowed_consumers` | Camadas autorizadas a receber o valor conforme a tabela de dependências abaixo. Liste consumidores por camada, não por preferência do redator. |
| `generation_input` | `yes`, `no` ou `conditional`, conforme a tabela abaixo. Este metadado não é um controle de modelo e não transforma conteúdo em evidência. |

### Regras de elegibilidade para geração

| Classe/estado do conteúdo | Consumidores permitidos | Pode virar entrada de geração? |
| --- | --- | --- |
| Observação bruta (`OBSERVADO`) de referência | `REFERENCE_ANALYSIS` e revisão de evidência | **Não** diretamente. Só fatos novos verificados independentemente podem entrar como fatos; padrões abstratos podem inspirar uma decisão após remodelagem. |
| Interpretação (`INTERPRETADO`) | `REFERENCE_ANALYSIS`, análise/revisão editorial | **Não** como fato, claim ou instrução. Pode motivar padrão ou decisão nova explicitamente remodelada. |
| Hipótese (`HIPOTESE`) | Planejamento de teste e comparação | **Não** como afirmação factual. Pode orientar uma variável experimental nova, identificada como tal. |
| Padrão reutilizável (`REUTILIZAVEL`) | Seleção editorial de template/hook/estrutura, após remodelagem | **Condicional**: somente a regra abstrata, reescrita para outro contexto e sem sinais/ativos/claims da referência. |
| Item não copiável (`NAO_COPIAR`) | Revisão para evitar reutilização | **Não**. |
| Briefing ou decisão editorial nova | `MODULE_CARDS` e camadas de composição indicadas no fluxo | **Condicional**: sim quando a informação é pertinente e não contradiz restrições ou fatos aprovados. |
| Fato/claim de produto aprovado | `MODULE_CARDS`, `UGC_TEMPLATES`, `HOOKS_RETENTION_CTA`, prompts-base e composição | **Condicional**: claim factual só entra no escopo exato sustentado por fonte e qualificação adequadas. |
| `BENEFIT` | Ideação/editorial e validação | **Não** como afirmação factual até validação; não equivale a `VERIFIED_BENEFIT`. |
| `VERIFIED_BENEFIT` com `PROOF` adequado | Roteiro/template e composição | **Sim**, restrito ao claim, escopo, fonte e condições registrados. |
| `TESTIMONIAL` autorizado | Template de testemunho/review e composição | **Condicional**: somente o relato real, autorizado e contextualizado; não generalizar nem completar. |
| `MODEL_PROFILE` | `MODEL_ADAPTER` | **Não** como conteúdo editorial. Capacidades/parâmetros verificados só informam a adaptação técnica. |
| `MODEL_ADAPTATION` | `MODEL_ADAPTER`/serialização final | **Sim**, como transformação de formato, preservando conteúdo e proveniência. |

## Dependências e passagem entre camadas

Estas dependências especificam tipos de informação permitidos; não alteram a ordem oficial de `PROMPT_ASSEMBLY.md`.

| Camada consumidora | Recebe | Não deve promover ou fazer |
| --- | --- | --- |
| `REFERENCE_ANALYSIS/` | Referência autorizada, identificável e acessível; fatos de contexto fornecidos. | Transformar fala/claim observado em fato confirmado; inferir métrica/eficácia ou aparência/identidade. |
| Briefing e decisões editoriais | Fatos aprovados e, quando houver, padrões abstratos remodelados. | Importar observações, interpretações ou hipóteses como fatos/claims. |
| `UGC_TEMPLATES/` | `OBJECTIVE`, formato/template, contexto novo e dados de produto elegíveis. | Herdar automaticamente claims ou eventos da referência. |
| `HOOKS_RETENTION_CTA/` | Arco UGC e objetivo; padrões remodelados e fatos aprovados pertinentes. | Reutilizar hook/CTA/alegação da referência como texto novo sem revisão. |
| `MODULE_CARDS/` | Valores já qualificados para objetivo, produto, ação, roteiro e campos visuais. | Criar proveniência ausente ou elevar `BENEFIT` a `VERIFIED_BENEFIT`. |
| `VIDEO_DIRECTION/` | Ações/diálogo selecionados e aprovados para a nova peça. | Converter observação de atuação da referência em instrução de cópia. |
| `CAMERA_AND_PHOTOGRAPHY/`, `STYLE_PRESETS/` | Decisões visuais novas ou padrões abstratos remodelados. | Preservar composição/ativos distintivos da referência por default. |
| `VIDEO_PROMPTS/`, `IMAGE_PROMPTS/` | Apenas decisões criativas elegíveis das camadas anteriores. | Receber observação/interpretação/hipótese bruta como fato; inventar claims, fontes ou suporte. |
| `MODEL_ADAPTERS/` | Prompt composto elegível, `MODEL_PROFILE` verificado e parâmetros disponíveis. | Alterar fonte, status, confiança, escopo ou autorização de qualquer conteúdo. |

Os componentes podem ser **fornecidos diretamente** no input, **observacionais** na análise, **interpretados** a partir de observações, **derivados** por uma decisão editorial/remodelagem, ou **verificados** por fonte/aprovação. Preserve a categoria e a ligação de proveniência durante toda a composição. “Herdado” significa apenas que um campo comum se repete entre templates; não muda sua origem nem sua classe, e não estabelece herança obrigatória.

## Estrutura de `PROOF`

Use apenas quando há suporte existente. A estrutura registra a relação entre claim e evidência; não produz nem inventa evidência.

```yaml
claim: "[CLAIM]"
evidence_type: "[EVIDENCE_TYPE]"
data_source: "[DATA_SOURCE]" # quando o suporte vier de dados/documento
source_qualification: "[SOURCE_QUALIFICATION]" # quando houver condições/limites
evidence_locator: "[EVIDENCE_LOCATOR]" # quando o suporte observado estiver localizado numa referência
testimonial: "[TESTIMONIAL]" # somente relato real e autorizado, se aplicável
```

`CLAIM` identifica uma afirmação já proposta. `EVIDENCE_TYPE` descreve a forma real do suporte — dado documentado, demonstração observável ou testemunho autorizado —, mas esses valores não atestam validade. O campo irrelevante deve ser omitido. Se não houver fonte/suporte disponível, registre a lacuna no processo de análise; não preencha o objeto com suposições. `VERIFIED_BENEFIT` só deve ser usado quando o suporte sustentar aquele benefício específico e seu escopo.

`SOURCE_QUALIFICATION` deve declarar quando a fonte é insuficiente, indireta, não verificada ou inadequada para o claim. Em qualquer desses casos, o suporte não autoriza `VERIFIED_BENEFIT` nem geração do claim como fato. Um registro em `REFERENCE_ANALYSIS` é origem/localizador de observação, não prova automática de claim de produto.

## Placeholders com alternativas misturadas

Não use barra para esconder alternativas dentro de um token. Para casos com destinos conhecidos, use o campo canônico apropriado; onde a responsabilidade não estiver resolvida, mantenha o token legado documentado até decisão específica.

| Placeholder atual | Tratamento nesta etapa | Motivo |
| --- | --- | --- |
| `[ACTION/DEMONSTRATION]` | Usar `[ACTION]`; “demonstração” é o contexto/forma narrativa, não alias de ação. | Uma ação pode ocorrer sem formato de demonstração e vice-versa. |
| `[ROOM/AREA]` | Normalizado para `[LOCATION]`; alias contextual legado registrado acima. | O contexto da imagem já descreve casa; o campo especifica o local/área física. |
| `[TYPE/SETTING]` | Preservar por enquanto e reportar pendente. | Tipo de restaurante e setting físico podem ser dimensões diferentes; não há campo aprovado para a primeira. |
| `[SINK/COUNTER/OTHER_AREA]` | Normalizado para `[LOCATION]`; alias contextual legado registrado acima. | Neste prompt, o campo escolhe a área física do banheiro onde ocorre a rotina. |
| `[MOMENT/ROUTINE]` | Preservar por enquanto e reportar pendente. | Momento e sequência de rotina têm responsabilidades diferentes. |
| `[DETAIL/EXPRESSION]` | Separar como `[DETAIL]` e `[EXPRESSION]`, usar somente o aplicável. | Detalhe de produto e expressão do assunto visual são focos diferentes. |
| `[SUBJECT/PRODUCT]` | Usar `[SUBJECT]` para o foco do enquadramento; quando for um produto, preencher o foco com o produto sem declarar os campos como aliases. | `PRODUCT` permanece entidade comercial e `SUBJECT` papel visual. |
| `[SUBJECT/PRODUCT_DETAIL]` | Usar `[SUBJECT]` ou `[PRODUCT_DETAIL]` conforme o foco real; não preencher ambos automaticamente. | Assunto visual e detalhe de produto podem ser alvos distintos. |
| `[FIT/LIMITATION]` | Preservar e reportar pendente. | Adequação ao público e limitação do produto são conceitos diferentes; `PRODUCT_FIT` não foi aprovado como campo. |

## Herança futura

Campos comuns podem futuramente ser herdados por templates a partir de um formulário-base, mas nesta versão os templates mantêm seus campos `necessários`, `opcionais` e suas listas locais. A herança não é requisito desta biblioteca até uma decisão posterior.
