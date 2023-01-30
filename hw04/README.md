# hw04

# memory map
 see memory_map.md. Highlights: 

   8000_0000 EMIF0 SDRAM
   481A_E000 GPIO3
   481A_C000 GPIO2
   4804_C000 GPIO1
   44E0_7000 GPIO0

# gpio via mmap
 python_LED_toggle toggles P9_14 as fast as possible. 
 button_and_light reads 4 switches to control 4 LEDs across 2 gpio ports - specifically P8_11,12,15,16 to control P9_11,13,14,15
 Both require sudo. 
 For speed, they're much much faster than gpiod. Their speed is mostly limited by the python GIL or processor speed, rather than file io speed

# i2c via kernel driver
 kernel_i2c.py will read the i2c sensors via a kernel driver. 

# 2.4 " TFT LCD
 the LCD has been set up on SPI1. displaying images works nicely though mplayer doesn't. In addition to a USB keyboard, this allows for running the bone without a PC. 

# etch a sketch
 etch a sketch has been improved to allow flask input. 
 flask uses pins P8_7-10 as outputs for GPIO and Etch a Sketch uses P8_11,12,15,16 as inputs so wire them to each other to allow for control via flask. 
# hw04 grading

| Points      | Description | |
| ----------- | ----------- | - |
|  2/2 | Memory map 
|  4/4 | mmap()
|  4/4 | i2c via Kernel
|  0/5 | Etch-a-Sketch via flask | *Not demo'ed*
|  5/5 | LCD display
|      | Extras
| 11/20 | **Total**
Late -4
*My comments are in italics. --may*

