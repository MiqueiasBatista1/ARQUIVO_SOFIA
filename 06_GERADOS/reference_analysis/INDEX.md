# Índice — análises de referência

Escopo: quatro vídeos solicitados, com artefatos locais de `06_GERADOS/ingestion_test/batch_transcription` e vídeos de `01_REFERENCIAS`. Os documentos normativos existem em `03_PROMPTS/REFERENCE_ANALYSIS`; o caminho `pipeline/VIDEO_INGESTION/REFERENCE_ANALYSIS` informado não existe. Nenhum prompt, remodelagem para Sofia ou chamada externa foi produzido.

| Vídeo | Duração | Status | Principais mecanismos observados |
| --- | ---: | --- | --- |
| `ssstik.io_@agathabahiense_1791318445882.mp4` | 251,23 s | Concluída com lacunas | Relato pessoal, exemplos em série, pergunta sobre normalização e reflexão final; formato de comentário/reflexão falada. |
| `ssstik.io_@amandarosariomkp_1791318471913.mp4` | 199,40 s | Concluída com lacunas | Tutorial longo por etapas, fala associada à demonstração, ocasião específica, resposta à objeção e resultado final. |
| `ssstik.io_@helenaricci_1791318505769.mp4` | 64,90 s | Concluída com lacunas | Contraste de práticas, demonstração localizada e experiência pessoal com ressalva; formato curto de opinião/demonstração. |
| `ssstik.io_@raecambra2.0_1791318517880.mp4` | 101,80 s | Concluída com lacunas | Rotina demonstrativa em etapas, avaliações pessoais ao longo do processo e close final; formato de rotina/review. |

## Diferenças entre formatos

- Agathabahiense é comentário narrativo/reflexivo sem produto como eixo; progride por exemplos e reflexão (251 s).
- Amandarosariomkp é tutorial sequencial mais longo (199 s), com maquiagem apresentada por etapas; há 84 frames, mas os cortes não foram revisados manualmente.
- Helenaricci é o vídeo mais curto (65 s), sobre diferença de aplicação de pó, com ressalva de que a escolha depende de cada pessoa.
- Raecambra2.0 mostra uma rotina de cerca de 102 s, com comentários pessoais ligados às etapas e fechamento visual próximo do resultado.

## Cobertura e limitações

As quatro transcrições constam como `SUCCESS` em `ingestion.json`; texto e segmentos não existem em arquivos separados com nomes `transcription_result.text`/ `.segments`. Contagens do texto consolidado e segmentos: agatha 3.862 caracteres/88 segmentos; amanda 4.379/76; helena 1.437/21; rae 1.228/23. As contagens de caracteres referem-se a `transcription_result.text`, que pode diferir da concatenação dos segmentos.

Os estados de ingestão estão como `partial` e OCR sem resultados. Frames são esparsos em três vídeos e amostrais, embora numerosos, no tutorial de Amanda. Limites automáticos de cena não equivalem a revisão humana. Assim, edição contínua, pattern interrupts, movimento, estabilidade, gestos ao longo do tempo, texto em tela fora dos stills e CTA visual têm evidência limitada ou não determinado pelos artefatos disponíveis. Transcrições automáticas podem conter erros; alegações dos vídeos foram tratadas como falas observadas, não fatos verificados. Métricas de desempenho não foram fornecidas.

As análises separam `OBSERVAÇÃO` de `INTERPRETAÇÃO`, registram padrões em nível abstrato e identificam elementos particulares a não copiar. Padrões reutilizáveis exigem remodelagem independente e não são instruções diretas de geração.


