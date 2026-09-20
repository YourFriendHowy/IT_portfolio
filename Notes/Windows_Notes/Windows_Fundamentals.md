---
obsidianUIMode: preview
Language:
  - N/A
Category: Study
Topic: Windows Fundamentals
Type: Notes
System: Windows
Element type: Concept
Arguments: N
Source: TestOut / Professor Messer
Complexity: Beginner
Keywords:
  - Windows
  - A+
  - OS
  - Fundamentals
aliases: Windows Fundamentals
DateCreated: 2025-10-20
LastEdited: 2025-10-20
---

# Windows Fundamentals

This page covers the basic concepts I practiced while preparing for the CompTIA A+ exams (1101 / 1102).  
Most of what’s written here comes from TestOut labs and a bit of Professor Messer’s content.  
It’s meant as a quick refresher for how Windows works and what tools I actually use.

---

## User Accounts and Permissions
- Windows separates **standard** and **administrator** accounts.  
- Local accounts live on the device; domain accounts come from a server (Active Directory).  
- Permissions are tied to **NTFS**. The main ones are Read, Write, Modify, and Full Control.  
- Permissions can be set in the file’s Properties → Security tab.

---

## System Tools I Use Most
- **Control Panel / Settings** – General configuration  
- **Device Manager** – Check drivers and hardware status  
- **Task Manager** – End stuck programs, watch CPU or RAM use  
- **Event Viewer** – View system or application errors  
- **Disk Management** – Format or resize drives

---

## Networking Basics on Windows
- `ipconfig` shows IP info  
- `ping` tests connectivity  
- `nslookup` checks DNS  
- `tracert` shows the route to a destination  
- Basic home setup: most devices use DHCP for automatic addressing

---

## System Maintenance
- Keep Windows Update turned on  
- Use antivirus (Windows Defender works fine for most setups)  
- Disk Cleanup and Storage Sense help free space  
- Backups can be done with File History or OneDrive sync

---

## Common Fix Commands
| Purpose | Command |
|----------|----------|
| Check system files | `sfc /scannow` |
| Repair image | `DISM /Online /Cleanup-Image /RestoreHealth` |
| View startup items | `msconfig` |
| Check disk for errors | `chkdsk /f` |

---

## Notes
This note just keeps my basic Windows knowledge in one place.  
Any hands-on steps, screenshots, or troubleshooting examples will go in a project or journal entry instead.
