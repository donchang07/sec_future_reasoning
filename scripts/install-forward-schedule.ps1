param([string]$TaskName = 'SEC-Frozen-Forward-Daily', [ValidateSet('07:00')][string]$At = '07:00')
$ErrorActionPreference = 'Stop'
if ((Get-TimeZone).Id -ne 'Korea Standard Time') { throw 'This installer requires Korea Standard Time' }
$projectRoot = Split-Path -Parent $PSScriptRoot
$pythonWindowless = Join-Path $projectRoot '.venv\Scripts\pythonw.exe'
if (-not (Test-Path -LiteralPath $pythonWindowless)) { throw 'Project pythonw.exe is missing' }
$action = New-ScheduledTaskAction -Execute $pythonWindowless -Argument '-m forward_ops daily' -WorkingDirectory $projectRoot
$trigger = New-ScheduledTaskTrigger -Daily -At $At
$settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -MultipleInstances IgnoreNew -ExecutionTimeLimit (New-TimeSpan -Minutes 10) -RestartCount 3 -RestartInterval (New-TimeSpan -Minutes 30) -Hidden
$account = [System.Security.Principal.WindowsIdentity]::GetCurrent().Name
$principal = New-ScheduledTaskPrincipal -UserId $account -LogonType Interactive -RunLevel Limited
Register-ScheduledTask -TaskName $TaskName -Action $action -Trigger $trigger -Settings $settings -Principal $principal -Description 'daily-preopen-v1.0.1: 07:00 KST frozen v2; source-timing-v1.0.1; immutable forward evaluation. Requires logged-in user.' -Force | Select-Object TaskName,State
