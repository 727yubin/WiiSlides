# WiiSlides
Use your Wii Remote as a clicker for presentations.

## Requirements:
<ul>
	<li> A Wii Remote (not sure if it works for ones with MotionPlus)
	<li> A computer running Linux with Bluetooth(X should be fine, but not sure about Wayland)
	<li> Python **2.** Support for Python 3 will be availible once CWiid-python is ported to Py3.
	<li> CWiid-python (you should be able to download it using `sudo pip install cwiid` )
	<li> xdotool ( `sudo apt-get install xdotool` or `sudo dnf install xdotool` )
</ul>

## Getting started

Run the program and press 1 and 2 on your Wii Remote. Once the LEDs stop blinking, it means it is connected. Try pressing buttons on the D-Pad to verify: the cursor should move.

<h2>Features(or what the buttons do)</h2>
<ul>
	<li>D-Pad: Move cursor
	<li>Button A: Right Arrow (vibrate once)
	<li>Button B: Left Arrow (vibrate twice)
	<li>Minus Key: Escape
	<li>Home Key: Alt+F4 then runs `sudo poweroff` after 5 seconds
	<li>Plus Key: F5
	<li>Button 1: Left click
	<li>Button 2: Right click
</ul>

The LEDs show battery level, with 4 being full and 1 being almost empty.


## To Do:
<ul>
	<li> Toggle vibrations
	<li> Make code more readable
	<li> Port to Windows. The main issue I am having with this is making Python deal with Bluetooth. Once the solution is found, it should be working.
</ul>
