#!/bin/bash

# This is a tool to change the kernel on an Arch Linux System. The kernel choices include
# the current linux kernel, linus-lts, linux-grsec, and linux-zen

# Written by Jody James for OBRevenge OS

# setting title
title="OBRevenge Kernel Configuration"

# getting current kernel
current=$(pacman -Qqen | grep "linux" | grep -v "atm" | grep -v "sys" | grep -v "util" | grep -v "headers")

# Greeting user and allowing user to choose whick kernel to install
kernel=$(zenity --list --title="$title" --height=550 --text "There are several kernels available for the system.\n\nOBRevenge OS ships with the current linux kernel.\nThis kernel is the most up to date, providing the best hardware support.\nHowever, there could be possible bugs in this kernel, despite testing.\n\nThe linux-lts kernel provides a focus on stability.\nIt is based on an older kernel, so it may lack some newer features.\n\nThe linux-grsec kernel is focused on security\nIt contains the Grsecurity Patchset and PaX for increased security.\n\nThe linux-zen kernel is the result of a collaboration of kernel hackers\nto provide the best possible kernel for everyday systems.\n\nYou are currently running the $current kernel.\n\nPlease select the kernel that you would like to install." --radiolist --column "Select" --column "Kernel" FALSE linux FALSE linux-lts FALSE linux-grsec FALSE linux-zen FALSE "exit")

# checking for exit status
if [ "$kernel" = "exit" ]
	then exit
fi
if [ "$kernel" = "" ]
	then exit
fi

# removing old kernel
(echo "# Removing $current kernel..."
pacman -Rdd --noconfirm os-prober
pacman -Rdd --noconfirm $current

# installing selected kernel
echo "# Installing $kernel kernel..."
pacman -S --noconfirm $kernel

echo "# Generating new Grub config file..."
grub-mkconfig -o /boot/grub/grub.cfg) | zenity --progress --title="$title" --width=300 --pulsate --auto-close

# Choices for closing
close=$(zenity --list --title="$title" --text "The Process is complete\nWhat would you like to do now?" --radiolist --column "Select" --column "Options" FALSE "reboot" FALSE "exit")

# acting on choice
if [ "$close" = "reboot" ]
	then reboot
else exit
fi








