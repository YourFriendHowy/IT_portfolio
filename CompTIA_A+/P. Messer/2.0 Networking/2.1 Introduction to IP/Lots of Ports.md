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
> -

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
- non-encrypted, unsecure
- Not the best choice for production systems

## SMTP - Simple Mail Transfer Protocol
#### SMTP - Simple mail transfer protocol
- Server to Server email transfer
- TCP port 25
#### Also used to send mail from a device to mail server
- Commonly configured on mobile devices and email
