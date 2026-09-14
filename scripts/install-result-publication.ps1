param([string]$TaskName = 'SEC-Frozen-Forward-Publish')
$ErrorActionPreference = 'Stop'
$projectRoot = Split-Path -Parent $PSScriptRoot
$pythonWindowless = Join-Path $projectRoot '.venv\Scripts\pythonw.exe'
if (-not (Test-Path -LiteralPath $pythonWindowless)) { throw 'Project pythonw.exe is missing' }
$action = New-ScheduledTaskAction -Execute $pythonWindowless -Argument '-m publication' -WorkingDirectory $projectRoot
$now = Get-Date
$nextPublication = $now.Date.AddHours(7).AddMinutes(15)
if ($nextPublication -le $now) { $nextPublication = $nextPublication.AddDays(1) }
$trigger = New-ScheduledTaskTrigger -Daily -At $nextPublication
$settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -MultipleInstances IgnoreNew -ExecutionTimeLimit (New-TimeSpan -Minutes 4) -Hidden
$account = [System.Security.Principal.WindowsIdentity]::GetCurrent().Name
$principal = New-ScheduledTaskPrincipal -UserId $account -LogonType Interactive -RunLevel Limited
Register-ScheduledTask -TaskName $TaskName -Action $action -Trigger $trigger -Settings $settings -Principal $principal -Description 'Publish immutable public prediction results to origin/main daily at 07:15 local time; never invokes prediction. Requires logged-in user and network.' -Force | Select-Object TaskName,State
