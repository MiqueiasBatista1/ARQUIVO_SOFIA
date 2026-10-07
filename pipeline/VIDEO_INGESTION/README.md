# VIDEO_INGESTION

Camada para receber vídeo local, validar o arquivo, extrair metadados, áudio e frames, detectar limites de cenas e preparar dados para `03_PROMPTS/REFERENCE_ANALYSIS`. A entrada URL continua dependente de um downloader explicitamente configurado; não há download implícito.

## Componentes

- `schemas/`: contratos Python e JSON de entrada, cenas e saída.
- `adapters/interfaces.py`: portas substituíveis de metadados, mídia, cenas, OCR, transcrição e tradução.
- `adapters/ffmpeg.py`: adapters reais isolados para ffprobe, extração de WAV e frames JPEG.
- `adapters/pyscenedetect.py`: detector opcional de cenas via PySceneDetect.
- `adapters/reference_analysis_bridge.py`: cria evidências candidatas com timestamps e revisão humana pendente.
- `extractors/orchestrator.py`: coordena adapters injetados.
- `cli.py`: comando local e persistência dos artefatos.
- `tests/`: testes offline com fakes/mocks.

## Dependências e instalação

Requer Python 3.10+. Para processamento de mídia, instale FFmpeg e ffprobe (geralmente distribuídos juntos) e confirme `ffmpeg -version` e `ffprobe -version` no terminal. PySceneDetect é necessário para detecção de cenas; seu backend OpenCV é opcional no pacote principal e instalado com:

```powershell
python -m pip install "scenedetect[opencv]"
```

Nenhuma ferramenta é instalada pelo código. A transcrição opcional tem um adapter Groq configurado pela interface `Transcriber`; tradução e OCR ainda não têm adapters concretos e não requerem APIs nesta etapa.

## Execução local

Na raiz do repositório, informe o caminho de um vídeo de teste que já exista localmente:

```powershell
python -m pipeline.VIDEO_INGESTION.cli --input ".\video_teste.mp4" --output ".\artifacts"
```

Parâmetros opcionais incluem `--language pt`, `--platform tiktok`, `--ffmpeg CAMINHO`, `--ffprobe CAMINHO` e `--scene-threshold 27`. Este ambiente não contém as ferramentas nem um vídeo teste; o comando emitirá uma mensagem direta se faltar uma dependência.

## Artefatos gerados

Para `video_teste.mp4`, são criados em `artifacts/video_teste/`:

- `audio/video_teste.wav`: áudio mono PCM de 16 kHz;
- `frames/frame_NNNN_T.sss.jpg`: um JPEG no ponto médio de cada cena detectada;
- `ingestion.json`: entrada, metadados normalizados, caminhos, cenas, frames, transcrições quando disponíveis e warnings;
- `reference_analysis_seed.json`: dados enviados pelo bridge como evidências candidatas `PENDING_HUMAN_REVIEW`.

Metadados de mídia têm duração, container, tamanho, bitrate, codec, resolução, taxa de quadros, codec de áudio, sample rate e canais quando disponíveis. Valores ausentes são representados como `null`.

## Limitações atuais

- Sem downloader integrado para URL.
- Transcrição Groq é opcional e só é ativada quando configurada; tradução e OCR ainda não têm adapters concretos.
- PySceneDetect informa limites; não descreve semanticamente cenas. Descrição visual, diálogo, produto e outros campos continuam vazios até análise posterior.
- Frames são amostrados somente nos pontos médios das cenas.
- Resultado `partial` indica etapas não configuradas, não ausência de conteúdo no vídeo.
- O bridge não infere intenção, eficácia, viralidade ou identidade; exige revisão humana.

## Optional Groq transcription

`adapters/groq_transcription.py` implements the provider-neutral `Transcriber` interface using the installed Groq SDK (validated with version 0.37.1). It calls `audio.transcriptions.with_raw_response.create` with `response_format="verbose_json"` and segment timestamp granularity, then reads the raw HTTP JSON so returned timestamps are preserved.

Configure the process environment before invoking the existing CLI:

- `SOFIA_TRANSCRIPTION_PROVIDER=groq` enables the adapter. An unset provider, `none`, or `disabled` leaves transcription disabled.
- `SOFIA_TRANSCRIPTION_MODEL` is required when Groq is enabled. No fallback model is selected.
- `GROQ_API_KEY` must be supplied by the environment or a secrets manager. The pipeline does not log it or write it to the artifact.
- `SOFIA_TRANSCRIPTION_LANGUAGE` is optional. CLI `--language` takes precedence and is sent as a requested language.

The structured `transcription_result` is written to `ingestion.json` with `SUCCESS`, `PARTIAL`, or `ERROR`, metadata, segments, and typed errors. The existing `transcript` segment array remains for compatibility. The bridge emits literal text only as `OBSERVED_DIALOGUE`; it does not create interpretations. Confidence and speaker are carried only when the provider returns them.

Input, configuration, and provider failures are represented by typed error codes and retain the original error message/cause type. Partial results preserve returned text and leave unavailable timestamps null. Tests use fakes and make no external request. Sending audio to Groq occurs only after the provider is explicitly enabled with `SOFIA_TRANSCRIPTION_PROVIDER`.

## Testes

```powershell
python -m unittest discover -s pipeline -p "test_*.py" -v
```

Os testes usam mocks/fakes e não precisam de internet, binários FFmpeg/PySceneDetect nem serviços pagos.
