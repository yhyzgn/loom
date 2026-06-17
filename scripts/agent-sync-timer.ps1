$ErrorActionPreference = "SilentlyContinue"
Set-Location -LiteralPath "/home/neo/Projects/neo/pub/agent-config-hub"
& "/home/neo/Projects/neo/pub/agent-config-hub/bin/agent-sync" hook --platform timer --phase timer *>> "/home/neo/Projects/neo/pub/agent-config-hub/logs/windows-task.log"
