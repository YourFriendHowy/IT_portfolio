---
obsidianUIMode: preview
Language:
  - Bash
Category: Commands
Topic:
  - Terminal
Type: Bash Command
System: Linux
Element type: 
Arguments: 
Source: 
Complexity: 
Keywords: 
aliases: 
Meaning: 
Function: 
Shortcut: 
Built-in: 
Last Edited: ""
---

<%*
const hasTitle = !tp.file.title.startsWith("Untitled");
let title;
if (!hasTitle) {
    title = await tp.system.prompt("Enter Command");
    await tp.file.rename(title);
} else {
    title = tp.file.title;
}
_%>

>[!infobox]
> # Command: `=this.file.name`
> Category |  Info |
> ---|---|
> System|`=this.System`
> Languages|`=this.Language`
> Meaning|`=this.Meaning`
> Function| `=this.Function`
> Shortcut|`=this.Shortcut`
> # Important
> -

| Flag/Action/Keyword | Meaning | Effect | Example |
| ------------------- | ------- | ------ | ------- |
|                     |         |        |         |
|                     |         |        |         |
