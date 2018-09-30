# WiiSlides
Use your Wii Remote as a clicker for presentations on linux.

## Requirements

- A Wii Remote
- A Linux computer with Bluetooth
- Python 3

## Instructions

1. Run `install.sh`.
2. Download `wiimote.pyw`.
3. Run the program and press the red "SYNC" button on Wii Remote. Once the LEDs stop blinking, it means it is connected.
4. Try pressing buttons on the D-Pad to verify: the cursor should move.

## Key mapping

- D-Pad: Move cursor
- Button A: Right Arrow (vibrate once)
- Button B: Left Arrow (vibrate twice)
- Minus Key: Escape
- Home Key: <kdb> Alt+F4 </kbd> then runs `sudo poweroff` after 5 seconds
- Plus Key: F5
- Button 1: Left click
- Button 2: Right click

The LEDs show battery level in binary.

## To Do:
- Test on Fedora(Wayland)
