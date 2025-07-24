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
LastEdited: 2025-07-24
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

# <%* tp.file.cursor _%>