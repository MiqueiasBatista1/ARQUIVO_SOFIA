# SCRIPT

**Use quando:** definir a sequência narrativa da peça. O script determina o que acontece e em que ordem; não substitui a direção física nem os parâmetros de câmera.

`SCRIPT` contém beats e sequência. `DIALOGUE` contém palavras faladas; não são aliases mesmo quando uma peça simples usa o mesmo texto nos dois. Veja [`GLOSSARIO_CANONICO.md`](../GLOSSARIO_CANONICO.md).

**Combine com:** `HOOK` como abertura, `ACTION` para os momentos visuais e `DIALOGUE` quando for necessário especificar as falas. Evite incluir a mesma fala em `[SCRIPT]` e `[DIALOGUE]` duas vezes.

**Bloco reutilizável:**

```text
Roteiro: [SCRIPT]. Organize em abertura, desenvolvimento e encerramento, respeitando [OBJECTIVE] e [DURATION].
```

**Exemplo preenchido:** `SCRIPT = apresentar o produto, mostrar uma etapa de uso e encerrar convidando o público a consultar os detalhes`.
