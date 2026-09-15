param(
    [string]$TaskName = 'SEC-Frozen-Forward-Publish',
    [string]$Recipient
)
$ErrorActionPreference = 'Stop'
$projectRoot = Split-Path -Parent $PSScriptRoot
$pythonWindowless = Join-Path $projectRoot '.venv\Scripts\pythonw.exe'
if (-not (Test-Path -LiteralPath $pythonWindowless)) { throw 'Project pythonw.exe is missing' }
$stateRoot = Join-Path $projectRoot 'artifacts\local\publication'
$configPath = Join-Path $stateRoot 'email-config.json'
New-Item -ItemType Directory -Path $stateRoot -Force | Out-Null

$existing = $null
if (Test-Path -LiteralPath $configPath) {
    $existing = Get-Content -Raw -Encoding UTF8 -LiteralPath $configPath | ConvertFrom-Json
}
if ([string]::IsNullOrWhiteSpace($Recipient)) {
    if ($null -eq $existing -or [string]::IsNullOrWhiteSpace([string]$existing.recipient)) {
        throw 'Recipient is required for the first email-enabled installation'
    }
    $Recipient = [string]$existing.recipient
}
try { $mailAddress = [System.Net.Mail.MailAddress]::new($Recipient) }
catch { throw 'Recipient must be one plain email address' }
if ($mailAddress.Address -cne $Recipient -or $Recipient -match '[,;\r\n]') {
    throw 'Recipient must be one plain email address'
}

$codexPackage = Join-Path $env:APPDATA 'npm\node_modules\@openai\codex'
$codexCandidates = @(Get-ChildItem -LiteralPath $codexPackage -Filter 'codex.exe' -File -Recurse)
if ($codexCandidates.Count -ne 1) { throw 'Expected exactly one installed native codex.exe' }
$activationDate = if ($null -ne $existing -and -not [string]::IsNullOrWhiteSpace([string]$existing.activation_date_kst)) {
    [string]$existing.activation_date_kst
} else {
    (Get-Date).ToString('yyyy-MM-dd')
}
$model = if ($null -ne $existing -and -not [string]::IsNullOrWhiteSpace([string]$existing.model)) {
    [string]$existing.model
} else {
    'gpt-5.6-luna'
}
$emailConfig = [ordered]@{
    version = 1
    enabled = $true
    recipient = $Recipient
    activation_date_kst = $activationDate
    codex_executable = $codexCandidates[0].FullName
    model = $model
}
$configJson = $emailConfig | ConvertTo-Json -Depth 4
[System.IO.File]::WriteAllText($configPath, $configJson + [Environment]::NewLine, [System.Text.UTF8Encoding]::new($false))

$action = New-ScheduledTaskAction -Execute $pythonWindowless -Argument '-m publication' -WorkingDirectory $projectRoot
$now = Get-Date
$nextPublication = $now.Date.AddHours(7).AddMinutes(15)
if ($nextPublication -le $now) { $nextPublication = $nextPublication.AddDays(1) }
$trigger = New-ScheduledTaskTrigger -Daily -At $nextPublication
$settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -MultipleInstances IgnoreNew -ExecutionTimeLimit (New-TimeSpan -Minutes 10) -Hidden
$account = [System.Security.Principal.WindowsIdentity]::GetCurrent().Name
$principal = New-ScheduledTaskPrincipal -UserId $account -LogonType Interactive -RunLevel Limited
Register-ScheduledTask -TaskName $TaskName -Action $action -Trigger $trigger -Settings $settings -Principal $principal -Description 'Publish immutable public results and reconcile one professional briefing email daily at 07:15 local time; never invokes prediction. Requires logged-in user and network.' -Force | Select-Object TaskName,State
