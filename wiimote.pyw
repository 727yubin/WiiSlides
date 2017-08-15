#!/usr/bin/env python

import cwiid, time, os, threading

try:
	os.system('zenity --info --timeout 2 --text "Press 1 and 2"')
	wii=cwiid.Wiimote()
except RuntimeError:
	os.system('zenity --info --timeout 2 --text "Connection failed"')
	quit()

wii.rpt_mode = cwiid.RPT_BTN
timeout = 0.2

def battery():
	while 1:
		wii.led = int(round(wii.state['battery']*3/2.09/20))
		time.sleep(2)

child_t = threading.Thread(target=battery)
child_t.setDaemon(True)
child_t.start()

while 1:
	if (wii.state['buttons'] & cwiid.BTN_A):
		os.system('xdotool key Right')
		wii.rumble = True
		time.sleep(timeout/2)
		wii.rumble = False
	if (wii.state['buttons'] & cwiid.BTN_B):
		os.system('xdotool key Left')
		wii.rumble = True
		time.sleep(0.1)
		wii.rumble = False
		time.sleep(0.1)
		wii.rumble = True
		time.sleep(timeout/2)
		wii.rumble = False
	if (wii.state['buttons'] & cwiid.BTN_LEFT):
		os.system('xdotool mousemove_relative -- -5 0')
	if (wii.state['buttons'] & cwiid.BTN_RIGHT):
		os.system('xdotool mousemove_relative 5 0')
	if (wii.state['buttons'] & cwiid.BTN_UP):
		os.system('xdotool mousemove_relative -- 0 -5')
	if (wii.state['buttons'] & cwiid.BTN_DOWN):
		os.system('xdotool mousemove_relative 0 5')
	if (wii.state['buttons'] & cwiid.BTN_MINUS):
		os.system('xdotool key Escape')
		time.sleep(timeout)
	if (wii.state['buttons'] & cwiid.BTN_PLUS):
		os.system('xdotool key F5')
		time.sleep(timeout)
	if (wii.state['buttons'] & cwiid.BTN_1):
		os.system('xdotool click 1')
		time.sleep(timeout)
	if (wii.state['buttons'] & cwiid.BTN_2):
		os.system('xdotool click 3')
		time.sleep(timeout)
	if (wii.state['buttons'] & cwiid.BTN_HOME):
		os.system('xdotool key Alt+F4')
		time.sleep(5)
		os.system('poweroff')
	else:
		pass
