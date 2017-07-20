#!/bin/bash

# This is a graphical tool to install Flash from the Arch repos
# This tool was written by Jody James for OBRevenge OS

# Setting title
title="Revenge Flash Installer"
# Greeting user and allowing user to choose to install codecs or exit
answer=$(zenity --list --title="$title" --text "Would you like to install Flash\nThis may include some proprietary software." --radiolist --column "Select" --column "Choice" FALSE "Yes, Please intall Flash" FALSE "No, thank you")

# acting on user input
if [ "$answer" = "Yes, Please intall Flash" ]
	then (echo "# Installing Flash..."
	pacman -S --noconfirm flashplugin pepper-flash) | zenity --progress title="$title" --pulsate --auto-close
	else exit
fi

# Advising user that the process is complete
zenity --info --title="$title" --height=40 --text "Process complete!"
