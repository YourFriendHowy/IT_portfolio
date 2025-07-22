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

drwxrwxr-x
1234567890
││││││ └─  (0) Others: execute
│││ ││└─── (9) Others: write
│││ │└──── (8) Others: read
│││ └───── (7) Group: execute
││└─────── (6) Group: write
│└──────── (5) Group: read
├───────── (4) User: execute
├───────── (3) User: write
└───────── (2) User: read
           (1) File type (`d` = dir, `-` = file)


## For directories:

- **Read (`r`)**: Allows you to **list the contents** of the directory (see filenames).
- **Write (`w`)**: Allows you to **add, rename, or delete** files/directories inside.
- **Execute (`x`)**: Allows you to **enter (cd into)** the directory and access files/subdirectories inside.

All three permissions interact for full control. For example:

- Without `x`, you can’t `cd` into the directory, even if you can list files (`r`).
- Without `r`, you can’t list contents, but with `x` you can access files if you know their names.
- Without `w`, you can’t create or delete files in that directory.


