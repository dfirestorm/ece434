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
