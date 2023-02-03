#!/usr/bin/env python3
import os,time
t1 = "/sys/class/i2c-adapter/i2c-2/2-0048/hwmon/hwmon0/temp1_input"
t2 = "/sys/class/i2c-adapter/i2c-2/2-0049/hwmon/hwmon1/temp1_input"
f1_exists = os.path.exists(t1)
f2_exists = os.path.exists(t2)
if f1_exists:
    pass
else:
    os.system("echo tmp101 0x48 > /sys/class/i2c-adapter/i2c-2/new_device")
    time.sleep(1)
if f2_exists:
    pass
else:
    os.system("echo tmp101 0x49 > /sys/class/i2c-adapter/i2c-2/new_device")
    time.sleep(1)

f1 = open(t1, 'r')
f2 = open(t2, 'r')
print(f1.read())
print(f2.read())
