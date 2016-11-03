#!/bin/bash

sed -i '/conky/d' ~/.config/openbox/autostart
killall conky