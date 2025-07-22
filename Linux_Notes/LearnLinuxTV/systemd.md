---
obsidianUIMode: preview
Language: Bash
Category: Terminal
Topic: Bash
Type: Bash Commands
System: Linux
Element type:
  - Shell Built-in
Flags(y/n): "True"
Actions: "True"
Source: https://www.youtube.com/@LearnLinuxTV
Complexity: Beginner
Keywords: 
aliases: 
Last Edited: 2025-07-22
---
# systemctl
*may require sudo*
## Status
Loaded: loaded (/usr/lib/systemd/system/apache2.service; enabled; preset: enabled)
- enabled means startup on boot
- preset shows vendor default(enabled/disabled)
Active: active (running) since Sun 2025-07-20 11:22:32 EDT; 1min 34s ago
- shows current status


### Logging
>Jul 20 11:22:32 Hades-MS-7B93 systemd[1]: Starting apache2.service - The Apache HTTP Server...
>Jul 20 11:22:32 Hades-MS-7B93 apachectl[21581]: AH00558: apache2: Could not reliably determine the server>
>Jul 20 11:22:32 Hades-MS-7B93 systemd[1]: Started apache2.service - The Apache HTTP Server.

# journalctl
| Keyword/Flag | Meaning | Effect                                                                                            | Example |
| ------------ | ------- | ------------------------------------------------------------------------------------------------- | ------- |
| -u           | unit    | how messages for the specified systemd unit _UNIT_, or for any of the units matched by _PATTERN_. |         |
| -f           | follow  | output appended data as the file grows                                                            |         |