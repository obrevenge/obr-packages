#!/bin/bash

packages=` cat .packages.txt `

echo $packages

pacman -S --noconfirm $packages | zenity --progress --title="OBRevenge Software Tool" --no-cancel --pulsate --text "Installing Packages" --width=500 --auto-close

rm .packages.txt
