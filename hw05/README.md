# hw05

## ebc Make exercise
    Done, loaded into the folder as Makefile
## kernel exercises
    in the kernel folder is a copy of Derek Molloy's kernel exercises from exploringBB. 
    they are heavily modified such that gpioTest will map P8_15 and P8_18 to P9_12 and P9_14 respectively, 
    and led will blink P9_12 and P9_14. 
    Use them with make, sudo insmod <name>.ko, and then they should run. 
    Remove them with sudo rmmod <name>.
## Etch A Sketch Updates

 etch a sketch now runs via the i2c accelerometer. It uses a kernel module so if it doesn't work, go to /sys/class/i2c-adapter/i2c-2 and run sudo chgrp -R i2c *
 That is all of the work for this module. 

# hw05 grading

| Points      | Description |
| ----------- | ----------- |
|  0/0 | Project 
|  2/2 | Makefile
|  6/6 | Kernel Source
|  4/4 | Etch-a-Sketch
|  8/8 | Kernel Modules: hello, ebbchar, gpio_test, led
|  4/4 | Extras - Blink at different rates
| 20/20 | **Total**
Late: -4
*My comments are in italics. --may*

