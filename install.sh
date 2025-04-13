# Step One update

yes| sudo pacman -Syu

yes| sudo pacman -S --needed git base-devel && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si

yes| sudo pacman -S jre8-openjdk python-pip tk

pip install pyautogui pynput requests --break-system-packages

