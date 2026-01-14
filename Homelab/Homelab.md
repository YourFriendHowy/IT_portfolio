This Document is an overview of my current homelab in its entirety, it is not intended to be fully detailed documentation.
# Personal PC
### Hardware
This is a custom build I researched and assembled on in May 2020.

| CPU     | AMD Ryzen 7 3800X 3.9 GHz 8-Core                                                              |
| ------- | --------------------------------------------------------------------------------------------- |
| GPU     | MSI GAMING X TRIO GeForce RTX 2080 SUPER 8 GB Video Card                                      |
| Mobo    | MSI MPG X570 GAMING PRO CARBON WIFI                                                           |
| PSU     | SeaSonic FOCUS PLUS 850 Gold 850 W 80+ Gold Certified Fully Modular ATX Power Supply          |
| RAM     | G.Skill Trident Z RGB 32 GB (2 x 16 GB) DDR4-3600                                             |
| Storage | Samsung 860 Evo 500 GB 2.5" Solid State Drive,<br>Western Digital WD_BLACK 4 TB 3.5" 7200 RPM |
### Platform / Software
- Host OS: Fedora 43
- Secondary OS: Windows 10 (gaming and OS-required applications) 

### Workloads / Purpose
- Primary personal workstation
- Homelab command center
- Windows 10: Gaming and OS-required general-purpose computing(e.g., certification testing)

# Home Server

### Hardware
Cyberpower prebuild, upgraded ram and CPU cooler

| CPU     | Intel(R) Core(TM) i7-8700 CPU @ 3.20GHz 6-Core                                                         |
| ------- | ------------------------------------------------------------------------------------------------------ |
| GPU     | MSI GeForce GTX 1060 6GB                                                                               |
| Mobo    | ASRock B360M Xtreme                                                                                    |
| PSU     | CyberPower OEM ATX PSU (model not software-detectable)                                                 |
| RAM     | CORSAIR - VENGEANCE LPX 32GB (2x16GB) DDR4 3200MHz                                                     |
| Storage | 240GB WD Green 2.5-inch SATA III Solid State Drive (SSD)<br>1TB WD Blue internal hard disk drive (HDD) |
### Platform / Software
- Host OS: Proxmox VE 9.x (Debian-based)
- Virtualization:
	- WindowsServer2025 (AD / testing)
	- Windows 11 (client testing)
	- Ubuntu Server (general services)
	- Arch Linux (documentation reference / Arch Wiki only)
- Container runtime
	- Docker
		- Docker Compose
			- Mediamtx
			- Jellyfin
			- Tailscale
			- Caddy
			- filebrowser
	- Custom Docker startup script to resolve port conflicts
- Key system-level services: N/A (not built on host)

### Workloads / Purpose
- Homeserver for media hosting (remote DnD session recording and library)
- Virtualized test environment (system breakage and recovery)
- Evolving homeserver as I learn of new projects to build
# Network Host

### Hardware
Lenovo m900 thinkcentre SFF

| CPU     | Intel Core i5-6500                |
| ------- | --------------------------------- |
| GPU     | Intel HD Graphics 530             |
| Mobo    | LENOVO 30BC                       |
| PSU     | Lenovo OEM PSU                    |
| RAM     | 8GB                               |
| Storage | Samsung SSD 850 PRO 256GB         |
| NIC     | Intel I350 Gigabit Network 2 port |
### Platform / Software
- Host OS: Proxmox VE 9.x (Debian-based)
- Virtualization:
	- pfSense
- Container runtime
	- MongoDB-backed UniFi Network Controller (containerized)
- Key system-level services:
	- Cron-scheduled maintenance tasks
	- Automated update and orchestration scripts

### Workloads / Purpose
- Primary purpose is to host pfSense and other network utilities
- Centralized automation node for the entire homelab, responsible for home server uptime (5pm–12am) and orchestrating updates and maintenance across all hosts, VMs, containers, and the Raspberry Pi via scripts and cron.

# Network Infrastructure
- Network host (router)
- Cisco Catalyst 2960L 8-Port PoE+ (managed switch)
- Ubiquiti UniFi UAP-AC-Pro (wireless access point)
- Raspberry Pi (Ubuntu Server) – temporary network edge / Wi-Fi to Ethernet bridge
