#!/bin/bash

# This is a Utility to Assist Users in installing NVIDIA drivers
# Written for OBRevenge by Jody James

# setting title
title="Revenge NVIDIA Drivers Tool"

# Getting graphics card info
card=$(lspci -k | grep -A 2 -E "(VGA|3D)")

# Remove Virtualbox Kernel Modules
zenity --question --height=30 --title="Revenge NVIDIA Drivers Tool" --text "Before installing the NVIDIA drivers, please make sure\nthat the virtualbox kernel modules have\nbeen removed. You can do this\nby hitting the button on the Welcome\nScreen or by running the command vbox-clear.sh in a terminal.\nAre you ready to begin installation?"

if [ "$?" = "1" ]
	then exit
fi

# Greet User and get user choice
zenity --list --height=400 --title="$title" --text "This utility will assist you in installing NVIDIA drivers.\nYou will need to know what model of NVIDIA gaphics card you are using.\nFor NVIDIA 400 series and newer install nvidia and nvidia-libgl.\nFor 8000-9000 or 100-300 series install nvidia-304xx and nvidia-304xx-libgl.\n\nYour current graphics card is:\n$card\n\nSelect the NVIDIA drivers that you would like to install.\nYou can also choose to remove the nvidia drivers and reinstall open source drivers." --checklist --column "Select" --column "Driver" FALSE "nvidia nvidia-libgl" FALSE "nvidia-304xx nvidia-304xx-libgl" FALSE "remove nvidia drivers" > ~/.nvidia.txt

drivers=` cat ~/.nvidia.txt `

if [ "$drivers" = "" ]
	then exit
fi

# Checking to see if drivers need to be removed
if [ "$drivers" = "remove nvidia drivers" ]
	then (pacman -Rdd nvidia
	pacman -Rdd nvidia-libgl
	pacman -Rdd nvidia-304xx
	pacman -Rdd nvidia-304xx-libgl
	pacman -S --noconfirm mesa xf86-video-nouveau) | zenity --progress --pulsate --auto-close --title="OBRevenge NVIDIA Drivers Tool" --text "Installing Drivers..." 
fi

(yes | pacman -S $drivers nvidia-settings) | zenity --progress --pulsate --auto-close --title="OBRevenge NVIDIA Drivers Tool" --text "Installing Drivers..." 

rm ~/.nvidia.txt

zenity --info --height=20 --title="OBRevenge NVIDIA Drivers Tool" --text "Your drivers are installed,\nthey should be loaded after you reboot!"
