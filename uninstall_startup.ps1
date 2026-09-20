$StartupDir = [Environment]::GetFolderPath("Startup")
$ShortcutPath = Join-Path $StartupDir "LegendsVote.lnk"

if (Test-Path $ShortcutPath) {
    Remove-Item $ShortcutPath -Force
    Write-Host "Kaldirildi: $ShortcutPath"
} else {
    Write-Host "Kisayol bulunamadi."
}