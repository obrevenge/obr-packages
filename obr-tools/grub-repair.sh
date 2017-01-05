#!/bin/bash

# This is a graphical tool to re-install grub, generate a new grub config file, or
# set up a dual boot in grub.
# 
# Written by Jody James for OBRevenge OS
#
# Setting Title
title="OBRevenge Grub Configuration Tool"
#
#Getting a list of available devices
lsblk -lno NAME,TYPE | grep 'disk' | awk '{print "/dev/" $1 " " $2}' | sort -u > devices.txt
sed -i 's/\<disk\>//g' devices.txt
devices=` awk '{print "FALSE " $0}' devices.txt `
#
# Greeting User and providing options for actions
choice=$(zenity --list --title="$title" --height=250 --text "What would you like to do?\nThe dual boot repair option will allow you to select a\npartition that contains another operating system and\nmake sure that system is included in the Grub Menu." --radiolist --column "Select" --column "Options" FALSE "Re-Install Grub" FALSE "Generate a new Grub config file" FALSE "Repair dual boot")

# Acting on the User's choice
if [ "$choice" = "Re-Install Grub" ]
	then drive=$(zenity --list --title="$title" --height=250 --text "Where would you like to install Grub?" --radiolist --column "Select" --column "Options" $devices)
	(echo	"# Installing Grub..."
	grub-install $drive
	echo "# Generating New Grub Config File..."
	grub-mkconfig -o /boot/grub/grub.cfg) | zenity --progress --title="$title" --pulsate --auto-close
	elif [ "$choice" = "Generate a new Grub config file" ]
	then (echo "# Generating New Grub Config File..."
	grub-mkconfig -o /boot/grub/grub.cfg) | zenity --progress --title="$title" --pulsate --auto-close
	elif [ "$choice" = "Repair dual boot" ]
	then dbpart=$(find /dev -mindepth 1 -maxdepth 1  -name "*[sh]d[a-z][0-9]"  | sort | awk '{ printf "FALSE""\0"$0"\0" }' | \
	xargs -0 zenity --list --title="$title" --text="Select the partition that contains the other system\nthat needs to be included in the Grub Menu." \
	--radiolist --multiple --column ' ' --column 'Partitions')
	(echo "# Adding $dbpart to Grub Config..."
	mount $dbpart /mnt
	pacman -S --noconfirm os-prober
	echo "# Generating new Grub config file..." 
	grub-mkconfig -o /boot/grub/grub.cfg;umount -R /mnt) | zenity --progress --title="$title" --pulsate --auto-close
	else exit
fi

rm devices.txt

# Advising the User that the process is complete
exit=$(zenity --list --title="$title" --height=200 --text "Process Complete!\nWhat would you like to do now?" --radiolist --column "Select" --column "Options" FALSE "Exit" FALSE "Reboot")
# Acting on User Choice
if [ "$exit" = "Exit" ]
	then exit
	elif [ "$exit" = "Reboot" ]
	then reboot
	else exit
fi




