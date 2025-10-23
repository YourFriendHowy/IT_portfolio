---
obsidianUIMode: preview
Language: N/A
Category: Networking
Topic: Networking Basics
Type: Notes
System: Any
Element type: Concept
Arguments: N
Source: TestOut / Professor Messer / personal notes
Complexity: Beginner
Keywords:
  - Networking
  - A+
  - TCP/IP
  - Commands
  - Fundamentals
aliases: Networking Basics
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
> # Important
> - Remember private IPv4 ranges: 10.0.0.0/8 · 172.16.0.0/12 · 192.168.0.0/16

# Networking Basics

Quick reference for networking fundamentals covered in CompTIA A+.  
Focuses on key concepts, basic troubleshooting, and common commands used in Windows and Linux.

---

## IP Addressing
- **IPv4:** 32-bit, written as four octets (e.g., 192.168.1.10).  
- **IPv6:** 128-bit, written in hexadecimal (e.g., fe80::1).  
- **Subnet Mask:** Defines which part of the address is the network and which is the host.  
- **Gateway:** Usually the router — default path out of the local network.  
- **DNS:** Translates names to IP addresses.  
- **DHCP:** Automatically assigns IP information to devices.

---

## Common Network Types
| Network | Description |
|----------|--------------|
| LAN | Local Area Network — home or small office |
| WAN | Wide Area Network — connects multiple LANs |
| WLAN | Wireless LAN — Wi-Fi network |
| PAN | Personal Area Network — Bluetooth, tethering |
| VPN | Virtual Private Network — encrypted remote connection |

---

## Protocols & Ports
| Protocol | Port    | Purpose                              |
| -------- | ------- | ------------------------------------ |
| HTTP     | `80`    | Web traffic                          |
| HTTPS    | `443`   | Secure web traffic                   |
| FTP      | `21`    | File transfer                        |
| SSH      | `22`    | Secure remote access                 |
| Telnet   | `23`    | Insecure remote access (avoid using) |
| DNS      | `53`    | Name resolution                      |
| DHCP     | `67/68` | IP assignment                        |
| SMTP     | `25`    | Send email                           |
| POP3     | `110`   | Receive email                        |
| IMAP     | `143`   | Email sync                           |
| RDP      | `3389`  | Remote Desktop                       |
| SMB      | `445`   | File/printer sharing (Windows)       |

---

## Basic Network Commands
| Task | Windows | Linux / macOS | Notes |
|------|----------|----------------|-------|
| View IP info | `ipconfig /all` | `ip a` | Shows adapters and IPs |
| Test connectivity | `ping <address>` | `ping <address>` | Use `-n` (Win) or `-c` (Linux) for count |
| Trace route | `tracert <address>` | `traceroute <address>` | Shows hops to destination |
| DNS lookup | `nslookup <domain>` | `dig <domain>` | Confirms DNS resolution |
| View ARP table | `arp -a` | `ip neigh` | Shows cached MAC addresses |
| Check routing table | `route print` | `ip route` | Shows how packets leave system |
| Open connections | `netstat -an` | `ss -tuna` | Active ports and connections |
| Release/Renew DHCP | `ipconfig /release` / `ipconfig /renew` | `dhclient -r` / `dhclient` | Refresh network lease |

---

## Troubleshooting Flow
1. **Check physical connection** (cables, Wi-Fi link).  
2. **Verify IP address** (`ipconfig` or `ip a`).  
3. **Ping gateway** to confirm LAN reachability.  
4. **Ping external host** to confirm internet access.  
5. **Check DNS** if ping by IP works but not by name.  
6. **Restart adapter** or **release/renew IP** if needed.  

---

## Notes
This note is meant for quick review of basic networking concepts, ports, and commands that tie into A+ fundamentals.  
Any actual configurations, lab builds, or troubleshooting logs go into projects.
