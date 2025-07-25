---
obsidianUIMode: preview
Language: 
Category: 
Topic: 
Type: 
System: 
Element type: 
Arguments: 
Source: 
Complexity: 
Keywords: 
aliases: 
DateCreated: 
LastEdited:
---
<%*
const hasTitle = !tp.file.title.startsWith("Untitled");
let title;
if (!hasTitle) {
    title = await tp.system.prompt("Enter Note Title");
    await tp.file.rename(title);
} else {
    title = tp.file.title;
}
_%>
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

# <%* tp.file.cursor _%>_