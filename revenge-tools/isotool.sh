#!/bin/bash

#This is a tool to write iso images to USB for OBRevenge OS
#
#Written by Jody James for OBRevenge OS

#code to detect available USB's
dev=$(lsblk -o tran,name | grep usb | grep -v sr | awk '{print $2}')

#total device list
devices=$(lsblk -lno NAME,TYPE,SIZE | grep "disk")

#setting title
title="Revenge Live USB Tool"

#main interface
yad --width=400 --title="$title" --window-icon=preferences-desktop --center --width=600 --text="This Utility will assist you in creating live USB's from an iso file" --separator=" " --item-separator="\n" --image="/usr/share/Icons/revenge_logo.png" --form --date-format="%-d %B %Y" --field="Below is a list of drives on your system\n$devices":LBL --field="Select your USB device. Only USB's should be listed,\nbut please choose with care.":CB --field="Select the base of the Linux Distro iso file:":CB --field="Select the iso image file:":FL \
"" "$dev" " 
Arch
Debian
Ubuntu" "" > .choice.txt

#setting variables based on input
device=` cat .choice.txt | awk '{print $1;}' `
iso=` cat .choice.txt | awk '{print $3;}' `
distros=` cat .choice.txt | awk '{print $2;}' `

if [ "$distros" = "" ]
	then exit
fi

if [ "$distros" = "Arch" ]
	then BS="bs=4M"
else
BS="bs=1M"
fi
#warning user about possible loss of data on USB
zenity --question --title="$title" --height=30 --text "WARNING\nAll data on /dev/${device} will be destroyed.\nDo you want to continue?"

if [ "$?" = "1" ]
	then exit
fi 

#writing iso to USB using dd

(
gksu dd $BS if=${iso} of=/dev/${device} status=progress && sync) | zenity --progress --title="$title" --pulsate --no-cancel --width=500 --text "Writing iso to the USB..." --auto-close

rm .choice.txt

zenity --info --height=30 --title="$title" --text "Process Complete!"




