#!/bin/sh
USER=jiml
export HOME=/home/$USER
source $HOME/.Xdbus
export DISPLAY=:0
# wait for the dock state to change
sleep 0.5
DOCKED=$(cat /sys/devices/platform/dock.0/docked)
case "$DOCKED" in
   "0")
       echo "Run undock script..."
        #/usr/local/sbin/undock
        sudo -u $USER $HOME/utils/autorandr/auto-disper --change
        ;;
    "1") 
        echo "Run dock script..."
        #/usr/local/sbin/dock
        sudo -u $USER $HOME/utils/autorandr/auto-disper --change
        ;;
esac
exit 0
