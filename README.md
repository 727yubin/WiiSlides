# WiiSlides
Use your Wii Remote as a clicker for presentations.

## Requirements:

- A Wii Remote (not sure if it works for ones with MotionPlus)
- A computer running Linux with Bluetooth(X should be fine, but not sure about Wayland)
- Python **2.** Support for Python 3 will be availible once CWiid-python is ported to Py3.
- CWiid-python (you should be able to download it using `sudo pip install cwiid`)
- xdotool (`sudo apt-get install xdotool` or `sudo dnf install xdotool`)

## Getting started

1. Download wiimote.pyw.
2. Run the program and press 1 and 2 on your Wii Remote. Once the LEDs stop blinking, it means it is connected.
3. Try pressing buttons on the D-Pad to verify: the cursor should move.

## Features(or what the buttons do)

- D-Pad: Move cursor
- Button A: Right Arrow (vibrate once)
- Button B: Left Arrow (vibrate twice)
- Minus Key: Escape
- Home Key: <kdb> ALT </kbd> + <kbd> F4 </kbd> then runs `sudo poweroff` after 5 seconds
- Plus Key: F5
- Button 1: Left click
- Button 2: Right click

The LEDs show battery level, with 4 being full and 1 being almost empty.

## Troubleshooting
If you did press 1 and 2 but cannot seem to connect, try using the red SYNC button next to the batteries.

## To Do:
- Toggle vibrations
- Make code more readable
- Port to Windows. The main issue I am having with this is making Python deal with Bluetooth. Once the solution is found, it should be working. Meanwhile, there is a more "hacky" version requiring different software [here](https://www.instructables.com/id/Use-a-Wii-Remote-to-Control-a-Computer/).
