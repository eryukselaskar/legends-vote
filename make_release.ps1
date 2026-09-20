$ErrorActionPreference = "Stop"
$ProjectDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $ProjectDir

$Version = "v1.0.0"
$OutDir = "release\LegendsVote-$Version"
$ZipPath = "release\LegendsVote-$Version.zip"

# 1) Exe var mi?
$ExePath = "dist\LegendsVote.exe"
if (-not (Test-Path $ExePath)) {
    throw "dist\LegendsVote.exe yok. Once build_exe.ps1 calistir."
}

# 2) Cikis klasorunu temizle
Remove-Item -Recurse -Force "release" -ErrorAction SilentlyContinue
New-Item -ItemType Directory -Force -Path $OutDir | Out-Null

# 3) Dosyalari kopyala
Copy-Item $ExePath "$OutDir\LegendsVote.exe"
Copy-Item ".env.example" "$OutDir\.env.example"
Copy-Item "OKU-BENI.txt" "$OutDir\OKU-BENI.txt"

# 4) Zip'le
Compress-Archive -Path "$OutDir\*" -DestinationPath $ZipPath -Force

Write-Host ""
Write-Host ">>> Release hazir: $ZipPath"
Write-Host ">>> GitHub Releases sayfasina yukle."