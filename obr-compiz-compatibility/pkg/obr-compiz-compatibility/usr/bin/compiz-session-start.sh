#!/bin/bash

# This is a script to start the compiz window manager in a standalone session
# for OBRevenge OS.
# The script will also start the applications that are listed in the user's openbox
# autostart file.

# copying config files for compiz
[ -f ~/.config/compiz-1/compizconfig ] || cp -r /etc/skel/.config/compiz-1 ~/.config/compiz-1
[ -f ~/.config/compiz/boxmenu/menu.xml ] || cp -r /etc/skel/.config/compiz ~/.config/compiz
[ -f ~/.emerald ] || cp -r /etc/skel/.emerald ~/.emerald

# running script to start applications in user's openbox/autostart file
compiz-autostart &

# starting compiz
compiz

