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
Meaning: Advanced Package Tool
Function: Used to install, remove, and manage software packages on Debian-based systems
Shortcut: N/A
Built-in: "True"
Last Edited: 2025-07-22
---

| Command           | Meaning         | Function         | Shortcuts        |
| ----------------- | --------------- | ---------------- | ---------------- |
| `=this.file.name` | `=this.Meaning` | `=this.Function` | `=this.Shortcut` |

| Flag/Action/Keyword       | Meaning              | Effect                                                      | Example |
| ------------------------- | -------------------- | ----------------------------------------------------------- | ------- |
| `update`                  | Update package lists | Downloads updated package info from repositories            |         |
| `upgrade`                 | Upgrade packages     | Installs available updates for installed packages           |         |
| `dist-upgrade`            |                      |                                                             |         |
| `install`                 | Install package      | Installs specified package(s)                               |         |
| `remove`                  | Remove package       | Removes specified package(s) but keeps config files         |         |
| `purge`                   | Purge package        | Removes package(s) including configuration files            |         |
| `search`                  | Search packages      | Searches for package names matching a pattern               |         |
| `show`                    | Show package info    | Displays detailed info about a package                      |         |
| `autoremove`              | Auto-remove          | Removes unused dependencies                                 |         |
| `clean`                   | Clean cache          | Removes downloaded package files (.deb) from cache          |         |
| `check`                   | Check package status | Checks for broken dependencies                              |         |
| `-y`                      | Assume yes           | Automatically answers 'yes' to prompts                      |         |
| `--purge`                 | Remove configs       | Removes config files when removing packages                 |         |
| `--simulate / -s`         | Dry run              | Simulates actions without making changes                    |         |
| `--reinstall`             | Reinstall package    | Forces reinstallation of installed package                  |         |
| `--no-install-recommends` | Skip recommended     | Installs only main packages, skips recommended dependencies |         |
| `--fix-broken`            | Fix broken packages  | Attempts to fix broken package dependencies                 |         |
