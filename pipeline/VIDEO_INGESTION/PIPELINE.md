# Pipeline e limites de responsabilidade

`VideoInput` -> validacao local ou `Downloader` -> metadados -> `AudioExtractor` -> `Transcriber` opcional -> `Translator` opcional -> `SceneDetector` -> `FrameExtractor` -> `OCRExtractor` -> `IngestionOutput` -> bridge para `REFERENCE_ANALYSIS`.

## Portas desacopladas

As interfaces em `adapters/interfaces.py` recebem tipos do schema e retornam resultados normalizados:

- `Downloader`: URL para caminho local de midia; nao e configurado pelo CLI local.
- `MetadataExtractor`: caminho de video para metadados JSON compativeis.
- `AudioExtractor`: video para audio.
- `Transcriber`: WAV para `TranscriptResult` (estado, metadados e segmentos); provider adapters ficam desacoplados do nucleo.
- `Translator`: segmentos para segmentos traduzidos e temporizados.
- `SceneDetector`: video para cenas com timestamps.
- `FrameExtractor`: video e timestamps para frames.
- `OCRExtractor`: frame para texto associado a timestamp.

## Adapters incluidos

`adapters/ffmpeg.py` inclui `FFprobeMetadataExtractor`, `FFmpegAudioExtractor` (WAV PCM mono 16 kHz) e `FFmpegFrameExtractor` (JPEG nos timestamps recebidos). `adapters/pyscenedetect.py` inclui deteccao opcional de limites com PySceneDetect. `adapters/groq_transcription.py` inclui o adapter Groq, opt-in por ambiente. Os binarios e pacotes Python sao dependencias externas e nunca sao instalados pelo codigo.

O CLI configura metadados, audio, deteccao e frames; Groq e configurado somente com `SOFIA_TRANSCRIPTION_PROVIDER=groq`. Grava `ingestion.json` mais `reference_analysis_seed.json`. O resultado estruturado da transcricao fica em `transcription_result`; os segmentos legados permanecem em `transcript`. A extracao de frames usa o ponto medio de cada cena devolvida pelo detector. Veja `README.md` para configuracao.

## Limites

Capability ausente produz warning e resultado `partial`; erro de adapter e propagado. Transcricao, traducao e OCR ainda nao possuem implementacoes reais. PySceneDetect identifica cortes/limites, nao descreve semanticamente o conteudo. O bridge fornece evidencias candidatas e timestamps com revisao humana pendente, sem inferir intencao, eficacia, viralidade ou identidade.
