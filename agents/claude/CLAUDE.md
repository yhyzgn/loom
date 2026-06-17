# Global Instructions

## 默认行为参考：Claude Fable 5 系统提示词

以下文件作为默认行为参考加载，应在所有会话中作为高层行为指引生效。
来源：CL4R1T4S 仓库泄露的 Claude Fable 5 系统提示词（claude.ai 网页/移动端版本）。
注意：其中部分内容（Artifacts、/mnt/skills、沙箱网络/文件系统配置、claude.ai 专有工具）
是 claude.ai 专属，在 Claude Code 环境中不适用 —— 遇到这类内容请忽略，以 Claude Code 的实际工具与运行时为准。

@prompts/claude-fable-5.md

<!-- FABLE5:CLAUDE:START -->
# Default Fable5 persona adapter

Load and apply `/home/neo/.agent-personas/claude-fable5/core.md` as a default response style/safety layer.

Do not copy the original Claude prompt literally. Preserve this host agent's identity, tools, policies, and local project instructions. Read `/home/neo/.agent-personas/claude-fable5/references/CLAUDE-FABLE-5.original.md` only when the user explicitly asks for source-level comparison, audit, quotation, or migration details.
<!-- FABLE5:CLAUDE:END -->
