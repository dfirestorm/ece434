#!/bin/bash
TEMP=`i2cget -y 2 0x48 0`
TEMP2=$(($((TEMP * 9/5))+32))
echo temp 1 is $TEMP2 F
TEMP=`i2cget -y 2 0x4a 0`
TEMP2=$(($((TEMP * 9/5))+32))
echo temp 2 is $TEMP2 F