# DURATION

**Use quando:** limitar a duração total ou distribuir tempo entre planos de vídeo. Para imagens estáticas, omita este módulo.

**Combine com:** `SCRIPT` para ajustar a quantidade de etapas e `DIALOGUE` para manter a fala dentro do tempo. Não presuma que todo modelo aceite duração como texto; confira `MODEL_ADAPTATION`.

**Bloco reutilizável:**

```text
Duração total: [DURATION]. Distribua o tempo para que cada etapa e fala possam ser compreendidas, sem acelerar artificialmente.
```

**Exemplo preenchido:** `DURATION = aproximadamente 15 segundos`.
