# Input schema

Contrato JSON correspondente a schemas/video_input.schema.json; validação Python em schemas/contracts.py.

| Campo | Tipo | Regra |
| --- | --- | --- |
| source_type | string | local ou url |
| source | string | Caminho local ou URL absoluta http(s) |
| filename | string/null | Nome opcional, não substitui a origem |
| language | string/null | Idioma declarado/detectado pelo chamador |
| duration | number/null | Duração conhecida em segundos, maior que zero |
| platform | string/null | Plataforma de origem, se conhecida |
| metadata | object | Metadados adicionais serializáveis |

source_type e source são obrigatórios. VideoInput.from_dict() rejeita campos desconhecidos. Validar URL não faz download. A validação de arquivo local ocorre no pipeline e exige arquivo existente.

Exemplo de objeto:
    {"source_type":"local","source":"path/to/reference.mp4","filename":"reference.mp4","language":null,"duration":null,"platform":null,"metadata":{}}
