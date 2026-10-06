# Output schema

O contrato JSON esta em `schemas/ingestion_output.schema.json`; cenas seguem `schemas/scene.schema.json`. Classes Python: `IngestionOutput`, `Scene`, `TranscriptSegment`, `TranscriptResult`, `TranscriptError`, `ExtractedFrame` e `OCRResult`. `transcript` conserva os segmentos normalizados; `transcription_result` inclui estado, idioma, provider, modelo, audio de origem e erro tipado.

## Resultado do pipeline

`IngestionOutput` inclui `source`, estado `complete`/`partial`, `resolved_media_path`, `media_metadata`, caminho do audio, transcricao original e traduzida, frames, cenas, OCR e warnings. `media_metadata` e um objeto JSON normalizado pelo adapter de ffprobe com container, duracao, tamanho, bitrate e propriedades de streams disponiveis. Os dados sao preservados em `source_context.media_metadata` pelo bridge para `REFERENCE_ANALYSIS`, sem criar observacoes analiticas.

Arrays vazios e warnings representam etapas nao executadas; nao sao evidencia de ausencia no video.

## Cena

Campos temporais obrigatorios: `start_seconds` e `end_seconds`, com inicio nao negativo e fim posterior ao inicio. Campos opcionais: `visual_description`, `main_action`, `person_character`, `product`, `environment`, `framing`, `camera_movement`, `on_screen_text`, `speech`, `audio_music`, `cta`, `perceived_emotion` e `observations`.

`person_character` aceita somente rotulo de papel/presenca nao identificador; nao e campo de aparencia. `perceived_emotion` e interpretacao e requer revisao.

Cada observacao exportada pelo bridge preserva origem, timestamp e `PENDING_HUMAN_REVIEW`.
