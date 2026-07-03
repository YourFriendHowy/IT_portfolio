This Document is an overview of my current **homelab** in its entirety; it is **not intended to be fully detailed documentation**.

# Personal PC

### Hardware

This is a **custom build** I researched and assembled in **May 2020**.

|CPU|**AMD Ryzen 7 3800X** 3.9 GHz 8-Core|
|---|---|
|GPU|**MSI GAMING X TRIO GeForce RTX 2080 SUPER** 8 GB Video Card|
|Mobo|**MSI MPG X570 GAMING PRO CARBON WIFI**|
|PSU|**SeaSonic FOCUS PLUS 850 Gold** 850 W 80+ Gold Certified Fully Modular ATX Power Supply|
|RAM|**G.Skill Trident Z RGB** 32 GB (2 x 16 GB) DDR4-3600|
|Storage|**Samsung 860 Evo** 500 GB 2.5" SSD,  <br>**WD_BLACK** 4 TB 3.5" 7200 RPM HDD|

### Platform / Software

- **Host OS:** Fedora 43
    
- **Secondary OS:** Windows 10 (gaming and OS-required applications) may switch this to bazzite
    
- Both OS are installed on the same ssd, plans are to put bazzite on a partition on the 4tb hdd and use the other partition for gaming. this is undecided at the moment. Windows is required to take pearson vue tests, cant be a VM. this has me holding off, the 80gb provided for windows is full, no updates for windows 10 or drivers can be patched, win10 at eol. 
### Workloads / Purpose

- **Primary personal workstation**
    
- **Homelab control and data command center**
    
- **Windows 10:** Gaming and OS-required general-purpose computing (e.g., certification testing)
    

---

# Home Server

### Hardware

Cyberpower **prebuilt**, upgraded **RAM** and **CPU cooler**

| CPU     | **Intel Core i7-8700** @ 3.20GHz 6-Core                    |
| ------- | ---------------------------------------------------------- |
| GPU     | **MSI GeForce GTX 1060** 6GB                               |
| Mobo    | **ASRock B360M Xtreme**                                    |
| PSU     | **CyberPower OEM ATX PSU** (model not software-detectable) |
| RAM     | **CORSAIR VENGEANCE LPX** 32GB (2x16GB) DDR4 3200MHz       |
| Storage | **WD Green** 240GB SSD,  <br>**WD Blue** 1TB HDD           |

### Platform / Software

- **Host OS:** Proxmox VE 9.x (Debian-based)
    
- Virtualization:
    
    - **WindowsServer2025** (AD / testing)
        
    - **Windows 11** (client testing)
        
    - **Ubuntu Server** (general services)
        
    - **Arch Linux** (documentation reference / Arch Wiki only)
        
- Container runtime
    
    - **Docker(on pve lxc, needs moved to a vm for security)**
        
        - **Docker Compose**
            
            - Mediamtx
                
            - Jellyfin
                
            - Tailscale
                
            - Caddy
                
            - filebrowser
                
    - **Custom Docker startup script** to resolve port conflicts
        
- Key system-level services: N/A (not built on host)
    

### Workloads / Purpose

- **Home server** for media hosting (remote DnD session recording and library)
    
- **Virtualized test environment** (system breakage and recovery)
    
- **Evolving home server** as I learn of new projects to build
    
- **This is the data machine currently**
---

# Network Host

### Hardware

**Lenovo M900 ThinkCentre** SFF

| CPU     | **Intel Core i5-6500**                  |
| ------- | --------------------------------------- |
| GPU     | **Intel HD Graphics 530**               |
| Mobo    | **LENOVO 30BC**                         |
| PSU     | **Lenovo OEM PSU**                      |
| RAM     | **8GB**                                 |
| Storage | **Samsung SSD 850 PRO** 256GB           |
| NIC     | **Intel I350** Gigabit Network (2-port) |

### Platform / Software

- **Host OS:** Proxmox VE 9.x (Debian-based)
    
- Virtualization:
    
    - **opnSense**
        
- Container runtime
    
    - **MongoDB-backed UniFi Network Controller** (containerized docker on lxc, needs moved to vm, would like to actually do thius on the laptop that has pihole)
        
- Key system-level services(broken):
    
    - **Cron-scheduled maintenance tasks**
        
    - **Automated update and orchestration scripts**
        

### Workloads / Purpose

- **Primary purpose:** host pfSense and other **network utilities**
    
- **Centralized automation node** for the entire homelab, responsible for **home server uptime (5pm–12am)** and orchestrating **updates and maintenance** across all hosts, VMs, containers, and the Raspberry Pi via **scripts and cron**
    

# Network Services

### Hardware

**Asus k55a 2012 i5**

### Platform / Software

- **Host OS:** Debian 13.1

### Workloads / Purpose

- **Primary purpose:** Pi-hole and network services host
---

# Network Infrastructure

- **Network host** (router) netgear
    
- **Cisco Catalyst 2960L** 8-Port PoE+ (managed switch)
    
- **Ubiquiti UniFi UAP-AC-Pro** (wireless access point)
    
- **Raspberry Pi (Ubuntu Server)** – temporary network edge / Wi-Fi to Ethernet bridge