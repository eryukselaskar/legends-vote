$ErrorActionPreference = "Stop"
$ProjectDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $ProjectDir

Write-Host ">>> PyInstaller hazirlaniyor..."
uv sync

Write-Host ">>> Eski build temizleniyor..."
Remove-Item -Recurse -Force build, dist, LegendsVote.spec -ErrorAction SilentlyContinue

Write-Host ">>> Exe uretiliyor (bu 1-3 dk surebilir)..."
uv run pyinstaller `
    --onefile `
    --noconsole `
    --name LegendsVote `
    --hidden-import winotify `
    --hidden-import dotenv `
    --hidden-import playwright `
    --collect-all playwright `
    --collect-all winotify `
    vote_app.py

Write-Host ""
Write-Host ">>> Exe hazir: $ProjectDir\dist\LegendsVote.exe"