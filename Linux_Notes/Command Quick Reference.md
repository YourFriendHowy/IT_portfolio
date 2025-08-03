
> [!NOTE] Things to Know
> *May not be accurate*
> - Common for Folders and Directories to be colored blue.
> - White are files
> - Green are programs or binary
# Commands

```dataview
table WITHOUT ID link(file.name) AS "Command", Meaning, Function, Shortcut AS "Shortcuts", Arguments
FROM "Linux_Notes"
where (Type = "Bash Command") 
```
# Shell Shortcuts

| Shortcut | use                                                                                                                         |
| -------- | --------------------------------------------------------------------------------------------------------------------------- |
| `*`      | this symbol is used to represent everything in a directory, can be narrowed by file type ie *.txt references all .txt files |
| `.`      | represents current directory                                                                                                |
| `..`     | represents parent directory                                                                                                 |
| `~`      | represents home directory                                                                                                   |
# Shell Operators

| Symbol / Operator | Description                                                                                                                                      |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `&`               | This operator allows you to run commands in the background of your terminal.                                                                     |
| `&&`              | This operator allows you to combine multiple commands together in one line of your terminal.                                                     |
| `>`               | This operator is a redirector - meaning that we can take the output from a command (such as using cat to output a file) and direct it elsewhere. |
| `>>`              | This operator does the same function of the `>` operator but appends the output rather than replacing (meaning nothing is overwritten).          |