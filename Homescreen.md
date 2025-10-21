# <p style="text-align:center">Techpedia</p>

> A living knowledge base, skill archive, and project portfolio by **Matt Howard**

---

## How to Use Techpedia

This vault is both a learning record and a quick-reference.  
See the README for navigation, structure, and conventions.

---

## About Me

**Matt “Howy” Howard**

- Red teamer in training • Linux learner • Builder of tidy docs
    
- Areas of focus: security fundamentals, Linux ops, scripting, automation
    
- Tools I use: Python, Bash, Git/GitHub, Obsidian (Templater/Dataview), TryHackMe
    
- Availability: Open to internships, apprenticeships, and junior roles
    

> Email / LinkedIn / GitHub: _add links here_

---

## Skills Snapshot

|Area|What I’ve practiced|Evidence|
|---|---|---|
|Linux Ops|Filesystem/navigation, permissions, processes, journaling|`Linux_Notes/*` (command cards like `ls`, `chmod`, `systemctl`, `journalctl`, `tail`, etc.)|
|Scripting|Python (CLI tools, sockets), Bash (workflow, aliases)|**Port Scanner** (`portScanner.py`), **Bash Aliases**|
|Networking|Ports/services, basic scanning, SSH/SCP|Port scanner usage, `scp` notes, TryHackMe rooms|
|Systems & Logs|`journalctl`, `/var/log`, `dmesg`, `uptime`, load avg|Notes: **Logs.md**, **systemd.md**, **Systemd/load avg**|
|Tooling|Git basics + workflow, Obsidian templating/dataview|**Git Cheatsheet**, **Templates** (`progress_template`, `command_template`)|

---

## Weekly Progress (recent)

|Date|Focus|Link|
|---|---|---|
|2025-08-08|A+ Core 1 prep reflections; THM streak|[[2025-08-08]]|
|2025-07-28|Package mgmt & vault structure tweaks|[[2025-07-28]]|
|2025-07-27|`apt` vs `apt-get`; custom callouts|[[2025-07-27]]|
|2025-07-26|Taught Linux basics to a friend|[[2025-07-26]]|
|2025-07-25|Practice quiz takeaways; THM start|[[2025-07-25]]|
|2025-07-23|A+ networking study; note workflow|[[2025-07-23]]|
|2025-07-22|JS date study; vault restructure|[[2025-07-22]]|

**Full Journal Index** → _link your journal index or tag view_

---

## Recent Projects

### Python: TCP Port Scanner

Small, focused CLI port scanner with banner-grabbing and simple range parsing.  
**Stack:** Python 3 (sockets, argparse)  
**Flags:** `-i` show local IP, `-l` show closed/filtered, `-v` verbose banners  
**File:** [[portScanner.py]]

`Examples - Scan a few ports:    python portScanner.py 192.168.1.10 22,80,443 - Scan a range:        python portScanner.py 10.0.0.5 1-1024 -l - Grab banners:        python portScanner.py target.tld 80,443 -v`

> Next steps (roadmap): parallel scans with `concurrent.futures`, service fingerprints, output to CSV/JSON.

---

## Training & Rooms (TryHackMe)

|Track|Notes|
|---|---|
|Offensive Security Intro|[[R1-Offensive Security Intro]]|
|Defensive Security Intro (SOC/DFIR basics)|[[R2-Defensive Security Intro]]|
|Search Skills|[[R3-Search Skills]] _(skeleton ready to expand)_|
|Linux Fundamentals — Part 1|[[R4-Linux Fundamentals-part1]] _(template in place)_|

---

## Reference Libraries

### Linux Notes (Command Cards)

Quick, single-purpose cards with flags, meaning, and examples.

- Navigation & Files: `ls`, `cd`, `pwd`, `cp`, `mv`, `rm`, `mkdir`, `touch`, `file`, `head`, `tail`, `diff`, `cat`
    
- System & Processes: `ps`, `top`, `htop`, `uptime`, load average, `free`, `df`
    
- Users & Groups: `adduser`, `userdel`, `passwd`, `groups`, `groupadd`, `groupdel`, `su`, `sudo`
    
- Networking & Transfer: `scp`, `curl`, `wget`, `which`, `whoami`
    
- Services & Logs: `systemctl`, `journalctl`, **Logs.md**
    
- Special dirs: `/etc`, `/var`, `/tmp`, `/root`
    

> Start here: **[[Commands.md]]** (index), then jump into any command card.

---

## Templates & Workflows

- **Daily Progress** → [[progress_template]] (auto-dated, with study + practice sections)
    
- **Universal Study Template** → [[A+_template]] (rename to `study_template.md` if you prefer)
    
- **Command Card Template** → [[command_template]]
    
- **Default Note Template** → [[default_template]]
    

**Customizations & Config**

- **Bash Aliases** → _[[Bash Aliases]]_
    
- **Git Basics** → _[[Git Commands]]_
    
- Obsidian settings/keybinds → _add links/screenshots when ready_
    

---

## Resume

Add your hosted resume link here (PDF or site) → **View My Resume**

> Tip: keep the vault and resume in sync—when you add a new project or room, append a single-line entry to your resume’s “Projects” or “Training” section.

---

## Changelog

[View the Vault Changelog](CHANGELOG.md)

---

### Footer

_Last updated:_ **<insert today’s date>** • _Vault owner:_ **Matt Howard (YourFriendHowy)**