---
obsidianUIMode: preview
Category: Cyber-security
Topic:
  - Defensive
Type: Introduction
System: Any
Source:
  - TryHackMe.com
Complexity: Beginner
DateCreated: 2025-07-25
LastEdited:
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

# Task 1
- Introduces us to Defensive security, including blue teams.
- Training users about cyber security
- document and manage assets, cant protect what you aren't aware you have
- Keeping systems up to date.
- preventative security
- logging and monitoring
- Soc(Security operations Center)
- Threat intelligence
- Digital forensics and incident response (DFIR)
# Task 2
- Two main topics
	- SOC(Security operations Center)
	- DFIR(Digital forensics and incident response)
- Security operations Center (SOC)
	- Team of security professionals that monitor network and systems to detect malicious cyber activity
	- Vulnerabilities, patch weaknesses
	- Policy violations, Set and enforce
	- Unauthorized activity, Watch for users logging in off hours, or accessing data they shouldn't
	- Network intrusions, detect and prevent further damage
### Threat Intelligence
- Build knowledge before a threat not after, a Threat-informed Defense
### Digital Forensics and Incident Response (DFIR)
- Digital Forensics
- Incident Response
- Malware Analysis
###### Digital Forensics
- Forensics is the science of investigating crimes and establishing evidence.
- Began as computer forensics
- In digital forensics the focus shifts to analyzing evidence of an attack and its perpetrators and other areas such as intellectual property theft, cyber espionage, and possession of unauthorized content.
	- File system: analyzing a digital forensics image  of a systems storage reveals much information such as installed programs, created files, partially overwritten files, and deleted files.
	- System memory: If the attacker runs their malicious program in memory without saving it to the disk, taking a forensic image of the system memory is the best way to analyze its contents and learn about the attack.
	- System logs: Each client and server computer maintains different log files about what is happening. Log files provide plenty of information about what happened on a system/ Even of the attacker tries to clear their traces, some traces remain.
	- Network logs: Logs of the network packets that have traversed a network help answer more questions about whether an attack is occurring and what it entails.
###### Incident Response
- An incident typically refers to a data breach or cyber attack; however in some cases it can be something less critical such as misconfig, an intrusion attempt or policy violation. Incident response specifies the methodology that should be followed to handle such a case. The aim is to reduce damage and recover in the shortest time possible. Ideally you would develop a plan  that is ready for incident response.  
###### Malware Analysis
- Malware stands for malicious software. Software refers to programs, documents, and files you can save on a disk or send over the network. Malware includes many types, such as:
	- A virus is a piece of code that attached itself to a program. It is designed to spread from one computer to another and works by altering, overwriting, and deleting files once it infects a computer.
	- Trojan horse is a program that shows one desireable function but hides a malicious function underneath. For example, a victim might download a video player from a shady website that gives the attacker complete control over their system.
	- Ransomwsre is a mal;icious program that encrypts the users fikles. Encryption makesd the files unreadable without knowning the encryption password. The attacker offers the user the encryption password if the user is willing to pay a "ransom."
	- Malware analysis aims to learn about such malicious programs using various means:

		1. Static analysis works by inspecting the malicious program without running it. This usually requires solid knowledge of assembly language (the processor’s instruction set, i.e., the computer’s fundamental instructions).
		2. Dynamic analysis works by running the malware in a controlled environment and monitoring its activities. It lets you observe how the malware behaves when running.