#!/usr/bin/python
#
# This script will automatically set status to "unavailable" when screen is
# locked or screensaver is activated, and will bring it back to available
# (online) when screensaver is closed.
# 
# Reference:
# http://askubuntu.com/questions/36894/how-can-i-automatically-set-my-status-to-available-when-i-log-in

import os
import time
import dbus
from gi.repository import TelepathyGLib as Tp
from gi.repository import GObject

session_bus = dbus.SessionBus()
loop = GObject.MainLoop()
am = Tp.AccountManager.dup()
am.prepare_async(None, lambda *args: loop.quit(), None)
loop.run()

screensaver_started = 0
running = 0

while 1:
    active = 0
    out = ""
    pid = 0

    if screensaver_started == 0:
        # Don't do anything if the screensaver isn't running
        s = os.popen("pidof gnome-screensaver")
        spid = s.read()
        s.close()
        if len(spid) > 0:
            screensaver_started = 1
    else:
        h = os.popen("gnome-screensaver-command -q", "r")
        out = h.read()
        active = out.find("inactive")
        h.close()

        if active < 0 and running == 0:
            am.set_all_requested_presences(Tp.ConnectionPresenceType.OFFLINE, 'Offline', "")
            running = 1
        elif active > 0 and running == 1:
            am.set_all_requested_presences(Tp.ConnectionPresenceType.AVAILABLE, 'Available', "")
            running = 0
        time.sleep(5)
