#!/usr/bin/env python3
import Adafruit_BBIO.GPIO as GPIO
import time

button1="P8_11"
button2="P8_12"
button3="P8_15"
button4="P8_16"

LEDr   ="P9_12"
LEDy   ="P9_15"
LEDg   ="P9_23"
LEDb   ="P8_26"

# Set the GPIO pins:
GPIO.setup(LEDr,    GPIO.OUT)
GPIO.setup(LEDy,    GPIO.OUT)
GPIO.setup(LEDg,    GPIO.OUT)
GPIO.setup(LEDb,    GPIO.OUT)
GPIO.setup(button1, GPIO.IN)
GPIO.setup(button2, GPIO.IN)
GPIO.setup(button3, GPIO.IN)
GPIO.setup(button4, GPIO.IN)

# Turn on both LEDs
GPIO.output(LEDr, 1)
GPIO.output(LEDy, 1)
GPIO.output(LEDg, 1)
GPIO.output(LEDb, 1)
# Map buttons to LEDs
map = {button1: LEDr, button2: LEDy, button3: LEDg, button4: LEDb}

def updateLED(channel):
    print("channel = " + channel)
    state = GPIO.input(channel)
    GPIO.output(map[channel], state)
    print(map[channel] + " Toggled")

print("Running...")

GPIO.add_event_detect(button1, GPIO.BOTH, callback=updateLED) 
# RISING, FALLING or BOTH
GPIO.add_event_detect(button2, GPIO.BOTH, callback=updateLED)
GPIO.add_event_detect(button3, GPIO.BOTH, callback=updateLED)
GPIO.add_event_detect(button4, GPIO.BOTH, callback=updateLED)

try:
    while True:
        time.sleep(100)   # Let other processes run

except KeyboardInterrupt:
    print("Cleaning Up")
    GPIO.cleanup()
GPIO.cleanup()
