#!/bin/bash

# This is a utility written for OBRevenge to assist in install steam
# Writen by Jody James


# Greet user and ask them if they want to install steam

zenity --question --height=30 --title="OBRevenge Steam Installer" --text "Would you like to install steam?"

# get answer and react accordingly

if [ "$?" = "1" ]
    then exit
fi

# Get graphics card choice

ans=$(zenity --list --title="OBRevenge Steam Installer" --text "What kind of graphics card is in your computer?" --checklist --column "Select" --column "Graphics Card" FALSE "ATI/AMD" FALSE "Intel" FALSE "Nvidia")

if [ "$?" = "1" ]
    then exit
fi

# Set variable to for graphics card
if [ "$ans" = "Nvidia" ]
    then driver="lib32-nvidia-libgl"
    else driver="lib32-mesa-libgl"
fi

# Ask user if they are ready to install

zenity --question --height=30 --title="OBRevenge Steam Installer" --text "Are you ready to install Steam?"

if [ "$?" = "1" ]
    then exit
fi

# Install Steam and selected driver

(yes | pacman -S --noconfirm $driver lib32-alsa-plugins lib32-curl steam) | 
zenity --progress --title="OBRevenge Steam Installer" --text "Installing Steam..." --pulsate --auto-close

zenity --info --title="OBRevenge Steam Installer" --height=30 --text "Steam has been installed!"

