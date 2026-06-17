# RTK - Rust Token Killer

**Usage**: Token-optimized CLI proxy (60-90% savings on dev operations)

## Meta Commands (always use rtk directly)

```bash
rtk gain              # Show token savings analytics
rtk gain --history    # Show command usage history with savings
rtk discover          # Analyze Claude Code history for missed opportunities
rtk proxy <cmd>       # Execute raw command without filtering (for debugging)
```

## Installation Verification

```bash
rtk --version         # Should show: rtk X.Y.Z
rtk gain              # Should work (not "command not found")
which rtk             # Verify correct binary
```

⚠️ **Name collision**: If `rtk gain` fails, you may have reachingforthejack/rtk (Rust Type Kit) installed instead.

## Hook-Based Usage

All other commands are automatically rewritten by the Claude Code hook.
Example: `git status` → `rtk git status` (transparent, 0 tokens overhead)

Refer to CLAUDE.md for full command reference.

<!-- FABLE5:GEMINI:START -->
# Default Fable5 persona adapter

Load and apply `/home/neo/.agent-personas/claude-fable5/core.md` as a default response style/safety layer.

Do not copy the original Claude prompt literally. Preserve this host agent's identity, tools, policies, and local project instructions. Read `/home/neo/.agent-personas/claude-fable5/references/CLAUDE-FABLE-5.original.md` only when the user explicitly asks for source-level comparison, audit, quotation, or migration details.
<!-- FABLE5:GEMINI:END -->
