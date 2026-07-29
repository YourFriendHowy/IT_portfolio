10![[Pasted image 20260126182730.png]]

## Router/Firewall Config

`10.42.0.1` = *gateway*

`10.42.1.*` = *VLAN1 default*

`10.42.5.*` = *VLAN5; Security/tools lab VLAN*

`10.42.10.*` = *VLAN10; AP and guest connectivity*

`10.42.15.*` = *VLAN15; Proxmox services2*

`10.42.20.*` = *VLAN20; private services with tailscale tunnel

`10.42.30.*` = *VLAN30; public services with tailscale funnel*

`10.42.99.*` = *VLAN99;Network management plane, network services(firewall, AP control panel, pihole control panel, upstream PI access.*

`10.42.100.*` = *VLAN100; user plane, jump host VM, anything I directly log into (proxmox management)*

### IP addressing and VLAN assignments


Fixed — AP moves to VLAN10.

**VLAN10 — Guest/AP Connectivity**

|Device (Codename)|IP|Hostname|
|---|---|---|
|Access Point / Guest Network|10.42.10.* (DHCP)|—|

**VLAN5 — Security/Tools Lab**

|Device (Codename)|IP|Hostname|
|---|---|---|
|Kali Linux (Hephaestus)|10.42.5.2|heph.homelab.arpa|

**VLAN20 — Private Services (Tailscale/internal)**

| Device (Codename)                                                                 | IP          | Hostname         |
| --------------------------------------------------------------------------------- | ----------- | ---------------- |
| Network Storage LXC (Moirai)                                                      | 10.42.20.10 | moirai.home.arpa |
| Atlas (formerly Hermes — MediaMTX, Jellyfin, Gitea, Filebrowser, Foundry, Termix) | 10.42.20.20 | atlas.home.arpa  |

**VLAN30 — Public Services (Tailscale Funnel / edge)**

| Device (Codename) | IP          | Hostname         |
| ----------------- | ----------- | ---------------- |
| Edge LXC (Apollo) | 10.42.30.30 | apollo.home.arpa |

**VLAN99 — Network Management Plane**

| Device (Codename)             | IP                               | Hostname           |
| ----------------------------- | -------------------------------- | ------------------ |
| Network Mgmt Host (Olympus)   | 10.42.99.2                       | olympus.home.arpa  |
| OPNsense (Athena)             | 10.42.99.1                       | athena.home.arpa   |
| Pi-hole Controller (Cerberus) | 10.42.99.7<br>currently on 100.7 | cerberus.home.arpa |
| Switch WebUI (Proteus)        | 10.42.99.49 / Serial console     | proteus.home.arpa  |
| Unifi Controller (Helios)     | 10.42.99.25 (untagged)           | helios.home.arpa   |

**VLAN100 — User Plane**

| Device (Codename)       | IP                                     | Hostname                |
| ----------------------- | -------------------------------------- | ----------------------- |
| Desktop (Hades)         | 10.42.100.* (DHCP)                     | hades.homelab.arpa      |
| Server (Underworld)     | 10.42.100.2 (on trunk)                 | underworld.homelab.arpa |
| Control VM (Zeus)       | 10.42.100.5                            | zeus.home.arpa          |
| Nextcloud (Delphi)      | 10.42.100.13:12321/12322 (to be moved) | delphi.home.arpa        |
| Home Assistant (Hestia) | 10.42.100.79:8123                      | hestia.home.arpa        |
| Vaultwarden (Aegis)     | 10.42.100.253                          | aegis.home.arpa         |

**Not Yet Built**

| Device (Codename)   | Status          |
| ------------------- | --------------- |
| Ollama (Prometheus) | Needs hardware  |
| Alfred (Iris)       | Needs hardw are |



many lxc and vm with unknown ip static and dhcp

### VLAN DHCP conventions: VLAN* (`10.42.*.0/24`)

| Range                       | Purpose                         |
| --------------------------- | ------------------------------- |
| `10.42.*.1`                 | Gateway (OPNsense interface IP) |
| `10.42.*.2 – 10.42.*.49`    | Static infrastructure           |
| `10.42.*.50 – 10.42.*.199`  | DHCP pool                       |
| `10.42.*.200 – 10.42.*.254` | Reserved / future               |


## Switch settings
Empty ports on vlan5

**Port 1:** Trunk in
**Port 2:** Empty
**Port 3:** VLAN100(LAN)(Hades)
**Port 4:** trunk 1,99 cerberus
**Port 5:** Trunk(VLAN100, VLAN30, VLAN20, VLAN15, VLAN10)(underworld)
**Port 6:** unknown to printer
**Port 7:** Trunk(VLAN1,VLAN10, untagged VLAN99)(AP)
**Port 8:** TRUNK(VLAN1, VLAN99)(Zeus)