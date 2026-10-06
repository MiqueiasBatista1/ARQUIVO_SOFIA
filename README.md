# SOFIA_AI

Repositório para organizar referências, preservar a identidade aprovada da Sofia e apoiar a produção de conteúdo. A identidade oficial permanece em 02_IDENTITY/IDENTIDADE_OFICIAL.md; esta etapa não a altera nem a finaliza.

## Estrutura do projeto

- 01_REFERENCIAS/: materiais de referência originais.
- 02_IDENTITY/: documentação oficial de identidade.
- 03_PROMPTS/: biblioteca modular de criação e análise.
- 04_FOTOGRAFIA/: materiais e orientações de fotografia.
- 05_CENAS/: definições e materiais de cenas.
- 06_GERADOS/: artefatos gerados durante a produção.
- 07_VERSOES/: revisões e histórico de materiais.
- pipeline/: contratos e módulos técnicos para ingestão e remodelagem de referências audiovisuais.

## Fluxo de referência para conteúdo

VIDEO/URL
→ VIDEO_INGESTION
→ TRANSCRIÇÃO / TRADUÇÃO / FRAMES / CENAS / OCR (quando adapters estiverem conectados)
→ REFERENCE_ANALYSIS
→ EXTRAÇÃO DE PADRÕES
→ REFERENCE_TO_UGC
→ UGC_TEMPLATES
→ MODULE_CARDS
→ PROMPT FINAL

Os módulos técnicos em pipeline/ definem schemas, interfaces e bridges. Não incluem provedores de mídia nem APIs pagas. As camadas editoriais correspondentes ficam em 03_PROMPTS/.

## Etapas e responsabilidades

- **Ingestão:** valida uma entrada local ou URL e coordena adapters substituíveis para extração. Não é análise criativa.
- **Observação:** registra sinais de mídia com fonte e timestamp; extrações automatizadas ficam pendentes de revisão.
- **Análise:** classifica evidências, interpretações, padrões e hipóteses usando 03_PROMPTS/REFERENCE_ANALYSIS/.
- **Remodelagem:** converte mecanismos abstratos em um conceito original, descartando elementos distintivos da referência.
- **Geração:** combina o conceito com templates e fichas para compor um prompt final. Esta etapa não é executada automaticamente pelo pipeline implementado.

## Testes

Com Python 3.10 ou superior, execute na raiz:

    python -m unittest discover -s pipeline -v

Os testes usam a biblioteca padrão e não acessam rede nem serviços externos.
