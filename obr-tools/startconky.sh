#!/bin/bash

sed -i '/conky/d' ~/.config/openbox/autostart
echo "conky -c ~/.config/conky.conf &" >> ~/.config/openbox/autostart
conky -c ~/.config/conky.conf &