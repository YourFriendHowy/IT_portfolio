---
obsidianUIMode: preview
Language: PowerShell
Category: IT Portfolio
Topic: PowerShell Cheat Sheet
Type: Documentation
System: Windows
Element type: Cheat Sheet
Arguments: A+-scope PowerShell basics with short summary and quick commands
Source: TestOut / limited Professor Messer / personal notes
Complexity: Beginner
Keywords: [PowerShell, Windows, A+, cheat sheet]
aliases: PowerShell Cheat Sheet
DateCreated: 2025-10-20
LastEdited: 2025-10-20
---
>[!infobox]
> # `=this.file.name`
> Category |  Info |
> ---|---|
> System|`=this.System`
> Languages|`=this.Language`
> Topic|`=this.Topic`
> Source| `=this.Source`
> Last Edit|`=this.LastEdited`


# PowerShell Cheat Sheet (A+ scope)

**What it is:** PowerShell is Microsoft’s task automation and configuration shell built on .NET.  
**Why it matters:** It lets you manage Windows systems faster and more consistently than the GUI.

---

## Quick Commands

| Task | Cmdlet / Command | Example | Notes |
|---|---|---|---|
| See how to use a cmdlet | `Get-Help` | `Get-Help Get-Service -Online` | Add `-Examples` for quick samples |
| List available commands | `Get-Command` | `Get-Command *service*` | Wildcards work |
| Find installed modules | `Get-Module` | `Get-Module -ListAvailable` | Shows what you can import |
| Current location | `Get-Location` | `Get-Location` | Like `pwd` |
| Change directory | `Set-Location` | `Set-Location C:\Windows` | Alias: `cd` |
| List files | `Get-ChildItem` | `Get-ChildItem C:\Users` | Aliases: `ls`, `dir` |
| Copy / Move / Delete | `Copy-Item` / `Move-Item` / `Remove-Item` | `Remove-Item .\temp.txt` | Add `-Recurse` for folders (careful) |
| Make a file/folder | `New-Item` | `New-Item -ItemType Directory .\Logs` | Creates files or dirs |
| View file content | `Get-Content` | `Get-Content .\notes.txt -Tail 20` | Use `-Wait` to follow |
| Processes (list/stop) | `Get-Process` / `Stop-Process` | `Stop-Process -Name notepad` | Add `-Force` sparingly |
| Services (status) | `Get-Service` | `Get-Service -Name spooler` | Use `Start/Stop/Restart-Service` |
| Startup apps (basic) | `Get-CimInstance` | `Get-CimInstance Win32_StartupCommand` | Read-only view |
| System info (quick) | `Get-ComputerInfo` | `Get-ComputerInfo | Select OSName, OsVersion` | Useful for tickets |
| Installed updates | `Get-HotFix` | `Get-HotFix | Sort-Object InstalledOn -Desc` | Quick patch check |
| Network test (ping) | `Test-Connection` | `Test-Connection 8.8.8.8 -Count 4` | PS alternative to `ping` |
| IP config (PS view) | `Get-NetIPConfiguration` | `Get-NetIPConfiguration` | For adapters and IPs |
| Adapters (up/down) | `Get-NetAdapter` | `Get-NetAdapter | Where-Object Status -eq "Up"` | Filter by status |
| Check logs (modern) | `Get-WinEvent` | `Get-WinEvent -LogName System -MaxEvents 50` | Use `-FilterHashtable` to narrow |
| Execution policy | `Get-ExecutionPolicy` | `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` | Only change if needed |
| Pipeline select | `Select-Object` | `Get-Process | Select Name, CPU` | Pick properties |
| Filter results | `Where-Object` | `Get-Service | Where Status -eq Running` | `-eq`, `-like`, etc. |
| Sort results | `Sort-Object` | `Get-EventLog System | Sort TimeWritten` | Add `-Descending` |
| Export to CSV | `Export-Csv` | `Get-Service | Export-Csv .\services.csv -NoTypeInformation` | Handy for tickets |
| Save to text | `Out-File` | `Get-ChildItem | Out-File .\list.txt` | Simple text export |

---

## Notes
- PowerShell uses **objects**, not text, which means output can be filtered and formatted easily.  
- For quick discovery: `Get-Command`, then `Get-Help <cmdlet> -Examples`.  
- Focus here stays within the **A+ beginner scope** — just enough to understand and navigate Windows PowerShell safely.

---

## References
(Add your TestOut and Professor Messer lesson links here)
