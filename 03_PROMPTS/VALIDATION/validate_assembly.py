#!/usr/bin/env python3
"""Local structural checks for the 03_PROMPTS library and a prompt assembly.

Uses only the Python standard library. It reports editorial/semantic questions
for human review instead of treating them as automatic errors.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MARKDOWN_LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
INLINE_PATH = re.compile(r"`((?:\.\.?/)?[A-Z][A-Z0-9_./-]+(?:\.md|/))`")
PLACEHOLDER = re.compile(r"\[([A-Z][A-Z0-9_]*(?:/[A-Z0-9_]+)*)\]")
REQ = re.compile(r"\*\*Módulos necessários:\*\*\s*(.*)", re.I)
OPT = re.compile(r"\*\*Módulos opcionais:\*\*\s*(.*)", re.I)
IDENTITY_RISK = re.compile(
    r"(?:ignore|substitua|substituir|contradiga|contradizer|override|replace|change)"
    r".{0,45}(?:identidade|identity).{0,45}(?:Sofia|oficial|official)|"
    r"(?:identidade|identity).{0,45}(?:Sofia|oficial|official).{0,45}"
    r"(?:ignore|substitua|contradiga|override|replace|change)", re.I,
)

MEDIA_ONLY_VIDEO = {
    "UGC_FORMAT", "UGC_TEMPLATE", "HOOK", "RETENTION", "SCRIPT", "DIALOGUE",
    "CTA", "VIDEO_DIRECTION", "DURATION", "VIDEO_PROMPT_STRUCTURE",
}
MEDIA_ONLY_IMAGE = {"SCENE", "IMAGE_PROMPT_BASE"}
FIELD_FILES = {
    "OBJECTIVE": "MODULE_CARDS/OBJECTIVE.md", "PRODUCT": "MODULE_CARDS/PRODUCT.md",
    "UGC_FORMAT": "MODULE_CARDS/UGC_FORMAT.md", "HOOK": "MODULE_CARDS/HOOK.md",
    "SCRIPT": "MODULE_CARDS/SCRIPT.md", "DIALOGUE": "MODULE_CARDS/DIALOGUE.md",
    "ACTION": "MODULE_CARDS/ACTION.md", "LOCATION": "MODULE_CARDS/LOCATION.md",
    "CAMERA": "MODULE_CARDS/CAMERA.md", "LIGHTING": "MODULE_CARDS/LIGHTING.md",
    "STYLE": "MODULE_CARDS/STYLE.md", "MOOD": "MODULE_CARDS/MOOD.md",
    "DURATION": "MODULE_CARDS/DURATION.md",
    "MODEL_ADAPTATION": "MODULE_CARDS/MODEL_ADAPTATION.md",
    "VIDEO_DIRECTION": "VIDEO_DIRECTION/README.md",
    "MODEL_PROFILE": "MODEL_ADAPTERS/README.md",
    "RETENTION": "HOOKS_RETENTION_CTA/ORCHESTRATION.md",
    "CTA": "HOOKS_RETENTION_CTA/ORCHESTRATION.md",
    "IMAGE_PROMPT_BASE": "IMAGE_PROMPTS/README.md",
    "VIDEO_PROMPT_STRUCTURE": "VIDEO_PROMPTS/README.md",
}

def markdown_files():
    return sorted(p for p in ROOT.rglob("*.md") if ".git" not in p.parts)

def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()

def audit_library():
    errors, warnings, info = [], [], []
    files = markdown_files()
    for source in files:
        text = source.read_text(encoding="utf-8")
        for target in MARKDOWN_LINK.findall(text):
            target = target.strip().split("#", 1)[0]
            if not target or re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target):
                continue
            resolved = (source.parent / target).resolve()
            if not resolved.exists():
                errors.append(f"link local quebrado: {rel(source)} -> {target}")
        for target in INLINE_PATH.findall(text):
            candidates = [(source.parent / target).resolve(), (ROOT / target).resolve()]
            if not any(candidate.exists() for candidate in candidates):
                errors.append(f"referência interna inexistente: {rel(source)} -> {target}")

    # Extract the field names already defined in the canonical glossary. This
    # deliberately treats legacy/pending placeholders as review items, not errors.
    glossary = (ROOT / "GLOSSARIO_CANONICO.md").read_text(encoding="utf-8")
    # A glossary field can appear outside its main table (reference-analysis
    # fields, provenance metadata, proof schema, and documented legacy tokens).
    defined = set(PLACEHOLDER.findall(glossary))
    declared_local = set()
    for p in files:
        body = p.read_text(encoding="utf-8")
        for match in re.findall(r"\*\*Campos específicos desta ficha:\*\*\s*([^\n]+)", body, re.I):
            declared_local.update(re.findall(r"`([A-Z][A-Z0-9_]*)`", match))
    defined |= declared_local
    uses = {}
    for p in files:
        for token in PLACEHOLDER.findall(p.read_text(encoding="utf-8")):
            uses.setdefault(token, set()).add(rel(p))
    pending = [token for token in ("TYPE/SETTING", "MOMENT/ROUTINE", "FIT/LIMITATION") if token in uses]
    if pending:
        warnings.append("placeholders explicitamente pendentes no glossário: " + ", ".join(f"[{x}]" for x in pending))

    templates = sorted((ROOT / "UGC_TEMPLATES/VIDEO_TEMPLATES").glob("*.md"))
    counts = {"markdown": len(files), "ugc_templates": len(templates), "placeholders": len(uses)}
    info.append("compatibilidade semântica, duplicação e identidade exigem revisão humana")
    return counts, errors, warnings, info

def split_module_list(value):
    marked = set(re.findall(r"`([^`]+)`", value))
    return marked or {x.strip().strip("`. ") for x in value.split(",") if x.strip()}

def validate_assembly(data):
    errors, warnings, passed = [], [], []
    media = str(data.get("media", "")).lower()
    if media not in {"image", "video"}:
        errors.append("'media' deve ser 'image' ou 'video'.")
        media = "unknown"

    # These are the published PROMPT_ASSEMBLY sequences, including its optional
    # reference-analysis stage. They are mirrored here for checking, not changed.
    stages = (data.get("stages") or [])
    if media == "video":
        order = ["INPUT", "REFERENCE_ANALYSIS", "UGC_TEMPLATE", "HOOKS_RETENTION_CTA",
                 "MODULE_CARDS", "VIDEO_DIRECTION", "CAMERA_AND_PHOTOGRAPHY",
                 "STYLE_PRESETS", "VIDEO_PROMPTS", "MODEL_ADAPTER", "PROMPT_FINAL"]
    elif media == "image":
        order = ["INPUT", "REFERENCE_ANALYSIS", "MODULE_CARDS", "IMAGE_PROMPTS",
                 "CAMERA_AND_PHOTOGRAPHY", "STYLE_PRESETS", "MODEL_ADAPTER", "PROMPT_FINAL"]
    else:
        order = []
    if stages:
        normalized = [str(s).upper() for s in stages]
        if len(normalized) != len(set(normalized)):
            errors.append("etapas repetidas na montagem")
        if "REFERENCE_ANALYSIS" not in normalized and data.get("reference_analysis"):
            errors.append("referência foi informada, mas REFERENCE_ANALYSIS não consta nas etapas.")
        # Optional reference stage may be omitted. Remaining declared stages must
        # be an ordered subsequence of the official flow and include required endpoints.
        allowed = [s for s in order if s != "REFERENCE_ANALYSIS" or data.get("reference_analysis")]
        positions = [allowed.index(s) if s in allowed else -1 for s in normalized]
        if -1 in positions or positions != sorted(positions):
            errors.append("etapas fora de ordem ou não pertencentes ao fluxo oficial.")
        required_stages = [s for s in allowed if s != "REFERENCE_ANALYSIS"]
        for endpoint in required_stages:
            if endpoint not in normalized:
                errors.append(f"etapa do fluxo oficial ausente: {endpoint}.")
        if not errors:
            passed.append("ordem das etapas compatível com PROMPT_ASSEMBLY.md")
    else:
        errors.append("stages não informado; a montagem não pode comprovar o fluxo oficial")

    modules = data.get("modules", [])
    fields = data.get("fields", {})
    omitted_fields = set(data.get("omitted_fields", []))
    if not isinstance(modules, list) or not isinstance(fields, dict):
        errors.append("'modules' deve ser lista e 'fields' deve ser objeto no JSON.")
        modules, fields = [], {}
    library_tokens = set()
    for document in markdown_files():
        library_tokens.update(PLACEHOLDER.findall(document.read_text(encoding="utf-8")))
    for key in fields:
        if key not in library_tokens:
            errors.append(f"campo sem definição na biblioteca: {key}")
    selected = set()
    for item in modules:
        path = str(item).replace("\\", "/")
        target = (ROOT / path).resolve()
        if not target.exists() or ROOT not in target.parents:
            errors.append(f"módulo/arquivo selecionado inexistente ou fora da biblioteca: {item}")
        else:
            selected.add(path)
    if modules and len(selected) == len(modules):
        passed.append("módulos selecionados existem")
    if media in {"image", "video"}:
        serializer = "IMAGE_PROMPTS/README.md" if media == "image" else "VIDEO_PROMPTS/README.md"
        other_serializer = "VIDEO_PROMPTS/README.md" if media == "image" else "IMAGE_PROMPTS/README.md"
        if serializer not in selected:
            errors.append(f"serializador correspondente à mídia não selecionado: {serializer}")
        if other_serializer in selected:
            errors.append(f"serializador incompatível com a mídia selecionado: {other_serializer}")

    template = data.get("template")
    required, optional = set(), set()
    if template:
        tp = (ROOT / str(template)).resolve()
        if not tp.exists() or ROOT not in tp.parents:
            errors.append(f"template inexistente: {template}")
        else:
            body = tp.read_text(encoding="utf-8")
            m = REQ.search(body)
            if m: required = split_module_list(m.group(1))
            m = OPT.search(body)
            if m: optional = split_module_list(m.group(1))
            if media == "image":
                errors.append("template UGC de vídeo selecionado para imagem")
            absent = required - set(fields)
            if absent:
                errors.append("campos obrigatórios declarados pelo template ausentes: " + ", ".join(sorted(absent)))
            if not absent:
                passed.append("campos obrigatórios declarados pelo template presentes")
            template_tokens = set(PLACEHOLDER.findall(body))
            unresolved_template = template_tokens - set(fields) - omitted_fields
            if unresolved_template:
                errors.append("placeholders do template sem valor ou omissão registrada: " + ", ".join(f"[{x}]" for x in sorted(unresolved_template)))
            elif omitted_fields:
                warnings.append("campos omitidos explicitamente: " + ", ".join(sorted(omitted_fields)) + "; confirme que são aplicáveis")
            unknown_fields = set(fields) - set(re.findall(r"\[([A-Z][A-Z0-9_]*)\]", body)) - required - optional
            # Local tokens may be described as template-specific even if they are
            # not included in the module lists.
            local = set(re.findall(r"\[([A-Z][A-Z0-9_]*)\]", body))
            unknown_fields -= local
            if unknown_fields:
                warnings.append("campos no formulário não citados no template: " + ", ".join(sorted(unknown_fields)))

    if media == "video" and set(fields) & MEDIA_ONLY_IMAGE:
        errors.append("campo exclusivo de imagem selecionado em montagem de vídeo: " + ", ".join(sorted(set(fields) & MEDIA_ONLY_IMAGE)))
    if media == "image" and set(fields) & MEDIA_ONLY_VIDEO:
        errors.append("campo exclusivo de vídeo selecionado em montagem de imagem: " + ", ".join(sorted(set(fields) & MEDIA_ONLY_VIDEO)))
    if media in {"image", "video"}:
        passed.append("campos exclusivos de imagem/vídeo compatíveis com a mídia")

    if "OBJECTIVE" not in fields and not ("IMAGE_OBJECTIVE" in fields or "VIDEO_OBJECTIVE" in fields):
        errors.append("campo obrigatório OBJECTIVE ausente (glossário canônico)")

    unresolved = []
    for name, value in fields.items():
        if value is None or (isinstance(value, str) and not value.strip()):
            errors.append(f"campo sem valor: {name}")
        elif isinstance(value, str) and PLACEHOLDER.search(value):
            unresolved.append(name)
    if unresolved:
        errors.append("placeholders não substituídos nos campos: " + ", ".join(unresolved))
    else:
        passed.append("campos registrados sem placeholders residuais/vazios")

    for name in fields:
        module_path = FIELD_FILES.get(name)
        if module_path and not (ROOT / module_path).exists():
            errors.append(f"definição do campo {name} aponta para arquivo inexistente: {module_path}")
        elif module_path and module_path not in selected:
            errors.append(f"módulo necessário ao campo {name} não registrado em modules: {module_path}")
    if data.get("reference_analysis") and not (ROOT / "REFERENCE_ANALYSIS/README.md").exists():
        errors.append("REFERENCE_ANALYSIS selecionada, mas camada não encontrada")

    prompt = data.get("prompt", "")
    for token in PLACEHOLDER.findall(prompt) if isinstance(prompt, str) else []:
        if token not in library_tokens:
            errors.append(f"placeholder sem definição na biblioteca: [{token}]")
    if isinstance(prompt, str) and PLACEHOLDER.search(prompt):
        errors.append("PROMPT FINAL contém placeholders não substituídos")
    if isinstance(prompt, str) and IDENTITY_RISK.search(prompt):
        errors.append("texto sinaliza possível tentativa de substituir/contradizer identidade oficial; revisão humana obrigatória")
    else:
        warnings.append("identidade não é validável semanticamente; confirme manualmente a fonte oficial e não inclua traços físicos da Sofia")

    return errors, warnings, passed

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--audit", action="store_true", help="audita links e placeholders da biblioteca")
    parser.add_argument("--assembly", type=Path, help="valida arquivo JSON de uma montagem")
    args = parser.parse_args()
    if not args.audit and not args.assembly:
        parser.error("informe --audit e/ou --assembly")
    failed = False
    if args.audit:
        counts, errors, warnings, info = audit_library()
        print(f"AUDITORIA: {counts['markdown']} arquivos Markdown, {counts['ugc_templates']} templates UGC, {counts['placeholders']} placeholders distintos")
        for item in errors: print(f"ERRO: {item}")
        for item in warnings: print(f"REVISAR: {item}")
        for item in info: print(f"HUMANO: {item}")
        if not errors: print("OK: nenhuma referência Markdown local quebrada encontrada")
        failed |= bool(errors)
    if args.assembly:
        path = args.assembly if args.assembly.is_absolute() else ROOT / args.assembly
        try:
            data = json.loads(path.read_text(encoding="utf-8-sig"))
        except (OSError, json.JSONDecodeError) as exc:
            print(f"ERRO: não foi possível ler JSON de montagem: {exc}")
            return 2
        errors, warnings, passed = validate_assembly(data)
        for item in passed: print(f"OK: {item}")
        for item in warnings: print(f"REVISAR: {item}")
        for item in errors: print(f"ERRO: {item}")
        if not errors: print("RESULTADO: montagem aprovada nas verificações estruturais implementadas")
        failed |= bool(errors)
    return 1 if failed else 0

if __name__ == "__main__":
    sys.exit(main())
