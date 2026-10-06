# IMAGE_PROMPTS

Bases de imagem. Combine uma base abaixo com `[SCENE]`, `[ACTION]`, `[LOCATION]`, `[OUTFIT]`, `[LIGHTING]`, `[CAMERA]`, `[STYLE]` e `[MOOD]` conforme necessário. Substitua ou remova os campos não aplicáveis. As bases não definem características físicas de uma pessoa específica.

Os nomes e significados estão em [`GLOSSARIO_CANONICO.md`](../GLOSSARIO_CANONICO.md). `SCENE` descreve a situação visual e `LOCATION` o lugar. `STYLE` é acabamento visual; `MOOD` é tom emocional. `PRODUCT` e `SUBJECT` mantêm papéis diferentes.

O fluxo oficial de imagem está em [`PROMPT_ASSEMBLY.md`](../PROMPT_ASSEMBLY.md). Use estas bases depois de decidir objetivo/contexto e preencher os `MODULE_CARDS/` aplicáveis; elas compõem/serializam o conteúdo visual. Complete captura em `CAMERA_AND_PHOTOGRAPHY/` e acabamento em `STYLE_PRESETS/`, sem repetir as escolhas que a base já expressa. Imagem representa um estado estático: não inclua duração, diálogo, continuidade ou movimento temporal.

## Proveniência no prompt composto

Receba somente decisões criativas elegíveis e informações de produto qualificadas. Não transforme observação, interpretação, hipótese ou claim visto/ouvido em referência em fato visual ou afirmação sobre o produto. Não invente selo, resultado, claim, `PROOF` ou fonte. Para qualquer benefício ou claim factual representado, use apenas informação aprovada no escopo sustentado; mantenha `SOURCE_QUALIFICATION` e demais vínculos de proveniência acompanhando a composição. Consulte [`GLOSSARIO_CANONICO.md`](../GLOSSARIO_CANONICO.md).

## Formato e intenção

### Selfie
```text
Fotografia em formato selfie de [SUBJECT] em [LOCATION], registrando [ACTION]. Câmera próxima, perspectiva coerente com um braço segurando o celular, composição espontânea e contexto visível ao redor. [LIGHTING]. Clima [MOOD].
```

### Lifestyle
```text
Imagem lifestyle de [SUBJECT] usando ou interagindo com [PRODUCT] durante [ACTIVITY] em [LOCATION]. Priorize uma situação verossímil, detalhes ambientais úteis e gesto natural. [CAMERA], [LIGHTING], clima [MOOD].
```

### Beauty
```text
Imagem editorial de beleza mostrando [PRODUCT] ou [BEAUTY_ROUTINE] em contexto [SCENE]. Valorize a aplicação ou o detalhe relevante de forma clara, com luz [LIGHTING], enquadramento [CAMERA], acabamento [STYLE] e mood [MOOD]. Preserve textura e aparência realistas; não acrescente alegações visuais de resultado.
```

### Fashion
```text
Imagem de moda apresentando [OUTFIT] em [LOCATION]. Mostre caimento, material e detalhes importantes por meio de [ACTION] e [CAMERA]. Iluminação [LIGHTING], acabamento [STYLE], mood [MOOD].
```

### Product
```text
Imagem de produto de [PRODUCT] em [SCENE]. Mantenha embalagem, rótulos e características visíveis conforme a referência fornecida; destaque [PRODUCT_DETAIL] com composição [COMPOSITION] e iluminação [LIGHTING]. Não invente texto, selo, acessório ou especificação.
```

### UGC
```text
Imagem com linguagem UGC de [SUBJECT] compartilhando [PRODUCT] em [LOCATION]. Enquadramento simples de celular, contexto cotidiano identificável e apresentação espontânea. [ACTION], [LIGHTING], clima [MOOD]. Evite aparência de anúncio de estúdio, salvo se solicitada.
```

## Locais e situações

### Praia
```text
Cena em praia em [TIME_OF_DAY], com [SUBJECT] realizando [ACTION] e [PRODUCT] integrado de forma plausível ao contexto. Luz ambiente [LIGHTING], composição [CAMERA], clima [MOOD]. Respeite o uso seguro e realista do produto no ambiente.
```

### Casa
```text
Cena doméstica em [LOCATION], mostrando [SUBJECT] realizando [ACTION] com [PRODUCT]. Inclua sinais de uso cotidiano sem desordem distrativa. [LIGHTING], [CAMERA], clima [MOOD].
```

### Rua
```text
Cena urbana em [LOCATION], com [SUBJECT] realizando [ACTION]. Integre [PRODUCT] à atividade sem bloquear a leitura da cena. Luz disponível [LIGHTING], enquadramento [CAMERA], clima [MOOD].
```

### Restaurante
```text
Cena em restaurante [TYPE/SETTING], registrando [SUBJECT] em [ACTION]. Posicione [PRODUCT] de forma coerente com o momento. Preserve ambiente e comida plausíveis, luz [LIGHTING], composição [CAMERA], clima [MOOD].
```

### Banheiro
```text
Cena de rotina no banheiro, em [LOCATION], mostrando [ACTION] com [PRODUCT]. Mantenha superfícies e reflexos coerentes, organização natural e enquadramento [CAMERA]. Luz [LIGHTING], clima [MOOD].
```

### Quarto
```text
Cena em quarto: [SCENE]. Mostre [SUBJECT] realizando [ACTION]. Integre [PRODUCT] ao ambiente de forma plausível. Composição [CAMERA], luz [LIGHTING], clima [MOOD].
```

### Academia
```text
Cena em academia durante [ACTIVITY], com [SUBJECT] usando [PRODUCT] somente se esse uso for apropriado ao produto. Priorize ação legível, ambiente plausível e enquadramento [CAMERA]. Luz [LIGHTING], clima [MOOD].
```

### Situações cotidianas
```text
Registre um momento cotidiano: [SITUATION]. Mostre [ACTION] e a relação prática com [PRODUCT] sem transformar a cena em demonstração forçada. Local [LOCATION], câmera [CAMERA], iluminação [LIGHTING], clima [MOOD].
```
