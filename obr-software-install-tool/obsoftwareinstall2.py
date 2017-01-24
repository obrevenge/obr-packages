#!/bin/bash




plug="12344"


yad --plug=$plug --tabnum=1 --list --text "Select the Internet Applications that You Would Like to Install" --checklist --separator=" " --column "Select" --column "Applications" FALSE "firefox " FALSE "chromium " FALSE "midori " FALSE "qupzilla " FALSE "netsurf " FALSE "filezilla " FALSE "opera " FALSE "evolution " FALSE "geary " FALSE "thunderbird " FALSE "transmission-gtk " FALSE "qbittorrent " FALSE "hexchat " --height 400 >> .net.txt &



yad --plug=$plug --tabnum=2 --list --text "Select the Media Applications that You Would Like to Install" --checklist --separator=" " --column "Select" --column "Applications" FALSE "gimp " FALSE "vlc " FALSE "totem " FALSE "spotify " FALSE "parole " FALSE "audacious " FALSE "clementine " FALSE "gthumb " FALSE "shotwell " FALSE "ristretto " FALSE "gpicview " FALSE "brasero " FALSE "audacity " FALSE "simplescreenrecorder " FALSE "xfburn " FALSE "kdenlive " FALSE "obs-studio " --height 400 >> .med.txt &


yad --plug=$plug --tabnum=3 --list --text "Select the Office Applications that You Would Like to Install" --checklist --separator=" " --column "Select" --column "Applications" FALSE "libreoffice-fresh " FALSE "calligra " FALSE "abiword " FALSE "gnumeric " FALSE "pdfmod " FALSE "evince " FALSE "epdfview " FALSE "calibre " FALSE "fbreader " --height 400 >> .off.txt &


yad --notebook --key=$plug --tab="Internet" --tab="Media" --tab="Office" --window-icon=preferences-desktop --image=preferences-desktop --image-on-top --center \
--title="OBRevenge Software Install Tool" --text='<span font_weight="bold">Quickly Select and Install Software</span>\nSelect software in the tabs below.' --height=500 --width=600 

sed -i -e 's/[|]//g' .net.txt
sed -i -e 's/[|]//g' .med.txt
sed -i -e 's/[|]//g' .off.txt

net=$(cat .net.txt | awk '{print $2}')
med=$(cat .med.txt | awk '{print $2}')
off=$(cat .off.txt | awk '{print $2}')

if [[ $(echo $med | grep -i 'kdenlive') != "" ]]
	then med="$med breeze-icons frei0r-plugins"
fi

zenity --question --title="OBRevenge Software Install Tool" --height=40 --text "The following software will be installed\n\n$net $med $off\n\nDo you want to proceed?"

if [ "$?" = "1" ]
	then exit
fi

(pacman -S --noconfirm $net $med $off) | zenity --progress --title="OBRevenge Software Install Tool" --text "Installing Software..." --width=600 --pulsate --auto-close --no-cancel

zenity --info --title="OBRevenge Software Install Tool" --text "Installation Complete!" --height=30

rm .net.txt
rm .med.txt
rm .off.txt






