---
obsidianUIMode: preview
Language: Bash
Category: Commands
Topic: Terminal
Type: Bash Command
System: Linux
Element type:
  - Shell Built-in
Arguments: Y
Source: https://www.youtube.com/@LearnLinuxTV
Complexity: Intermediate
Keywords: 
aliases: 
Meaning: Change Mode
Function: Changes file or directory permissions
Shortcut: N/A
Built-in: "True"
Last Edited: 2025-07-22
---
>[!infobox]
> # Command: `=this.file.name`
> Category |  Info |
> ---|---|
> System|`=this.System`
> Languages|`=this.Language`
> Meaning|`=this.Meaning`
> Function| `=this.Function`
> Shortcut|`=this.Shortcut`

| Flag/Action/Keyword | Meaning           | Effect                                                                                           | Example |
| ------------------- | ----------------- | ------------------------------------------------------------------------------------------------ | ------- |
| `+`                 | add permission    | `+x`, add execute permission<br>`+r`, add read permission<br>`+w`, add write permission          |         |
| `-`                 | remove permission | `-x`, remove execute permission<br>`-r`, remove read permission<br>`-w`, remove write permission |         |
| `u`                 | user (file owner) | `u+x`: give execute permission to the file owner                                                 |         |
| `g`                 | group             | `g+x`: give execute permission to the group                                                      |         |
| `o`                 | others            | `o+x`: give execute permission to others                                                         |         |
| `a`                 | all               | `a+x`: give execute permission to all (user, group, and others)                                  |         |
