from mmap import mmap
import time,struct

GPIO1_offset = 0x4804c000
GPIO1_size = 0x4804cfff-GPIO1_offset
GPIO_OE = 0x134
GPIO_SETDATAOUT = 0x194
GPIO_CLEARDATAOUT = 0x190
SW1 = 1<<13
SW2 = 1<<12
SW3 = 1<<15
SW4 = 1<<14
LED1 = 1<<18
LED2 = 1<<16
LED3 = 1<<19
LED4 = 1<<17
with open("/dev/mem", "r+b" ) as f:
  mem = mmap(f.fileno(), GPIO1_size, offset=GPIO1_offset)

packed_reg = mem[GPIO_OE:GPIO_OE+4]
reg_status = struct.unpack("<L", packed_reg)[0]
reg_status &= ~(LED1)
mem[GPIO_OE:GPIO_OE+4] = struct.pack("<L", reg_status)
try:
  while(True):
    mem[GPIO_SETDATAOUT:GPIO_SETDATAOUT+4] = struct.pack("<L", LED1)
    time.sleep(0.5)
    mem[GPIO_CLEARDATAOUT:GPIO_CLEARDATAOUT+4] = struct.pack("<L", LED1)
    time.sleep(0.5)
except KeyboardInterrupt:
  mem.close()