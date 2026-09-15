from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "install-result-publication.ps1"


def test_publication_task_runs_once_daily_at_0715():
    source = SCRIPT.read_text(encoding="utf-8")

    assert "AddHours(7).AddMinutes(15)" in source
    assert "New-ScheduledTaskTrigger -Daily -At $nextPublication" in source
    assert "RepetitionInterval" not in source
    assert "New-TimeSpan -Minutes 5" not in source
    assert "daily at 07:15 local time" in source


def test_publication_task_preserves_action_and_safety_settings():
    source = SCRIPT.read_text(encoding="utf-8")

    assert "'.venv\\Scripts\\pythonw.exe'" in source
    assert "-Argument '-m publication'" in source
    assert "-WorkingDirectory $projectRoot" in source
    assert "-StartWhenAvailable" in source
    assert "-MultipleInstances IgnoreNew" in source
    assert "-ExecutionTimeLimit (New-TimeSpan -Minutes 10)" in source
    assert "-Hidden" in source
    assert "-LogonType Interactive -RunLevel Limited" in source
    assert "Register-ScheduledTask -TaskName $TaskName" in source
    assert "-Force" in source


def test_publication_installer_keeps_email_identity_local():
    source = SCRIPT.read_text(encoding="utf-8")

    assert "[string]$Recipient" in source
    assert "artifacts\\local\\publication" in source
    assert "email-config.json" in source
    assert "activation_date_kst" in source
    assert "codex.exe" in source
    assert "example.com" not in source
    assert "@gmail.com" not in source
