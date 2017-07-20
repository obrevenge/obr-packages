#!/bin/bash
rm -f /etc/sudoers.d/g_wheel
rm -R /etc/systemd/system/getty@tty1.service.d
rm /etc/systemd/system/default.target
rm /usr/share/applications/rif.desktop
rm -f /etc/skel/Desktop/Calamares.desktop
rm -f /etc/skel/Desktop/Revenge_Installer.desktop
mkdir -p /etc/skel/.config/autostart
mv /etc/obwelcome.desktop /etc/skel/.config/autostart/obwelcome.desktop
systemctl enable lightdm.service



