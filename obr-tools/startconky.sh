#!/bin/bash

sed -i '/conky/d' ~/.config/openbox/autostart
echo "sh ~/.conky/conky-startup.sh &" >> ~/.config/openbox/autostart
conky -c ~/.conky/OBRevenge/OBRevenge &