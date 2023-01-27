#!/usr/bin/env python3
# From: https://towardsdatascience.com/python-webserver-with-flask-and-raspberry-pi-398423cc6f5d
# modified by donald hau
import gpiod
import sys,time
from flask import Flask, render_template, request
app = Flask(__name__)
#define sensors GPIOs
buttons=[2,3,5,4] # P8_7, P8_8, P8_9, P8_10

#initialize GPIO status variables
CHIP='2'
# Define button and PIR sensor pins as an input
chip = gpiod.Chip(CHIP)

# Define led pins as output
setlines = chip.get_lines(buttons)
setlines.request(consumer="flask_gpio.py", type=gpiod.LINE_REQ_DIR_OUT)
# turn led OFF 
setlines.set_values([0,0,0,0])

@app.route("/")
def index():
	# Read GPIO Status
	templateData = {
	 	'button_0'  : setlines.get_values()[0],
		'button_1'  : setlines.get_values()[1],
		'button_2'  : setlines.get_values()[2],
		'button_3'  : setlines.get_values()[3]
    }
	return render_template('index.html', **templateData)
	
@app.route("/<deviceName>/<action>")
def action(deviceName, action):
	devNumber = int(deviceName[-1])
	values = setlines.get_values()
	if action == "on":
		values[devNumber] = 1
		setlines.set_values(values)
	if action == "off":
		values[devNumber] = 0
		setlines.set_values(values)
	if action == "toggle":
		values[devNumber] = 1
		setlines.set_values(values)
		time.sleep(0.05)
		values[devNumber] = 0
		setlines.set_values(values)
	

	templateData = {
	 	'button_0'  : setlines.get_values()[0],
		'button_1'  : setlines.get_values()[1],
		'button_2'  : setlines.get_values()[2],
		'button_3'  : setlines.get_values()[3]
		}
	return render_template('index.html', **templateData)
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8081, debug=True)