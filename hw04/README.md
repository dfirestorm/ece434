# hw04

# memory map
 see memory_map.md. Highlights: 

   8000_0000 EMIF0 SDRAM
   481A_E000 GPIO3
   481A_C000 GPIO2
   4804_C000 GPIO1
   44E0_7000 GPIO0

# gpio via mmap
 python_LED_toggle toggles as fast as possible. 
 button_and_light reads 4 switches to control 4 LEDs across 2 gpio ports
 Both require sudo. 
 For speed, they're much much faster than gpiod. Their speed is mostly limited by the python GIL or processor speed, rather than file io speed

# i2c via kernel driver
 kernel_i2c.py will read the i2c sensors via a kernel driver. 

# 2.4 " TFT LCD
 the LCD has been set up on SPI1. displaying images works nicely though mplayer doesn't. In addition to a USB keyboard, this allows for running the bone without a PC. 

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

