# 2026-1-10
Today I moved from pfSense to OPNsense and began setting up a more hardened network and using VLANs. this is what I';ve completed today.

Starting out strong with downloading a .img installation media for OPNsense and not a .iso. 

## Router/Firewall Config

`10.42.0.1` = *gateway*

`10.42.1.*` = *VLAN1 default*

`10.42.5.*` = *VLAN5; AP and guest connectivity*

`10.42.10.*` = *VLAN10; Security/tools lab VLAN*

`10.42.15.*` = *VLAN15; Proxmox services2*

`10.42.20.*` = *VLAN20; private services with tailscale tunnel

`10.42.30.*` = *VLAN30; public services with tailscale funnel*

`10.42.99.*` = *VLAN99;Network management plane, network services(firewall, AP control panel, pihole control panel, upstream PI access.*

`10.42.100.*` = *VLAN100; user plane, jump host VM, anything I directly log into (proxmox management)*

### IP addressing and VLAN assignments

**Desktop(Hades):** VLAN100; 10.42.100.* (DHCP); *hades.homelab.arpa*
**Server(Underworld):** VLAN100(on trunk); 10.42.100.2; *underworld.homelab.arpa*
**Control VM(Zeus):** same as host(VLAN100); 10.42.100.5; *zeus.homelab.arpa*

**Access point/Guest network:** VLAN5; 10.42.5.* (DHCP);

**Kali linux(Hephaestus):** VLAN10; 10.42.10.2; *heph.homelab.arpa*

**MediaMTX and Jellyfin(Hermes):** VLAN20; 10.42.20.20; *hermes.homelab.arpa*

**EdgeLXC(Apollo):** VLAN30; 10.42.30.30; *apollo.homelab.arpa*

**NetworkMGMT host(Olympus):** VLAN99; 10.42.99.2; *olympus.homelab.arpa*
**OPNsense(Athena):** VLAN99; 10.42.99.1; *athena.homelab.arpa*
**PI-hole controller(Prometheus):** VLAN99; 10.42.99.14; *prom.homelab.arpa*
**Switch webUI(Proteus):** VLAN99; 10.42.99.49; *proteus.homelab.arpa*
**Unifi controller(Helios):** untagged VLAN99; 10.42.99.25; *helios.homelab.arpa*

**Raspberry PI pseudo modem(Hyperion):** VLAN99; 10.42.99.222(placeholder, need to locate real IP); *hyper.homelab.arpa*

### VLAN DHCP conventions: VLAN* (`10.42.*.0/24`)

| Range                       | Purpose                         |
| --------------------------- | ------------------------------- |
| `10.42.*.1`                 | Gateway (OPNsense interface IP) |
| `10.42.*.2 – 10.42.*.49`    | Static infrastructure           |
| `10.42.*.50 – 10.42.*.199`  | DHCP pool                       |
| `10.42.*.200 – 10.42.*.254` | Reserved / future               |


## Switch settings
Empty ports on vlan5

**Port 1:** Trunk
**Port 2:** Empty
**Port 3:** VLAN100
**Port 4:** Empty
**Port 5:** Trunk(VLAN100, VLAN30, VLAN20, VLAN15, VLAN10)
**Port 6:** Empty
**Port 7:** Trunk(VLAN5, untagged VLAN99)
**Port 8:** Empty