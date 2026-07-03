#!/usr/bin/env python3

"""
* Start chiaki.
* Start this script (in a race game).

Result:

    You will see the car accelleraing for 1 second, and then brake for 1 
    second.
"""

import evdev
from evdev import ecodes as e
import time

## Joystick (Sony Interactive Entertainment DualSense Wireless 
## Controller) has 8 axes (X, Y, Z, Rx, Ry, Rz, Hat0X, Hat0Y) and 13 
## buttons (BtnA, BtnB, BtnX, BtnY, BtnTL, BtnTR, BtnTL2, BtnTR2, 
## BtnSelect, BtnStart, BtnMode, BtnThumbL, BtnThumbR).

## Joystick (Sony Interactive Entertainment DualSense Wireless 
## Controller Motion Sensors) has 6 axes (X, Y, Z, Rx, Ry, Rz) and 0 
## buttons ().

cap = {
	e.EV_KEY: [
		e.BTN_A,
		e.BTN_B,
		e.BTN_X,
		e.BTN_Y,
		e.BTN_TL,
		e.BTN_TR,
		e.BTN_TL2,
		e.BTN_TR2,
		e.BTN_SELECT,
		e.BTN_START,
		e.BTN_MODE,
		e.BTN_THUMBL,
		e.BTN_THUMBR,

		e.BTN_SOUTH,
		e.BTN_EAST,
		e.BTN_NORTH,
		e.BTN_WEST,
		e.BTN_TL,
		e.BTN_TR,
		e.BTN_SELECT,
		e.BTN_START,
	],

	e.EV_ABS: [
		(e.ABS_X,     evdev.AbsInfo(value=127, min=0,  max=255, fuzz=0, flat=0, resolution=0)),
                (e.ABS_Y,     evdev.AbsInfo(value=127, min=0,  max=255, fuzz=0, flat=0, resolution=0)),
		(e.ABS_Z,     evdev.AbsInfo(value=  0, min=0,  max=255, fuzz=0, flat=0, resolution=0)),
		(e.ABS_RX,    evdev.AbsInfo(value=127, min=0,  max=255, fuzz=0, flat=0, resolution=0)),
		(e.ABS_RY,    evdev.AbsInfo(value=127, min=0,  max=255, fuzz=0, flat=0, resolution=0)),
		(e.ABS_RZ,    evdev.AbsInfo(value=  0, min=0,  max=255, fuzz=0, flat=0, resolution=0)),
		(e.ABS_HAT0X, evdev.AbsInfo(value=  0, min=-1, max=1,   fuzz=0, flat=0, resolution=0)),
		(e.ABS_HAT0Y, evdev.AbsInfo(value=  0, min=-1, max=1,   fuzz=0, flat=0, resolution=0)),
	]

	#e.EV_FF: [
	#	(['FF_EFFECT_MIN', 'FF_RUMBLE'], 80),
	#	('FF_PERIODIC', 81),
	#	(['FF_SQUARE', 'FF_WAVEFORM_MIN'], 88),
	#	('FF_TRIANGLE', 89),
	#	('FF_SINE', 90),
	#	(['FF_GAIN', 'FF_MAX_EFFECTS'], 96)
	#]
}


ui = evdev.UInput(cap, name="Python Virtual Pad", bustype=e.BUS_USB)
#print(ui)
#print(ui.capabilities())

while True:
	ui.write(e.EV_ABS, e.ABS_Z, 255)	## Brake!
	ui.write(e.EV_ABS, e.ABS_RZ, 0)		## No throttle.
	ui.syn()
	time.sleep(1.0)

	ui.write(e.EV_ABS, e.ABS_Z, 0)		## Release brake.
	ui.write(e.EV_ABS, e.ABS_RZ, 255)	## Full throttle.
	ui.syn()
	time.sleep(1.0)
