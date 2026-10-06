# Workflow de ingestão

1. Validar INPUT com VideoInput. URL é validada sem acesso à rede.
2. Resolver mídia: arquivo local existente ou Downloader fornecido pelo chamador.
3. Extrair áudio com AudioExtractor; ausência deixa execução parcial.
4. Transcrever com Transcriber desacoplado, usando idioma informado quando houver.
5. Traduzir opcionalmente quando houver idioma-alvo e adapter configurado; preservar também a transcrição original.
6. Detectar cenas com SceneDetector e timestamps.
7. Extrair frames nos pontos médios das cenas com FrameExtractor.
8. Executar OCR nos frames extraídos.
9. Serializar tudo em IngestionOutput, mantendo avisos e lacunas.
10. Preparar evidência com to_reference_analysis_payload() para 03_PROMPTS/REFERENCE_ANALYSIS. Os itens ficam pendentes de revisão humana.

As etapas 3–8 são independentes. O pipeline não finge produzir artefatos quando um adapter não está configurado.
