#!/bin/sh
# From http://wh1t3s.com/2009/05/14/reading-beagleboard-gpio/
# Orginally /usr/bin/readgpio, Modified by Mark A. Yoder 20-Jul-2011
#
# Toggle a GPIO input

if [ $# -lt 2 ]; then
    echo "Usage: $0 <gpio pin#> <delay in seconds>"
    exit 0
fi
GPIO=$1
PERIOD=$2

# Open the GPIO port
#
if [ ! -e /sys/class/gpio/gpio$GPIO ]; then
    echo "$GPIO" > /sys/class/gpio/export
fi
echo "out" > /sys/class/gpio/gpio${GPIO}/direction


THIS_VALUE=0
NEWLINE=0

# Read forever

while [ "1" = "1" ]; do

  # "^" for high, '_' for low
  if [ "1" = "$THIS_VALUE" ]; then
    THIS_VALUE=0
   else
    THIS_VALUE=1
  fi
  echo $THIS_VALUE > /sys/class/gpio/gpio${GPIO}/value


  # sleep for a while
  sleep $PERIOD


done

cleanup # call the cleanup routine

