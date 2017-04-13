#!/bin/bash

packages=` cat .packages.txt `

echo $packages

# updating databases and writing results to a file
pacman -Syy | tee .pacmanstatus.txt | zenity --progress --title="OBRevenge Software Tool" --no-cancel --pulsate --text "Updating Package Database..." --width=500 --auto-close

pstatus=` cat .pacmanstatus.txt `


# checking for other running package managers
if [[ $(cat .pacmanstatus.txt | grep -i 'downloading revenge_repo.db') = "" ]]
	then # giving choice to user to kill other process or wait
	ans=$(zenity --list --title="OBRevenge Software Tool" --radiolist --text "Another package manager is running.\nIf you are updating the system\nyou may want to finish updates before continuing\nto avoid problems. If not, it is safe to kill the other process.\nWhat would you like to do?" --column Select --column Choice TRUE "Kill other process and continue" FALSE "Wait to finish updating" --height=300)
	# killing pamac and unlocking db
	if [ "$ans" = "Kill other process and continue" ]
		then
		killall pamac-updater
		killall pamac-manager
		rm /var/lib/pacman/db.lck
		pacman -Syy | zenity --progress --title="OBRevenge Software Tool" --no-cancel --pulsate --text "Updating Package Database..." --width=500 --auto-close
		else # exiting according to user choice
		exit
	fi
fi

# Installing packages
pacman -S --noconfirm $packages | zenity --progress --title="OBRevenge Software Tool" --no-cancel --pulsate --text "Installing Packages..." --width=500 --auto-close

# Letting user know that packages have been installed
zenity --info --text="Your Packages Have Been Installed Successfully"

# removing files no longer needed
rm .packages.txt
rm .pacmanstatus.txt
rm /var/lib/pacman/db.lck

