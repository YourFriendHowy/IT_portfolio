---
obsidianUIMode: preview
Language: 
Category: ProgressJournal
Topic: 
Type: 
Systems: 
Source: 
Keywords: 
VaultUpdates: 
Time: 
TypeTime:
---
<%*
const hasTitle = !tp.file.title.startsWith("Untitled");

var date = moment();

var currentDate = date.format('YYYY-MM-DD')

let title;
if (!hasTitle) {
    title = currentDate;
    await tp.file.rename(title);
} else {
    title = tp.file.title;
}
_%>
>[!infobox]
> ###### `=this.file.name` Summary
> Type |  Stat |
> ---|---|
> Systems used|`=this.System`
> Languages studied|`=this.Language`
> Changelog|`=this.VaultUpdates`
> Study Sources| `=this.Sources`
> Time Spent Studying|`=this.Time`
> Keyboard Practice|`=this.TypeTime`
### What I did today:
*Breakdown today's lessons, using commit styled bullets*
- Learned the difference between `apt` and `apt-get`
- Experimented with custom callouts in Obsidian
- Refined Linux vault structure by separating tools vs concepts

### Vault Updates:
*link changlog, touch on anything major*
- Created [[Linux/Apt Commands]]
- Updated [[Obsidian/Style Guide]] with color tweaks

### Thoughts:  
*Short passage on the days progress" IE:Starting to grasp package management more fluently. Found a good rhythm in taking notes while watching videos. Still need to research `snap` vs `flatpak`.*

---
#### **Tomorrow**

- 
- 
#### **Future**
- 
