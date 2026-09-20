$ErrorActionPreference = "Stop"
$ProjectDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$ExePath = Join-Path $ProjectDir "dist\LegendsVote.exe"

if (-not (Test-Path $ExePath)) {
    throw "dist\LegendsVote.exe bulunamadi. Once build_exe.ps1 calistir."
}

$StartupDir = [Environment]::GetFolderPath("Startup")
$ShortcutPath = Join-Path $StartupDir "LegendsVote.lnk"

$WshShell = New-Object -ComObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut($ShortcutPath)
$Shortcut.TargetPath = $ExePath
$Shortcut.Arguments = "--watch"
$Shortcut.WorkingDirectory = $ProjectDir
$Shortcut.WindowStyle = 7  # minimized
$Shortcut.Description = "Legends Vote - gunluk oy hatirlatici"
$Shortcut.Save()

Write-Host "Startup kisayolu olusturuldu:"
Write-Host "  $ShortcutPath"
Write-Host "  -> $ExePath --watch"
Write-Host ""
Write-Host "PC bir sonraki acilisinda arka planda otomatik baslayacak."
Write-Host "Simdi baslatmak icin: Start-Process '$ExePath' -ArgumentList '--watch'"