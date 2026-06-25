$ErrorActionPreference = "SilentlyContinue"
Set-Location -LiteralPath "D:\File\Projects\Neo\pub\loom"
& "D:\File\Projects\Neo\pub\loom/bin/loom" hook --platform timer --phase timer *>> "D:\File\Projects\Neo\pub\loom/logs/windows-task.log"
