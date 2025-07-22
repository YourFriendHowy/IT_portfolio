
> [!NOTE] Things to Know
> *May not be accurate*
> - Common for Folders and Directories to be colored blue.
> - White are files
> - Green are programs or binary
# Commands

```dataview
table WITHOUT ID link(file.name) AS "Command", Meaning, Function, Shortcut AS "Shortcuts", Flags AS "Flags", Actions
FROM "Linux_Notes"
where (Type = "Bash Command") 
```

| Command      | Meaning | Function                        | Shortcuts |
| ------------ | ------- | ------------------------------- | --------- |
| adduser      |         | creates new user; requires sudo |           |
| passwd       |         | change password                 |           |
| [[#userdel]] |         | deletes user; requires sudo     |           |
| groupadd     |         | creates new group               |           |
| groupdel     |         | deletes group                   |           |
# Shortcuts

| Shortcut | use                                                                                                                         |
| -------- | --------------------------------------------------------------------------------------------------------------------------- |
| `*`      | this symbol is used to represent everything in a directory, can be narrowed by file type ie *.txt references all .txt files |
| `.`      | represents current directory                                                                                                |
| `..`     | represents parent directory                                                                                                 |
| `~`      | represents home directory                                                                                                   |
# userdel
| Keyword/Flag | Meaning | Effect                 | Example |
| ------------ | ------- | ---------------------- | ------- |
| `-r`         |         | removes user and files |         |
# groups

- `sudo gpasswd -d user group`   removes user from group