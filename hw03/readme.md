# hw03

## TMP101

 I2C addresses on the I2C Bus: 
 1001000, 1001001, 1001010 
 0x48, 0x49, 0x4a
 Use tmp_in_f.sh to read temp in f
 Use readtemp.py to read two different sensors at once via I2C
 Use templimit.py to read the sensors with alerts. 

## Etch A Sketch Updates

The etch a sketch program now uses the 8x8 LED matrix on I2C and uses two rotary encoders to control movement. use setup.sh to ensure using eQEP on the correct pins. No erase, orange as the indicator of user position. 
Uses p8_33/35 for eQEP1 and p8_41/42 for eQEP2