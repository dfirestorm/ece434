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
 button_and_light reads 2 switches to control 2 LEDs. 