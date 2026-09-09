$ErrorActionPreference = "Stop"
git submodule update --init --recursive
New-Item -ItemType Directory -Force -Path ".agents\skills" | Out-Null
Get-ChildItem ".bkit-codex\.agents\skills" -Directory | ForEach-Object {
  $dest = Join-Path ".agents\skills" $_.Name
  if (Test-Path $dest) { Remove-Item -Recurse -Force $dest }
  Copy-Item -Recurse -Force $_.FullName $dest
}
@("docs\01-plan\features","docs\02-design\features","docs\03-analysis","docs\04-report") | ForEach-Object { New-Item -ItemType Directory -Force -Path $_ | Out-Null }
Write-Host "bkit-codex project setup complete. Start Codex in this repository and check PDCA status."
