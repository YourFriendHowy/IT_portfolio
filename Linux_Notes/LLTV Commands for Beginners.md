
> [!NOTE] Things to Know
> *May not be accurate*
> - Common for Folders and Directories to be colored blue.
> - White are files
> - Green are programs or binary

| Command    | Meaning                      | Function                                                              | Shortcuts          |
| ---------- | ---------------------------- | --------------------------------------------------------------------- | ------------------ |
| [[#LS]]    | List Storage                 | Lists files and folders within folder                                 |                    |
| LS /       | List Storage /Base           | Lists folders and files at the base of the OS                         |                    |
| LS /home   | List storage /home Directory | Will list user directory                                              |                    |
| clear      | clears terminal              | clears Terminal                                                       | ctrl+l             |
| pwd        | Print Working Directory      | Tells you where you are right now                                     |                    |
| [[#cd]]    | Change Directory             | Lets you change your directory location                               | TAB(auto-complete) |
| [[#touch]] |                              | creates a new file with filename you enter. file cannot already exist |                    |
| [[#nano]]  |                              | opens text editor                                                     |                    |
| cat        | Concatenate                  | shows contents of file                                                |                    |
| which      |                              | used to search for command presence. Shows full path                  |                    |
| [[#vim]]   | Vi IMproved                  | text editor                                                           |                    |
| [[#cp]]    | copy                         | duplicates a file from one location to another                        |                    |
| diff       | difference                   | outputs lines that differ                                             |                    |
| [[#rm]]    | remove                       | removes file entered after command                                    |                    |
| mkdir      | make directory               | creates a new directory/folder                                        |                    |
| [[#mv]]    | move                         | moves file from one directory to another or used to rename a file.    |                    |
| alias      |                              | lists current aliases                                                 |                    |
| [[#chmod]] |                              | changes permissions                                                   |                    |
|            |                              |                                                                       |                    |
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
|                                   |                                                             |
|                                   |                                                             |
|                                   |                                                             |
|                                   |                                                             |
|                                   |                                                             |


# LS
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
> [!hint] tips
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
