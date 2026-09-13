---
obsidianUIMode: preview
Category: Study
Topic:
  - CompTIA A+
Type: Notes
System: Any
Source:
  - https://www.youtube.com/professormesser
Complexity: Beginner
Keywords: 
LastEdited: 2025-07-23
---

| Protocol | Port       | Name                              | Description                                    |
|----------|------------|-----------------------------------|------------------------------------------------|
| FTP      | tcp 20/21  | File Transfer Protocol            | Active (data) & control channels               |
| SSH      | tcp 22     | Secure Shell                      | Encrypted remote access                        |
| Telnet   | tcp 23     | Telnet                            | Unencrypted remote console                     |
| SMTP     | tcp 25     | Simple Mail Transfer Protocol     | Sending mail between servers                   |
| DNS      | tcp/udp 53 | Domain Name System                | Hostname ↔ IP resolution                       |
| DHCP     | udp 67/68  | Dynamic Host Configuration Proto. | Assigning IPs to clients                       |
| HTTP     | tcp 80     | HyperText Transfer Protocol       | Unencrypted web traffic                        |
| POP3     | tcp 110    | Post Office Protocol v3           | Retrieving mail (download & delete)            |
| NetBIOS  | udp/tcp 137–139 | NetBIOS / NetBIOS Session   | Name resolution & Windows file/printer sharing |
| IMAP     | tcp 143    | Internet Message Access Protocol  | Mail retrieval with server‑side sync           |
| SNMP     | udp 161/162| Simple Network Mgmt Protocol      | Device monitoring (query/trap)                 |
| LDAP     | tcp 389    | Lightweight Directory Access Prot.| Directory services                             |
| HTTPS    | tcp 443    | HTTP Secure                       | Encrypted web traffic                          |
| SMB      | tcp 445    | Server Message Block (CIFS)       | Windows file/printer/network sharing           |
| RDP      | tcp 3389   | Remote Desktop Protocol           | Graphical remote desktop access                |

# IPv4 sockets
- Server IP address, protocol, server application port number
- Client IP address, protocol, client port number
# Non-ephemeral ports - permanent port numbers
- Ports 0 through 1,023
- Usually on a server or service
- Port 80 commonly associated with HTTP
- Port 443 commonly associated with HTTPS
# Ephemeral ports - temporary port numbers
- Ports 1,024 through 65,535
- Determined in real-time by the client

# Port Numbers
### TCP and UDP ports can be any number between 0 and 65,535
### Most servers(services) use non-ephemeral port numbers
- This isn't always the case
	- its just a number
## Port numbers are for communication, not security
## Service port numbers need to be "Well Known"
## TCP port numbers aren't the same as UDP port numbers, they serve as different lanes on the same highway

# Ports on the Network
![[Pasted image 20250723221731.png]]
## Comparison of port numbers
- source ports are random
- destination port is the "well known" port
![[Pasted image 20250723221815.png]]


# Port numbers
### Well-known port number
- Client and server need to match
### Important for firewall rules
- Port-based security
### A bit of rote memorization
- Becomes second nature after a while
## Make sure you know port number, protocol and how protocol is used


## FTP - File Transfer Protocol
#### TCP port 20(Active mode data), TCP port 21(Controls data transfer)
- Transfers files between systems
#### Authenticates with username and password
- Some systems use a generic/anonymous login
#### Full-featured functionality
- List, add, delete, and other file management functions
## SSH - Secure Shell
#### Encrypted communication link TCP port 22
#### Looks and acts the same as Telnet
## Telnet
#### Telnet - Telecommunication network 
- TCP port 23
#### Login to devices remotely
- Console access
#### In-the-clear communication
- non-encrypted, unsecured
- Not the best choice for production systems

## SMTP - Simple Mail Transfer Protocol
#### SMTP - Simple mail transfer protocol
- Server to Server email transfer
- TCP port 25
#### Also used to send mail from a device to mail server
- Commonly configured on mobile devices and email
#### Other protocols are used for clients to receive email
- IMAP, POP3
## DNS - Domain Name System
#### Converts names to IP addresses - UDP port 53
- www.professormesser.com = 162.159.246.164
#### These are very critical resources
- Usually multiple DNS servers are in production
## DHCP - Dynamic Host Configuration Protocol
#### Automated configuration of IP address, subnet mask and other options
- UDP ports 67 and 68
- Requires a DHCP server
	- Server, appliance, integrated into SOHO router, etc
#### Dynamic/pooled
- IP addresses are assigned in real-time from a pool
- Each system is given a lease and must renew at set intervals
#### DHCP reservation
- Addresses are assigned by MAC address in the DHCP server
- Manage addresses from one location
## HTTP and HTTPS
#### Hypertext Transfer Protocol
- Communication in the browser
- And by other applications 
###### HTTP TCP port 80
- web server communication
###### HTTPS TCP port 443
- Web server communication with encryption
#### POP3/IMAP
###### Receive emails from an email server
- authenticate and transfer
###### POP3 - Post office protocol version 3
- port TCP 110
- Basic mail transfer functionality
###### IMAP4 - Internet message access protocol v4
- Port TCP 143
- Includes management of email inbox from multiple clients
#### SMB - Server message block
###### Protocol used by Microsoft windows
- File sharing, printer sharing
- Also called CIFS(Common internet file System)
###### Using NetBIOS over TCP/IP (Network basic input/Output system)
- Port UDP 137 - NetBIOS name services (nbname)
- Port TCP 139 - NetBIOS session service (nbsession)
###### Direct SMB connection over port TCP 445 (NetBIOS-less)
- Direct SMB communication over TCP without NetBIOS transport
