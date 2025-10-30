<p style="text-align:center">Techpedia</p>

> A living knowledge base, skill archive, and project portfolio by **Matt Howard**

---

## How to Use Techpedia

This vault is both a learning record and a quick-reference.  
See the [[README]] for navigation, structure, and conventions.

---

## About Me

I’m **Matthew J. Howard**, a hands-on learner with a passion for technology, problem-solving, and building clean, practical systems. My background in field service and telecommunications taught me how to think on my feet, diagnose complex issues, and deliver reliable results under pressure. Now I’m channeling that experience into **IT and cybersecurity**, developing skills in **Linux, scripting, and systems automation**. I enjoy understanding how things work, documenting what I learn, and turning it into clear, useful resources that live in **Techpedia**, my personal knowledge base and technical portfolio.

I’m currently seeking **entry-level positions** where I can contribute, grow, and continue learning through real-world challenges.

---

## Skills Snapshot
*[[Expanded Skills Log]]*

| Area                             | What I’ve Practiced                                                                                                                                                              | Evidence                                                                                                               |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Systems & Troubleshooting**    | Two decades of self-guided PC repair, OS installation, and issue resolution across Windows and Linux(1 year); proficient in diagnosing performance, driver, and hardware faults. | _[[Expanded Skills Log#Earlier Accomplishments\|Earlier Accomplishments]]_, _Progress Journals_                        |
| **Hardware & Build Maintenance** | Rebuilt and upgraded systems (CPU, RAM, cooling, PSU, storage); applied thermal paste, resolved overheating, and optimized builds for stability.                                 | _[[Expanded Skills Log]]_                                                                                              |
| **Networking & Connectivity**    | Configured DHCP/DNS, router firmware (DD-WRT bridge), port forwarding, and LAN hosting for multiplayer environments.                                                             | _Networking Notes_, _[[Expanded Skills Log#Earlier Accomplishments\|Earlier Accomplishments]]_                         |
| **Virtualization & Homelab**     | Installed and configured Proxmox; deployed Windows Server 2025 and Linux VMs; explored AD DS, DNS, DHCP, and future security hardening.                                          | _Projects → Homelab_                                                                                                   |
| **Documentation & Workflow**     | Designed and maintain a structured personal knowledge vault with changelogs, skill logs, templates, and daily progress journals.                                                 | _Vault Architecture_, _CHANGELOG_                                                                                      |
| **Security & Privacy Awareness** | Practiced safe OS isolation (VM sandboxing for monitored WFH software), studied network defense/hardening, and use privacy-focused tools.                                        | _Progress Journals_, _Homelab Security Plan_, [[Expanded Skills Log#Earlier Accomplishments\|Earlier Accomplishments]] |
| **Linux Familiarity & CLI**      | Installed and configured Arch Linux and Ubuntu; navigated file systems, permissions, and package management.                                                                     | _Linux Notes_                                                                                                          |

---

## Weekly Progress (recent)

| Date           | Focus                                                                |
| -------------- | -------------------------------------------------------------------- |
| [[2025-10-29]] | Focused on vault archiving and cohesion                              |
| [[2025-10-28]] | Homelab setup continued-DNS and DHCP creation on windows server 2025 |
| [[2025-10-27]] | Homelab setup; Security+ Study(Professor Messer Audio files)         |
| [[2025-08-08]] | A+ Core 1 prep reflections; THM streak                               |
| [[2025-07-28]] | Package mgmt & vault structure tweaks                                |
| [[2025-07-27]] | `apt` vs `apt-get`; custom callouts                                  |
| [[2025-07-26]] | Taught Linux basics to a friend                                      |

---

## Recent Projects

### Python: TCP Port Scanner

Small, focused CLI port scanner with banner-grabbing and simple range parsing.  
**Stack:** Python 3 (sockets, argparse)  
**Flags:** `-i` show local IP, `-l` show closed/filtered, `-v` verbose banners  
**File:** [[portScanner.py]]

`Examples - Scan a few ports:    python portScanner.py 192.168.1.10 22,80,443 - Scan a range:        python portScanner.py 10.0.0.5 1-1024 -l - Grab banners:        python portScanner.py target.tld 80,443 -v`

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
    

A directory of known commands can be found at Linux_Notes/Commands/ 

---

## Resume and Certifications
*My resume and current certifications are available below*
### Resume
**[[Resume|Matthew Howard resume]]**
### Certifications
**[[CompTIA A+ ce certificate.pdf|CompTIA A+ Certification]]**

---

## Changelog

[View the Vault Changelog](CHANGELOG.md)

---

### Footer

_Last updated:_ 10/21/2025• _Vault owner:_ **Matt Howard (YourFriendHowy)**