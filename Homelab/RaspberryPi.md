## Installing Arch Arm
Installed Arch Arm via "https://www.youtube.com/watch?v=WpCSOS_1vic"
- Guide: https://kiljan.org/2023/11/24/arch-linux-arm-on-a-raspberry-pi-5-model-b/
- Current Version: https://archlinuxarm.org/packages/aarch64/linux-rpi

### Issues
The following command had a 404 error solves by running `pacman -Syy && pacman -Su` then reran the command below. *There is suggestions for this error in the guide linked above*
```bash
pacman -Syu --overwrite "/boot/*" linux-rpi
```


## Build
### git
*needed to pull script and install fonts and other things, must ssh to github account*
**Dependencies:** *openssh*
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

## wget - installed for kitty theme installation
Hyprland
### Kitty
**Dependencies:** *git, wget*
#### Theme
  *Theme can be changed, themes are found at "https://github.com/dexpota/kitty-themes"*
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
### Fonts
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

oh-my-zsh
- theme