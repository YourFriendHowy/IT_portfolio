# Dotfiles & Userspace Documentation

**Author:** Howy  
**Last Updated:** <!-- DATE -->  
**Host(s) this applies to:** <!-- e.g. personal Arch laptop, Raspberry Pi (Hermes), etc. -->

---

## Table of Contents

1. [Overview](#overview)
2. [Repo Structure](#repo-structure)
3. [File Registry](#file-registry)
4. [Shell Environment](#shell-environment)
5. [Package List](#package-list)
6. [Application Configs](#application-configs)
7. [System-Level Configs](#system-level-configs)
8. [Services & Daemons](#services--daemons)
9. [Scripts & Bin Files](#scripts--bin-files)
10. [Fonts](#fonts)
11. [Secrets & Sensitive Files (DO NOT COMMIT)](#secrets--sensitive-files-do-not-commit)
12. [Symlink Map](#symlink-map)
13. [Bootstrap Order](#bootstrap-order)
14. [Known Issues / TODOs](#known-issues--todos)
15. [Changelog](#changelog)

---

## Overview

Brief description of what this dotfiles repo represents — your preferred userspace setup, what distro(s) it targets, and what the end goal is (e.g. reproducible setup on any fresh Arch install with one script).

**Target distro(s):** <!-- Arch Linux, Ubuntu, etc. -->  
**Primary shell:** <!-- bash / zsh / fish -->  
**Window manager / DE:** <!-- if applicable -->  
**Setup script:** `install.sh` <!-- or whatever you name it -->

---

## Repo Structure

How files are organized inside the repo itself. The repo layout should mirror where files live on the real system so the symlink logic stays simple.

```
dotfiles/
├── README.md                  # This file
├── install.sh                 # Symlink creator + bootstrap runner
├── packages.txt               # Master package list (pacman/apt/etc.)
├── shell/
│   ├── .bashrc
│   ├── .bash_profile
│   ├── .bash_aliases
│   └── .profile
├── git/
│   └── .gitconfig
├── vim/                       # or nvim/
│   └── .vimrc
├── tmux/
│   └── .tmux.conf
├── ssh/
│   └── config                 # Public/safe ssh config only — NO KEYS
├── scripts/                   # Custom bin scripts
│   └── example-script.sh
├── fonts/                     # Any manually installed fonts
└── <app>/                     # One directory per app
    └── config-file
```

> **Convention:** Each subdirectory in the repo maps to where those files live on the system. Files symlink from their real location (e.g. `~/.bashrc`) back to the repo copy (e.g. `~/dotfiles/shell/.bashrc`).

---

## File Registry

This is the single most important section. Every tracked file gets a row. Fill this out as you go — this is what your install script will read from.

|File in Repo|Symlink Target (live location)|Description|Notes|
|---|---|---|---|
|`shell/.bashrc`|`~/.bashrc`|Main bash config, sources aliases and profile|Loads on interactive non-login shell|
|`shell/.bash_profile`|`~/.bash_profile`|Login shell config, sets PATH|Runs on login|
|`shell/.bash_aliases`|`~/.bash_aliases`|All custom aliases|Sourced from .bashrc|
|`shell/.profile`|`~/.profile`|Fallback login config|Used if .bash_profile absent|
|`git/.gitconfig`|`~/.gitconfig`|Git identity + aliases + defaults|Replace email before committing publicly|
|`vim/.vimrc`|`~/.vimrc`|Vim config|<!-- describe key plugins/changes -->|
|`tmux/.tmux.conf`|`~/.tmux.conf`|Tmux keybinds + theme|<!-- describe prefix key etc -->|
|`ssh/config`|`~/.ssh/config`|SSH host aliases|NO private keys in repo|
|<!-- add rows -->||||

> **Adding a new file:** Drop it in the right repo subdirectory → add a row here → re-run `install.sh`.

---

## Shell Environment

### What changed from defaults and why

Document your deliberate changes here. This is the "what did I do" section that future-you needs to read.

#### PATH additions

```bash
# Added to .bash_profile or .profile:
export PATH="$HOME/.local/bin:$PATH"   # user-installed scripts
export PATH="$HOME/bin:$PATH"          # custom bin dir
# Add others here and explain why
```

#### Key environment variables

```bash
export EDITOR=vim          # default editor
export VISUAL=vim
export PAGER=less
# etc.
```

#### Aliases (notable ones)

Document any aliases that aren't obvious. Obvious ones (ll='ls -la') don't need explanation; non-obvious ones do.

```bash
alias gs='git status'          # self-explanatory shortcut
alias myalias='some command'   # EXPLAIN: what this does and why
```

#### Shell prompt / PS1

Describe any prompt customization. If using a framework (oh-my-bash, starship, etc.), note version and theme.

```
Framework: none / starship / oh-my-bash / etc.
Theme: <!-- -->
Config file: <!-- repo path -->
```

---

## Package List

Maintain a plain text package list so the install script can feed it to `pacman -S`, `apt install`, etc.

**File location in repo:** `packages.txt`

Group by category for readability:

```
# --- Core CLI tools ---
git
curl
wget
vim
tmux
htop
tree
unzip

# --- Networking ---
nmap
net-tools
openssh

# --- Development ---
python3
pip
nodejs
npm

# --- Shell enhancements ---
bash-completion
# starship (install separately via curl, not package manager)

# --- Add yours below ---
```

> **Note:** Some tools install via other methods (pip, npm, curl scripts, AUR, etc.). Document those separately below.

#### Non-package-manager installs

|Tool|Install method|Command / URL|Notes|
|---|---|---|---|
|starship|curl|`curl -sS https://starship.rs/install.sh \| sh`|Prompt framework|
|<!-- -->||||

---

## Application Configs

One subsection per app. Document: what changed, what the defaults were, and why you changed it.

---

### Vim / Neovim

**Config file in repo:** `vim/.vimrc`  
**Live location:** `~/.vimrc`  
**Plugin manager:** <!-- vim-plug, packer, lazy.nvim, none, etc. -->  
**Plugins installed:**

- `plugin-name` — reason you use it

**Key settings changed from default:**

```vim
set number          " line numbers — personal preference
set tabstop=4       " 4 space tabs
" explain any non-obvious setting
```

---

### Tmux

**Config file in repo:** `tmux/.tmux.conf`  
**Live location:** `~/.tmux.conf`  
**Prefix key:** <!-- Ctrl-b (default) / Ctrl-a / etc. -->  
**Plugin manager:** <!-- tpm or none -->

**Key changes:**

```bash
# Remap prefix to Ctrl-a
set -g prefix C-a   # REASON: habit from screen / easier reach
# Document others
```

---

### Git

**Config file in repo:** `git/.gitconfig`  
**Live location:** `~/.gitconfig`  
**Note:** Name and email are in the file — replace with your own before using publicly.

**Key settings:**

```ini
[core]
    editor = vim
[alias]
    st = status
    co = checkout
    # add others
```

---

### SSH

**Config file in repo:** `ssh/config`  
**Live location:** `~/.ssh/config`  
**What's documented here:** Host aliases only. No keys, no passwords.

```
Host homelab
    HostName 10.42.99.x
    User howy
    IdentityFile ~/.ssh/id_ed25519   # key not in repo — generate on each machine
```

---

### <!-- Next app -->

**Config file in repo:** `<app>/config-file`  
**Live location:** `~/<path>/config-file`  
**Changes:** <!-- -->

---

## System-Level Configs

Files that live outside `~` — typically in `/etc/` or require root. These generally should NOT be symlinked by the install script automatically. Document them so you can manually replicate them.

|File|Location|What it does|Replicate manually?|
|---|---|---|---|
|`etc/locale.conf`|`/etc/locale.conf`|Locale settings|Yes — copy manually post-install|
|<!-- -->||||

> Keep copies in a `system/` folder in the repo for reference, but don't auto-symlink `/etc/` files.

---

## Services & Daemons

Services you enable on a fresh install. Document so the install script can `systemctl enable` them.

|Service|Enabled at boot?|Notes|
|---|---|---|
|`sshd`|Yes|SSH server — enable immediately|
|`NetworkManager`|Yes||
|<!-- -->|||

---

## Scripts & Bin Files

Custom scripts that live in `~/bin/` or `~/.local/bin/`.

|Script|Location in repo|Live location|What it does|
|---|---|---|---|
|`example.sh`|`scripts/example.sh`|`~/.local/bin/example`|<!-- -->|
|<!-- -->||||

> All scripts in `scripts/` should be executable (`chmod +x`) and get symlinked to `~/.local/bin/` (without the `.sh` extension, optionally).

---

## Fonts

Any fonts installed manually outside the package manager.

|Font|Source / URL|Install location|Notes|
|---|---|---|---|
|<!-- font name -->|<!-- URL or included in repo under fonts/ -->|`~/.local/share/fonts/`|Run `fc-cache -fv` after installing|

---

## Secrets & Sensitive Files (DO NOT COMMIT)

These files are part of your setup but must **never** go into the repo. Document them here so you know to recreate them on a fresh install.

|File|Location|What to do on fresh install|
|---|---|---|
|`~/.ssh/id_ed25519`|`~/.ssh/`|Run `ssh-keygen -t ed25519 -C "your@email"`|
|`~/.ssh/id_ed25519.pub`|`~/.ssh/`|Add to GitHub, authorized_hosts, etc.|
|`~/.netrc`|`~/.netrc`|Recreate manually with credentials|
|<!-- -->|||

> Verify your `.gitignore` blocks all of these before your first push.

---

## Symlink Map

Quick-reference version of the File Registry. This is what `install.sh` is built from.

```
shell/.bashrc           → ~/.bashrc
shell/.bash_profile     → ~/.bash_profile
shell/.bash_aliases     → ~/.bash_aliases
shell/.profile          → ~/.profile
git/.gitconfig          → ~/.gitconfig
vim/.vimrc              → ~/.vimrc
tmux/.tmux.conf         → ~/.tmux.conf
ssh/config              → ~/.ssh/config
scripts/example.sh      → ~/.local/bin/example
```

> Format: `repo-relative-path → absolute-live-path`  
> The install script reads this section (or a separate `symlinks.txt`) to create all links.

---

## Bootstrap Order

The sequence your install script should follow on a fresh system. Order matters.

1. Install base packages from `packages.txt` via package manager
2. Install non-package-manager tools (see table above)
3. Create symlinks (run `install.sh`)
4. Set default shell if needed (`chsh -s /bin/bash`)
5. Install vim/tmux plugins (if plugin manager needs a separate step)
6. Generate SSH keys
7. Clone any private repos that depend on SSH
8. Enable systemd services
9. Install fonts + run `fc-cache -fv`
10. Reboot / log out and back in to apply shell changes

---

## Known Issues / TODOs

- [ ] <!-- e.g. tmux plugin install not yet automated -->
- [ ] <!-- e.g. need to document i3 config -->
- [ ] <!-- etc. -->

---

## Changelog

Brief log of significant changes. Not a substitute for git log — just big-picture notes.

| Date          | Change                        |
| ------------- | ----------------------------- |
| <!-- date --> | Initial documentation created |
| <!-- date --> | Added tmux config             |
| <!-- date --> | <!-- etc. -->                 |