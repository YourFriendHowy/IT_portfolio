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

# Connectionless
- no formal open or close to the connection
# "Unreliable" delivery
- No Error recovery
- No reordering of data or retransmissions
# No flow control
- Sender determines the amount of data transmitted

# Why would you ever use UDP?
### Real-time communication
- There's no way to stop and resend data
- Time doesn't stop for your network
### Connectionless protocols
- DHCP(Dynamic Host Configuration Protocol)
- TFTP(Trivial File Transfer Protocol)
### The data might not get through
- The application keeps track and decides what to do
- It might not do anything