param([string]$TaskName = 'SEC-Frozen-Forward-Daily', [string]$At = '16:10')
$ErrorActionPreference = 'Stop'
$projectRoot = Split-Path -Parent $PSScriptRoot
$pythonWindowless = Join-Path $projectRoot '.venv\Scripts\pythonw.exe'
if (-not (Test-Path -LiteralPath $pythonWindowless)) { throw 'Project pythonw.exe is missing' }
$action = New-ScheduledTaskAction -Execute $pythonWindowless -Argument '-m forward_ops daily' -WorkingDirectory $projectRoot
$trigger = New-ScheduledTaskTrigger -Daily -At $At
$settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -MultipleInstances IgnoreNew -ExecutionTimeLimit (New-TimeSpan -Minutes 10) -RestartCount 3 -RestartInterval (New-TimeSpan -Minutes 30) -Hidden
$account = [System.Security.Principal.WindowsIdentity]::GetCurrent().Name
$principal = New-ScheduledTaskPrincipal -UserId $account -LogonType Interactive -RunLevel Limited
Register-ScheduledTask -TaskName $TaskName -Action $action -Trigger $trigger -Settings $settings -Principal $principal -Description 'Frozen v2 daily close; shadow-only evidence; immutable forward evaluation. Requires logged-in user.' -Force | Select-Object TaskName,State
