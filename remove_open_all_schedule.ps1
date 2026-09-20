$TaskName = "LegendsVoteOpenAll"
try {
    Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false
    Write-Host "Gorev kaldirildi: $TaskName"
} catch {
    Write-Host "Gorev bulunamadi: $_"
}