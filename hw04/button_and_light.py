#!/usr/bin/env python3
"""
Switches and Lights.

Authors Donald Hau.

"""
try:
  from mmap import mmap
except ImportError: 
  print("Must be run as root, try again with sudo")
import time,struct
GPIO0_offset = 0x44E07000
GPIO0_size = 0x44E07FFF-GPIO0_offset
GPIO1_offset = 0x4804c000
GPIO1_size = 0x4804cfff-GPIO1_offset
GPIO_OE = 0x134
GPIO_SETDATAOUT = 0x194
GPIO_CLEARDATAOUT = 0x190
LED1 = 1<<18 # P9_14, GPIO1 18
LED2 = 1<<16 # P9_15, GPIO1 16
LED3 = 1<<30 # P9_11, GPIO0 30
LED4 = 1<<31 # P9_13, GPIO0 31
SW1 = 1<<13 # P8_11, GPIO 1 13
SW2 = 1<<12 # P8_12, GPIO 1 12
SW3 = 1<<15 # P8_15, GPIO 1 15
SW1 = 1<<14 # P8_16, GPIO 1 14


with open("/dev/mem", "r+b" ) as f:
  mem1 = mmap(f.fileno(), GPIO1_size, offset=GPIO1_offset)
  mem0 = mmap(f.fileno(), GPIO0_size, offset=GPIO0_offset)

packed_reg1 = mem1[GPIO_OE:GPIO_OE+4]
reg_status1 = struct.unpack("<L", packed_reg1)[0]
mem1[GPIO_OE:GPIO_OE+4] = struct.pack("<L", reg_status1)
packed_reg0 = mem0[GPIO_OE:GPIO_OE+4]
reg_status0 = struct.unpack("<L", packed_reg0)[0]
mem0[GPIO_OE:GPIO_OE+4] = struct.pack("<L", reg_status0)
try: 
  while True:
    #check values 
    if reg_status1 & SW1:
      mem1[GPIO_SETDATAOUT:GPIO_SETDATAOUT+4] = struct.pack("<L", LED1)
    else: 
      mem1[GPIO_CLEARDATAOUT:GPIO_CLEARDATAOUT+4] = struct.pack("<L", LED1)
    if reg_status1 & SW2:
      mem1[GPIO_SETDATAOUT:GPIO_SETDATAOUT+4] = struct.pack("<L", LED2)
    else:
      mem1[GPIO_CLEARDATAOUT:GPIO_CLEARDATAOUT+4] = struct.pack("<L", LED2)
    if reg_status1 & SW3:
      mem0[GPIO_SETDATAOUT:GPIO_SETDATAOUT+4] = struct.pack("<L", LED3)
    else:
      mem0[GPIO_CLEARDATAOUT:GPIO_CLEARDATAOUT+4] = struct.pack("<L", LED3)
    if reg_status1 & SW4:
      mem0[GPIO_SETDATAOUT:GPIO_SETDATAOUT+4] = struct.pack("<L", LED4)
    else:
      mem0[GPIO_CLEARDATAOUT:GPIO_CLEARDATAOUT+4] = struct.pack("<L", LED4)
    time.sleep(0.05)

    #update values?
    packed_reg1 = mem1[GPIO_OE:GPIO_OE+4]
    reg_status1 = struct.unpack("<L", packed_reg1)[0]
    mem1[GPIO_OE:GPIO_OE+4] = struct.pack("<L", reg_status1)
    packed_reg0 = mem0[GPIO_OE:GPIO_OE+4]
    reg_status0 = struct.unpack("<L", packed_reg0)[0]
    mem0[GPIO_OE:GPIO_OE+4] = struct.pack("<L", reg_status0)
except KeyboardInterrupt:
  mem1.close()
  mem0.close()
