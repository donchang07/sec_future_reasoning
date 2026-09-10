param([string]$TaskName = 'SEC-Frozen-Forward-Publish')
$ErrorActionPreference = 'Stop'
$projectRoot = Split-Path -Parent $PSScriptRoot
$pythonWindowless = Join-Path $projectRoot '.venv\Scripts\pythonw.exe'
if (-not (Test-Path -LiteralPath $pythonWindowless)) { throw 'Project pythonw.exe is missing' }
$action = New-ScheduledTaskAction -Execute $pythonWindowless -Argument '-m publication' -WorkingDirectory $projectRoot
$trigger = New-ScheduledTaskTrigger -Once -At ((Get-Date).AddMinutes(1)) -RepetitionInterval (New-TimeSpan -Minutes 5)
$settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -MultipleInstances IgnoreNew -ExecutionTimeLimit (New-TimeSpan -Minutes 4) -Hidden
$account = [System.Security.Principal.WindowsIdentity]::GetCurrent().Name
$principal = New-ScheduledTaskPrincipal -UserId $account -LogonType Interactive -RunLevel Limited
Register-ScheduledTask -TaskName $TaskName -Action $action -Trigger $trigger -Settings $settings -Principal $principal -Description 'Publish immutable public prediction results to origin/main every five minutes; never invokes prediction. Requires logged-in user and network.' -Force | Select-Object TaskName,State
