---
obsidianUIMode: preview
Language: Bash
Category: Glossary
Topic: Systemd
Type: Definition
System: Linux
Element type: 
Flags(y/n): "False"
Actions: "False"
Source: https://www.youtube.com/@LearnLinuxTV
Complexity: Beginner
Keywords: 
aliases: 
Last Edited: 2025-07-22
---

| Term         | Explanation                                                                                                 |
| ------------ | ----------------------------------------------------------------------------------------------------------- |
| Load Average | Number of processes waiting for CPU time                                                                    |
| Values       | 3 numbers: 1-minute, 5-minute, and 15-minute averages                                                       |
| Source       | Displayed by `uptime` and stored in `/proc/loadavg`                                                         |
| Meaning      | 1.00 = one full core used; values exceeding total CPU core count indicate CPU is overloaded (tasks waiting) |

## Example 
14:32:01 up 3 days,  4:27,  2 users,  load average: 0.58, 0.40, 0.36

'0.** ' Load shows how many tasks are waiting on the cpu