# HOOKS_RETENTION_CTA

Esta camada contém estruturas curtas e combináveis para abrir um vídeo, sustentar a atenção durante seu desenvolvimento e propor uma próxima ação. É independente de modelo e não substitui roteiro, direção, fotografia ou template UGC.

Os nomes canônicos e distinções estão em [`GLOSSARIO_CANONICO.md`](../GLOSSARIO_CANONICO.md). `HOOK` é o conteúdo da abertura; nomes dos arquivos de hooks são tipos/mecanismos. `RETENTION` representa mecanismos selecionados, não uma métrica de desempenho.

No fluxo oficial documentado em [`PROMPT_ASSEMBLY.md`](../PROMPT_ASSEMBLY.md), esta camada vem **depois** da escolha do template UGC e **antes** do preenchimento final dos `MODULE_CARDS/`. Ela encaixa mecanismos no arco existente; não cria outro roteiro.

## Quando usar cada grupo

- **HOOKS:** escolha quando precisar definir a abertura. Use um hook principal por vídeo; os formatos são alternativas, não uma lista para empilhar.
- **RETENTION:** escolha um ou poucos mecanismos quando a sequência precisar de progressão. Retenção organiza informação e expectativa; não significa cortes rápidos ou movimentos artificiais.
- **CTAS:** escolha a ação final que corresponde ao objetivo. Use um CTA principal; um segundo só quando for natural e não concorrer com o primeiro.

## Como combinar com UGC_TEMPLATES

1. Escolha um formato em `UGC_TEMPLATES/VIDEO_TEMPLATES/` conforme o objetivo.
2. Selecione um hook que combine com a primeira etapa desse formato.
3. Escolha mecanismos de retenção que ajudem o desenvolvimento do template e entreguem o que o hook introduziu.
4. Acrescente um CTA compatível com o conteúdo e o destino da publicação.
5. Use `ORCHESTRATION.md` para revisar coerência e evitar redundâncias.

Os templates UGC definem o arco narrativo; estes módulos orientam a abertura, a gestão da expectativa e o fechamento. Consulte `MODULE_CARDS/ORCHESTRATION.md` para combinar produto, ação, câmera, luz e demais módulos sem duplicar conteúdo.

## Independência de modelo

Os blocos são instruções editoriais. Adapte sua representação ao modelo e à versão somente após verificar os campos disponíveis, usando `MODEL_ADAPTATION` e `MODEL_ADAPTERS/`. Nenhum recurso específico de geração é presumido.

## Regras de factualidade e identidade

Não transforme curiosidade em alegação, nem sugira benefício, resultado, avaliação ou experiência não confirmados. Hooks e mecanismos de retenção devem ser pagos pelo próprio conteúdo. Use apenas recursos de CTA realmente disponíveis no canal de publicação. Esta camada não descreve aparência ou identidade de pessoas.

## Índices

### HOOKS

- [01_CURIOSIDADE](HOOKS/01_CURIOSIDADE.md)
- [02_PROBLEMA](HOOKS/02_PROBLEMA.md)
- [03_PERGUNTA](HOOKS/03_PERGUNTA.md)
- [04_DECLARACAO_DIRETA](HOOKS/04_DECLARACAO_DIRETA.md)
- [05_DESCOBERTA](HOOKS/05_DESCOBERTA.md)
- [06_ERRO_COMUM](HOOKS/06_ERRO_COMUM.md)
- [07_CONTRASTE](HOOKS/07_CONTRASTE.md)
- [08_DEMONSTRACAO_IMEDIATA](HOOKS/08_DEMONSTRACAO_IMEDIATA.md)
- [09_PROMESSA_DE_PROCESSO](HOOKS/09_PROMESSA_DE_PROCESSO.md)
- [10_HISTORIA_CURTA](HOOKS/10_HISTORIA_CURTA.md)
- [11_REACAO](HOOKS/11_REACAO.md)
- [12_PADRAO_INTERRUPCAO](HOOKS/12_PADRAO_INTERRUPCAO.md)

### RETENTION

- [01_ABRIR_LOOP](RETENTION/01_ABRIR_LOOP.md)
- [02_REVELACAO_PROGRESSIVA](RETENTION/02_REVELACAO_PROGRESSIVA.md)
- [03_MUDANCA_DE_PLANO](RETENTION/03_MUDANCA_DE_PLANO.md)
- [04_DEMONSTRACAO_EM_ETAPAS](RETENTION/04_DEMONSTRACAO_EM_ETAPAS.md)
- [05_MICRO_CURIOSIDADE](RETENTION/05_MICRO_CURIOSIDADE.md)
- [06_PAGAMENTO_DE_PROMESSA](RETENTION/06_PAGAMENTO_DE_PROMESSA.md)
- [07_CONTRASTE_VISUAL](RETENTION/07_CONTRASTE_VISUAL.md)
- [08_PROGRESSAO](RETENTION/08_PROGRESSAO.md)
- [09_INTERRUPCAO_NATURAL](RETENTION/09_INTERRUPCAO_NATURAL.md)
- [10_FECHAMENTO_DO_LOOP](RETENTION/10_FECHAMENTO_DO_LOOP.md)

### CTAS

- [01_CONHECER_PRODUTO](CTAS/01_CONHECER_PRODUTO.md)
- [02_CONFERIR_DETALHES](CTAS/02_CONFERIR_DETALHES.md)
- [03_VER_OFERTA](CTAS/03_VER_OFERTA.md)
- [04_CONSULTAR_PRODUTO](CTAS/04_CONSULTAR_PRODUTO.md)
- [05_SALVAR_PARA_DEPOIS](CTAS/05_SALVAR_PARA_DEPOIS.md)
- [06_COMENTAR](CTAS/06_COMENTAR.md)
- [07_SEGUIR](CTAS/07_SEGUIR.md)
- [08_COMBINADO](CTAS/08_COMBINADO.md)
