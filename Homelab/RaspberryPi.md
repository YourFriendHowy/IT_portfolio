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
git - needed to pull script and install fonts and other things, must ssh to github account
wget - installed for kitty theme installation
Hyprland
Kitty
- theme
  *theme name can be edited, themes are found at https://github.com/dexpota/kitty-themes
	- set variable for theme: `THEME=https://raw.githubusercontent.com/dexpota/kitty-themes/master/themes/AlienBlood.conf`
	- downloads theme to specified directory: `wget "$THEME" -P ~/.config/kitty/kitty-themes/themes`
	- navigate to kitty config: `cd ~/.config/kitty`
	- symlink theme: `ln -s ./kitty-themes/themes/AlienBlood.conf ~/.config/kitty/theme.conf`
	- create kitty config file and add theme: `echo "include ./theme.conf" > kitty.conf`
- fonts
	- download nerd-fonts: `git clone --filter=blob:none --sparse git@github.com:ryanoasis/nerd-fonts`
	- navigate to nerd-fonts directory: `cd nerd-fonts`
	- 

oh-my-zsh
- theme