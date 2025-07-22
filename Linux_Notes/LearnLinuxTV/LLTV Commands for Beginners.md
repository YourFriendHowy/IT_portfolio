
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

| Command        | Meaning                    | Function                                                                                          | Shortcuts                                 |
| -------------- | -------------------------- | ------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| [[#cd]]        | Change Directory           | Changes current directory; supports TAB for auto-completion                                       |                                           |
| [[#touch]]     | Create File                | Creates a new empty file; file must not already exist                                             |                                           |
| [[#nano]]      |                            | Opens the nano text editor                                                                        |                                           |
| cat            | Concatenate                | Displays contents of a file                                                                       |                                           |
| which          | Command Location           | Shows full path of a command/executable                                                           |                                           |
| [[#vim]]       | Vi IMproved                | Opens the vim text editor                                                                         |                                           |
| [[#cp]]        | copy                       | Copies a file from one location to another                                                        |                                           |
| diff           | difference                 | Shows line differences between two files                                                          |                                           |
| [[#rm]]        | remove                     | Deletes a file                                                                                    |                                           |
| mkdir          | make directory             | Creates a new directory/folder                                                                    |                                           |
| [[#mv]]        | move                       | Moves or renames a file or directory                                                              |                                           |
| alias          | alias                      | Lists current shell aliases                                                                       |                                           |
| [[#chmod]]     | Change Mode                | Changes file or directory permissions                                                             |                                           |
| [[#free]]      | Free Memory                | Displays memory usage statistics                                                                  |                                           |
| [[#df]]        | disk free                  | Shows disk storage usage per filesystem                                                           |                                           |
| htop           | Interactive Process Viewer | Shows real-time system processes, CPU, memory, and resource usage with a user-friendly interface. | Use arrow keys to navigate, `F10` to quit |
| uptime         | System Uptime              | Shows how long the system has been running, number of users, and load average                     |                                           |
| [[#apt]]       | Advanced Package Tool      | Used to install, remove, and manage software packages on Debian-based systems                     |                                           |
| [[#sudo]]      | Superuser Do               | Runs a command with elevated (root) privileges                                                    |                                           |
| [[#systemctl]] |                            |                                                                                                   |                                           |
| head           |                            | reads first 10 lines of file                                                                      |                                           |
| tail           |                            | reads last 10 lines of file                                                                       |                                           |
| [[#groups]]    |                            | list groups of user                                                                               |                                           |
| adduser        |                            | creates new user; requires sudo                                                                   |                                           |
| passwd         |                            | change password                                                                                   |                                           |
| [[#userdel]]   |                            | deletes user; requires sudo                                                                       |                                           |
| groupadd       |                            | creates new group                                                                                 |                                           |
| groupdel       |                            | deletes group                                                                                     |                                           |
# Shortcuts

| Shortcut | use                                                                                                                         |
| -------- | --------------------------------------------------------------------------------------------------------------------------- |
| *        | this symbol is used to represent everything in a directory, can be narrowed by file type ie *.txt references all .txt files |
| .        | represents current directory                                                                                                |
| ..       | represents parent directory                                                                                                 |
| ~        | represents home directory                                                                                                   |

# alias
##### My Aliases
*stored in .bash_aliases*

| ..='cd ..'                        | changes directory to parent by entering '..'                |
| --------------------------------- | ----------------------------------------------------------- |
| ...='cd ../..'                    | changes directory to grandparent by entering '...'          |
| c='clear'                         | clears terminal by entering 'c'                             |
| obsidia='cd ~/repos/obsidia-bulk' | changes directory to my obsidia vault by entering 'obsidia' |
| rst='source ~/.bashrc'            | resets bash by entering 'rst'                               |
| edalias='nano .bash_aliases'      | opens .bash_aliases to be edited by entering 'edalias'      |
# ls
### Arguments (flags)
*can use multiples at once ie: -la longlists and shows all*

| Flag | meaning      | Effect                                                  | Alias |
| ---- | ------------ | ------------------------------------------------------- | ----- |
| -l   | long listing | shows more details and puts every item on its own line. | ll    |
| -a   | all          | shows all files and folders in directory                |       |

# home (~)

> [!tip] 
> "~"  refers to the home directory, for example "cd ~" will return you to the home directory.


# CD 
> [!tip]
> 'cd ~' will return you to the home directory

# touch

# nano
Is a text editor
> [!hint|right-small] tips
> '^' means control

- can use a file name as an argument to open and edit an existing file or create and edit a new file.

# vim
*Installed text editor*

# cp (Copy)
- 'cp oldfile.txt' newfile.txt copies oldfile.txt into newfile.txt

# rm (Remove)

> [!attention] Use Caution
> When rm is used file is removed completely, not moved to be deleted like recycling bin

### Arguments (flags)
| Flag | meaning   | Effect                                                                                                | Alias |
| ---- | --------- | ----------------------------------------------------------------------------------------------------- | ----- |
| -r   | recursive | it tells `rm` to delete a directory and **everything inside it**, including subdirectories and files. |       |
|      |           |                                                                                                       |       |

# mv

- '../file.txt .' moves file.txt from the parent directory to active directory.
- is used to rename files. 'mv file.txt newname.txt' 

# chmod

| Flag | meaning           | Effect                                                                                     | Alias |
| ---- | ----------------- | ------------------------------------------------------------------------------------------ | ----- |
| +    | add permission    | +x, add execute permission<br>+r, add read permission<br>+w, add write permission          |       |
| -    | remove permission | -x, remove execute permission<br>-r, remove read permission<br>-w, remove write permission |       |
| u    | user (file owner) | `u+x`: give execute permission to the file owner                                           |       |
| g    | group             | `g+x`: give execute permission to the group                                                |       |
| o    | others            | `o+x`: give execute permission to others                                                   |       |
| a    | all               | `a+x`: give execute permission to all (user, group, and others)                            |       |
# free

> [!NOTE] Title
> - free: truly free, not utilized at all
> - available: free + reclaimable in-use memory (like cached/buffered RAM that _could_ be freed if needed).

| Flag | meaning            | Effect                               | Alias |
| ---- | ------------------ | ------------------------------------ | ----- |
| -m   | megabytes          | outputs megabytes                    |       |
| -b   | bytes              | outputs bytes                        |       |
| -k   | kilobytes(default) | outputs kilobytes                    |       |
| -g   | gigabytes          | outputs gigabytes                    |       |
| -h   | human-readable     | outputs GB/MB for easier readability |       |
# df
| Flag | meaning            | Effect                                                            | Alias |
| ---- | ------------------ | ----------------------------------------------------------------- | ----- |
| -m   | megabytes          | outputs megabytes                                                 |       |
| -k   | kilobytes(default) | outputs kilobytes                                                 |       |
| -g   | gigabytes          | outputs gigabytes                                                 |       |
| -h   | human-readable     | Outputs sizes using appropriate units (GB, MB, etc.)              |       |
| -i   | Inodes             | Show inode usage (total, used, free inodes) instead of disk space |       |
# apt

| Keyword/Flag            | Meaning              | Effect                                                      | Alias |
| ----------------------- | -------------------- | ----------------------------------------------------------- | ----- |
| update                  | Update package lists | Downloads updated package info from repositories            |       |
| upgrade                 | Upgrade packages     | Installs available updates for installed packages           |       |
| dist-upgrade            |                      |                                                             |       |
| install                 | Install package      | Installs specified package(s)                               |       |
| remove                  | Remove package       | Removes specified package(s) but keeps config files         |       |
| purge                   | Purge package        | Removes package(s) including configuration files            |       |
| search                  | Search packages      | Searches for package names matching a pattern               |       |
| show                    | Show package info    | Displays detailed info about a package                      |       |
| autoremove              | Auto-remove          | Removes unused dependencies                                 |       |
| clean                   | Clean cache          | Removes downloaded package files (.deb) from cache          |       |
| check                   | Check package status | Checks for broken dependencies                              |       |
| -y                      | Assume yes           | Automatically answers 'yes' to prompts                      |       |
| --purge                 | Remove configs       | Removes config files when removing packages                 |       |
| --simulate / -s         | Dry run              | Simulates actions without making changes                    | -s    |
| --reinstall             | Reinstall package    | Forces reinstallation of installed package                  |       |
| --no-install-recommends | Skip recommended     | Installs only main packages, skips recommended dependencies |       |
| --fix-broken            | Fix broken packages  | Attempts to fix broken package dependencies                 |       |

# sudo
| Flag | Meaning              | Effect                                                        | Alias |
|------|----------------------|---------------------------------------------------------------|-------|
| -u   | User                 | Run command as specified user instead of root                 |       |
| -s   | Shell                | Run a shell instead of a command                              |       |
| -i   | Login shell          | Run login shell as the target user                            |       |
| -k   | Invalidate timestamp | Forget cached credentials (forces password prompt)           |       |
| -v   | Validate             | Update user's cached credentials without running a command   |       |
# systemctl
*[[systemd#systemctl|Documentation]]* 

| Keyword/Flag | Meaning | Effect                        | Alias |
| ------------ | ------- | ----------------------------- | ----- |
| status       |         | shows status of unit          |       |
| disable      |         | disables unit startup on boot |       |
| stop         |         | stops unit                    |       |
| start        |         | starts unit                   |       |
| restart      |         | restarts unit                 |       |

# head
| Keyword/Flag | Meaning   | Effect                                            | Example                               |
| ------------ | --------- | ------------------------------------------------- | ------------------------------------- |
| -n           | NUM lines | print the first NUM lines instead of the first 10 | -n 50; prints 50 rather than 10 lines |
# tail
| Keyword/Flag | Meaning   | Effect                                          | Example                               |
| ------------ | --------- | ----------------------------------------------- | ------------------------------------- |
| -n           | NUM lines | print the last NUM lines instead of the last 10 | -n 50; prints 50 rather than 10 lines |
| -f           | follow    | output appended data as the file grows          |                                       |
# userdel
| Keyword/Flag | Meaning | Effect                 | Example |
| ------------ | ------- | ---------------------- | ------- |
| -r           |         | removes user and files |         |
# groups

- 'sudo gpasswd -d user group'    # removes user from group