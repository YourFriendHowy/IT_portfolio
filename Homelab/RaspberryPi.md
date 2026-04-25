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