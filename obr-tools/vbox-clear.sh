#!/bin/bash

# this is a simple script to clear the virtualbox modules and packages fr
# OBRevenge if the system is installed on hardware instead of a virtual
# machine

# By Jody James for OBRevenge OS

# Setting title
title="OBRevenge Virtualbox Modules Tool"

# UI for user to select if the install is on hardware or vm
answer=$(zenity --list --title="$title" --height=300 --text "OBRevenge OS ships with the virtualbox kernel modules\nby default. If the system is installed on hardware,\nthen you will probably want to remove the virtualbox kernel modules.\nIf you have removed the modules and would like to reinstall them,\nthis tool can do that too.\nWhat would you like to do?" --radiolist --column Select --column Option FALSE "remove vbox modules" FALSE "reinstall vbox modules")

# if statement to determine user anwer
if [ "$answer" = "remove vbox modules" ]
	then

	# Removing virtualbox guest module packages
	(pacman -Rns --noconfirm virtualbox-guest-utils virtualbox-guest-modules-arch

	# Removing the virtualbox modules.d file 
	rm /etc/modules-load.d/virtualbox.conf) | zenity --progress --text "Removing Virtualbox kernel modules..." --pulsate --auto-close

	zenity --info --height=30 --text "Virtualbox kernel modules have been removed! When you reboot the virtualbox modules will no longer try to load."

elif [ "$answer" = "reinstall vbox modules" ]
	then
	# Installing vbox guest modules
	(pacman -S --noconfirm virtualbox-guest-utils virtualbox-guest-modules-arch) | zenity --progress --text "Installing Virtualbox kernel modules..." --pulsate --auto-close

	zenity --info --height=30 --text "Virtualbox kernel modules have been installed! When you reboot the virtualbox modules load."

else exit
fi







