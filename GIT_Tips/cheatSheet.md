---
obsidianUIMode: preview
Language: Bash
Category: Git
Topic: Git Commands
Type: Cheatsheet
System: Any
Element type:
  - Git Command
  - Shell
Flags(y/n): "True"
Actions: "True"
Source: https://www.theodinproject.com/lessons/foundations-git-basics
Complexity: Beginner
Keywords:
  - Git
  - Github
aliases: 
Last Edited: 2025-07-22
---
Commands related to a remote repository:
    - `git clone git@github.com:USER-NAME/REPOSITORY-NAME.git`
 `git push` or `git push origin main` (Both accomplish the same goal in this context)
Commands related to the workflow:
- `git add .`
- `git commit -m "A message describing what you have done to make this snapshot different"`
Commands related to checking status or log history
- `git status`
- `git log`

The basic Git syntax is `program | action | destination`.

For example,

- `git add .` is read as `git | add | .`, where the period represents everything in the current directory;
- `git commit -m "message"` is read as `git | commit -m | "message"`; and
- `git status` is read as `git | status | (no destination)`.