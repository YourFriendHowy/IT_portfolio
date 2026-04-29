## Installing Arch Arm
[Youtube Guide](https://www.youtube.com/watch?v=WpCSOS_1vic)
- [Written Guide](https://kiljan.org/2023/11/24/arch-linux-arm-on-a-raspberry-pi-5-model-b/)
- [Current Version of Arch Arm](https://archlinuxarm.org/packages/aarch64/linux-rpi)
##### Issues
The following command had a 404 error solves by running `pacman -Syy && pacman -Su` then reran the command below. *There is suggestions for this error in the guide linked above*
```bash
pacman -Syu --overwrite "/boot/*" linux-rpi
```


## Generic stack Build
### git
*needed to pull script and install fonts and other things, must ssh to github account*
**Dependencies:** *openssh*
#### Installation
*Install using appropriate package manager for your system*
#### Initial Setup
```bash
# Configure git identity
git config --global user.name "Your Name"
git config --global user.email "yourname@example.com"

# Set default branch name
git config --global init.defaultBranch main

# Set merge strategy
git config --global pull.rebase false
```
#### SSH Key Setup
```bash
# Check existing ssh directory contents
ls ~/.ssh

# Check for existing key
ls ~/.ssh/id_ed25519.pub

# Generate new key if none exists
ssh-keygen -t ed25519 -C "yourname@example.com"

# Start ssh-agent
eval "$(ssh-agent -s)"

# Add key to agent
ssh-add ~/.ssh/id_ed25519

# Print public key - copy this output
cat ~/.ssh/id_ed25519.pub


# Manual step: paste output above into GitHub at github.com/settings/keys

# Test GitHub connection
ssh -T git@github.com
```
### wget
*Installed for kitty theme downloads*
#### Installation
*Install using appropriate package manager for your system*
### curl
### openssh
### ZSH
#### Installation
```bash
# Install using appropriate package manager for your system

# Making **Zsh** your default shell
chsh -s $(which zsh)
```
### oh-my-zsh
#### Installation
```bash
# Using wget
sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```
#### Themes
```bash
# Editing the .zshrc file
nano ~/.zshrc
# Rename the ZSH_THEME variable
ZSH_THEME="theme-name" _# e.g., half-life_
# Save and refresh .zshrc
source ~/.zshrc
```
#### Plugins
```
# Installing the zsh-syntax-highlighting plugin
`git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting`

# Installing the zsh-autosuggestions plugin
`git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions`

# Activating the plugins in the .zshrc file, 
plugins=(  
    _# other plugins..._  
	zsh-syntax-highlighting
    zsh-autosuggestions  
)
```

### Tmux
#### Installation
*Install using appropriate package manager for your system*
### fastfetch
### Base-devel
### Python3
### NVIM + Plugins
## Desktop only additions
### Hyprland
#### Installation
*Install using appropriate package manager for your system*
### Kitty
[Kitty Guide by Kevin Suñer](https://medium.com/better-programming/unleashing-your-terminal-with-kitty-and-zsh-102527d07a1c)
**Dependencies:** *git, wget*
#### Installation
*Install using appropriate package manager for your system*
#### Theme
  *Theme can be changed, [Themes can be found here!](https://github.com/dexpota/kitty-themes)*
```bash
# Set variable for theme
THEME=https://raw.githubusercontent.com/dexpota/kitty-themes/master/themes/AlienBlood.conf
  
# Downloads theme to specified directory
wget "$THEME" -P ~/.config/kitty/kitty-themes/themes

# Navigate to kitty config
cd ~/.config/kitty
  
# Symlink theme
ln -s ./kitty-themes/themes/AlienBlood.conf ~/.config/kitty/theme.conf

# Create kitty config file and add theme
echo "include ./theme.conf" > kitty.conf
```
#### Fonts
```bash
# Ready nerd-fonts
git clone --filter=blob:none --sparse git@github.com:ryanoasis/nerd-fonts

# Navigate to nerd-fonts directory
cd nerd-fonts

# Download nerd-fonts chosen font
git sparse-checkout add patched-fonts/Hack

# Install font
./install.sh Hack

# Add font to kitty
cd ~/.config/kitty && echo "font_family Hack Nerd Font Mono" > font.conf

# Add font to kitty.conf
echo "include ./font.conf" >> ~/.config/kitty/kitty.conf
```
### SDDM
### Superfile file manager
### Waybar
### Firefox(to be replaced possibly)
### rofi
### Obsidian
## CLI Monitoring build(Experimental)
*List of programs to test to find the ones I like*
### btop++
_Terminal resource monitor. Shows CPU, memory, disk, and network stats with live graphs. Runs on each host via SSH, one per tmux pane._

### glances
_Info-dense system monitor with network focus. Python-based. Best suited for Athena given its router/firewall role._
### bottom (btm)
_Lightweight Rust-based monitor. Minimal and fast, good for service hosts like Underworld._
### nmon
_Retro-aesthetic monitor, very old school block layout. Low overhead, good for LXC containers._
### lazydocker
_Docker and docker-compose TUI. Shows all containers, live logs, CPU/memory per container, compose stack groupings. Runs on Hermes._
### lnav
_Multi-source log aggregator and viewer. Pulls journalctl streams from multiple hosts and interleaves them with syntax highlighting and log-level colorization._
### gping
_Ping visualizer that renders latency as live terminal graphs. Run against all hosts simultaneously for a panoramic network health view across the bottom pane._
### speedtest-cli
_WAN speed test tool. Runs on a timer in a small corner pane, quietly logs upload/download speeds periodically._
### bmon
_Per-interface bandwidth monitor with live throughput graphs. Good for a dedicated network pane._
### iftop
_Live connection monitor showing active traffic between IPs, displayed as a ranked list. Strong hacker aesthetic._
### ccze
_Log colorizer. Pipes journalctl or other log output through it to add terminal-color highlighting without needing lnav._
### watch + custom script
_Shell-based service up/down tracker. Polls hosts and services via ping and curl, outputs a color-coded UP/DOWN list. Green on up, red on down. Refreshes every 30 seconds._
## Modern monitoring solutions
### Promtail
_Per-machine log shipping agent. Runs on every host and forwards logs to Loki. Configured per host to ship systemd journal and any service-specific log files._
### Loki
_Log aggregation backend. Receives log streams from all Promtail agents and indexes them for querying. Pairs directly with Grafana for unified log and metrics viewing._
### Prometheus Node Exporter
_Per-machine metrics exporter. Runs on every host and exposes system metrics on a local port for Prometheus to scrape. Covers CPU, memory, disk, network, and more._
### Prometheus
_Metrics collection and storage backend. Polls all node exporters on a schedule and stores time-series data. The data source for Grafana metrics dashboards._
### Grafana
_Unified observability dashboard. Connects to both Prometheus and Loki as data sources, displaying metrics and logs in a single interface. Community dashboard templates available for node exporter out of the box._
## Scripts 
### .zhrc helper scripts
*Directory: ~/.oh-my-zsh/custom/scripts.zsh*
```bash
#!/bin/bash

# Show a directory listing when using 'cd'
function cd() {
    local new_directory="
    builtin cd "$new_directory" && ls -ahF --time-style=long-iso --color=auto --ignore=lost+found
}


# Extract anyfile type on list
function extract () {
  if [ -f $1 ] ; then
    case $1 in
      *.tar.bz2)   tar xjvf $1    ;;
      *.tar.gz)    tar xzvf $1    ;;
      *.tar.xz)    tar xvf $1    ;;
      *.bz2)       bzip2 -d $1    ;;
      *.rar)       unrar2dir $1    ;;
      *.gz)        gunzip $1    ;;
      *.tar)       tar xf $1    ;;
      *.tbz2)      tar xjf $1    ;;
      *.tgz)       tar xzf $1    ;;
      *.zip)       unzip2dir $1     ;;
      *.Z)         uncompress $1    ;;
      *.7z)        7z x $1    ;;
      *.ace)       unace x $1    ;;
      *)           echo "'$1' cannot be extracted via extract()"   ;;
    esac
  else
    echo "'$1' is not a valid file"
  fi
}
```