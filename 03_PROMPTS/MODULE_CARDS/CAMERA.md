# CAMERA

**Use quando:** definir como a cena será capturada: enquadramento, perspectiva e movimento. Selecione uma configuração coerente por plano.

`CAMERA` descreve captura desejada; `OBSERVED_CAMERA`, `OBSERVED_FRAMING` e `OBSERVED_MOVEMENT` descrevem referência e não são aliases. `LIGHTING` e `STYLE` permanecem dimensões separadas. Consulte [`GLOSSARIO_CANONICO.md`](../GLOSSARIO_CANONICO.md).

**Combine com:** `ACTION` para garantir legibilidade; `LIGHTING` para condições de captura e `STYLE` para acabamento. Consulte `CAMERA_AND_PHOTOGRAPHY/` para opções detalhadas; não duplique a descrição técnica aqui.

**Bloco reutilizável:**

```text
Câmera: [CAMERA]. Mantenha o assunto principal e a ação legíveis durante todo o plano.
```

**Exemplo preenchido:** `CAMERA = plano médio fixo, com o produto visível sobre a mesa`.
