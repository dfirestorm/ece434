#!/usr/bin/env python3
# From: https://towardsdatascience.com/python-webserver-with-flask-and-raspberry-pi-398423cc6f5d
# modified by donald hau
import gpiod
import sys,time
from flask import Flask, render_template, request
app = Flask(__name__)
#define sensors GPIOs
buttons=[13,12,15,14] # P8_11, P8_12, P8_15, P8_16
#define actuators GPIOs
getoffsets=[18] # P9_14
#initialize GPIO status variables
CHIP='1'
# Define button and PIR sensor pins as an input
chip = gpiod.Chip(CHIP)
getlines = chip.get_lines(getoffsets)
getlines.request(consumer="flask_gpio.py", type=gpiod.LINE_REQ_DIR_IN)
# Define led pins as output
setlines = chip.get_lines(buttons)
setlines.request(consumer="flask_gpio.py", type=gpiod.LINE_REQ_DIR_OUT)
# turn led OFF 
setlines.set_values([0,0,0,0])

@app.route("/")
def index():
	# Read GPIO Status
	vals = getlines.get_values()
	templateData = {
	 	'button_0'  : setlines.get_values()[0],
		'button_1'  : setlines.get_values()[1],
		'button_2'  : setlines.get_values()[2],
		'button_3'  : setlines.get_values()[3],
  		'ledRed_0'  : getlines.get_values()[0]
    }
	return render_template('index.html', **templateData)
	
@app.route("/<deviceName>/<action>")
def action(deviceName, action):
	devNumber = int(deviceName[-1])
	if action == "on":
		setlines.set_values([1])[devNumber]
	if action == "off":
		setlines.set_values([0])[devNumber]
	if action == "toggle":
		setlines.set_values([1])[devNumber]
		time.sleep(0.2)
		setlines.set_values([0])[devNumber]

	templateData = {
	 	'button_0'  : setlines.get_values()[0],
		'button_1'  : setlines.get_values()[1],
		'button_2'  : setlines.get_values()[2],
		'button_3'  : setlines.set_values()[3],
  		'ledRed_0'  : getlines.get_values()[0]
		}
	return render_template('index.html', **templateData)
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8081, debug=True)