# Validação local da biblioteca

Esta primeira camada valida estrutura e consistência documental sem mudar a ordem definida em [`../PROMPT_ASSEMBLY.md`](../PROMPT_ASSEMBLY.md), o glossário ou qualquer template. Requer Python 3 e usa somente a biblioteca padrão.

## Auditoria da biblioteca

Na raiz de `03_PROMPTS`, execute:

```powershell
python VALIDATION/validate_assembly.py --audit
```

O modo de auditoria verifica links Markdown e referências a arquivos/pastas em código inline, conta o inventário de placeholders e reporta os três tokens que o glossário mantém explicitamente pendentes. No modo de montagem, placeholders ainda presentes no prompt final são erros e tokens inexistentes na biblioteca são sinalizados.

## Validar uma montagem

Crie localmente um JSON conforme este formato e passe o caminho com `--assembly`:

```json
{
  "media": "video",
  "reference_analysis": false,
  "stages": [
    "INPUT", "UGC_TEMPLATE", "HOOKS_RETENTION_CTA", "MODULE_CARDS",
    "VIDEO_DIRECTION", "CAMERA_AND_PHOTOGRAPHY", "STYLE_PRESETS",
    "VIDEO_PROMPTS", "MODEL_ADAPTER", "PROMPT_FINAL"
  ],
  "template": "UGC_TEMPLATES/VIDEO_TEMPLATES/01_DEMONSTRACAO.md",
  "modules": [
    "MODULE_CARDS/PRODUCT.md", "MODULE_CARDS/OBJECTIVE.md",
    "MODULE_CARDS/UGC_FORMAT.md", "MODULE_CARDS/SCRIPT.md",
    "MODULE_CARDS/ACTION.md", "MODULE_CARDS/DURATION.md",
    "VIDEO_PROMPTS/README.md", "MODEL_ADAPTERS/README.md"
  ],
  "fields": {
    "PRODUCT": "Organizador compacto",
    "OBJECTIVE": "Mostrar uma etapa de uso",
    "UGC_FORMAT": "Demonstração curta",
    "SCRIPT": "Apresentar e demonstrar uma etapa",
    "ACTION": "Colocar itens dentro do organizador",
    "DURATION": "15 segundos"
  },
  "prompt": ""
}
```

As etapas seguem o fluxo oficial; `REFERENCE_ANALYSIS` pode ser omitida quando não há referência para analisar. Para `image`, use `IMAGE_PROMPTS` e não inclua campos temporais de vídeo. `fields` registra apenas os campos efetivamente preenchidos; `modules` registra arquivos selecionados. Campos obrigatórios declarados no template escolhido precisam constar em `fields`. Campos opcionais e condicionais só são exigidos quando a condição documentada se aplica.

```powershell
python VALIDATION/validate_assembly.py --assembly caminho\para\montagem.json
```

## Registro simples de uso

Para medir uso sem banco de dados, acrescente uma linha por montagem a [`USAGE_LOG.csv`](USAGE_LOG.csv), com data, mídia, template/base, caminhos dos módulos selecionados, nomes dos campos preenchidos e resultado estrutural. Separe múltiplos módulos/campos com `;`. Não registre valores dos campos, conteúdo pessoal ou características de identidade. Um registro de uso não comprova qualidade ou desempenho.

## Limites

O validador não avalia veracidade de claims, qualidade editorial, duplicação semântica, suporte de capacidades do modelo nem se uma referência foi adequadamente remodelada. Informa esses pontos para decisão humana. A verificação de identidade é apenas um alerta textual limitado; confirme manualmente a fonte oficial e nunca use esta biblioteca para definir características físicas da Sofia.
