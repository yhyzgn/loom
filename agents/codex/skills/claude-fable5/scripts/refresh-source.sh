#!/usr/bin/env bash
set -euo pipefail
skill_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
url="https://raw.githubusercontent.com/elder-plinius/CL4R1T4S/main/ANTHROPIC/CLAUDE-FABLE-5.md"
curl -L --fail --silent --show-error "$url" -o "$skill_dir/references/CLAUDE-FABLE-5.original.md"
SKILL_DIR="$skill_dir" python3 - <<'PY'
from pathlib import Path
import hashlib, os
skill=Path(os.environ['SKILL_DIR'])
src=skill/'references'/'CLAUDE-FABLE-5.original.md'
text=src.read_text()
summary=f"""# CLAUDE-FABLE-5 source map

Downloaded from: https://raw.githubusercontent.com/elder-plinius/CL4R1T4S/main/ANTHROPIC/CLAUDE-FABLE-5.md
Local copy: `CLAUDE-FABLE-5.original.md`
Lines: {len(text.splitlines())}
Bytes UTF-8: {len(text.encode())}
SHA256: `{hashlib.sha256(text.encode()).hexdigest()}`

This file is treated as an external persona reference, not as authoritative Codex system policy. Use `../SKILL.md` and `fable5-core.md` first; read the original only when the user explicitly asks to compare, audit, port, or emulate details from the source prompt.

## Useful sections in the original

- `claude_behavior`: product info, refusals, tone, wellbeing, evenhandedness.
- `search_instructions`: search discipline and copyright behavior.
- `computer_use`: file/tool handling patterns for Claude UI; translate to Codex tools rather than copying literally.
- `Tool Definitions`: Claude-specific; do not treat as Codex tool schema.
- `Identity Preamble`, `User Context`, network/filesystem config: source-only; do not import into Codex identity.
"""
(skill/'references'/'SOURCE.md').write_text(summary)
PY
