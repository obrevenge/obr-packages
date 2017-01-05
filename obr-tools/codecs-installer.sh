#!/bin/bash

# This is a graphical tool to install multimedia codecs from the Arch repos
# This tool was written by Jody James for OBRevenge OS

# Setting title
title="OBRevenge Codecs Installer"
# Greeting user and allowing user to choose to install codecs or exit
answer=$(zenity --list --title="$title" --text "Would you like to install the most commonly used\nmultimedia codecs? Some of these may include some\nproprietary software." --radiolist --column "Select" --column "Choice" FALSE "Yes, Please intall codecs" FALSE "No, thank you")

# acting on user input
if [ "$answer" = "Yes, Please intall codecs" ]
	then (echo "# Installing Codecs..."
	pacman -S --noconfirm a52dec autofs faac faad2 flac lame libdca libdv libmad libmpeg2 libtheora libvorbis libxv wavpack x264 gstreamer0.10-plugins libdvdcss dvd+rw-tools dvdauthor dvgrab) | zenity --progress title="$title" --pulsate --auto-close
	else exit
fi

# Advising user that the process is complete
zenity --info --title="$title" --height=40 --text "Process complete!"
