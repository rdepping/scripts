#!/bin/bash
USER=jiml
export HOME=/home/$USER
source $HOME/.Xdbus
export DISPLAY=:0
echo "Undock script"
echo "Switch primary monitor"
sudo -u $USER $HOME/git/autorandr/auto-disper --change
