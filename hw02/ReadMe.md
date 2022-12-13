# hw02

## Buttons and LEDs

### Wiring
Buttons are on header P8, pins 11,12,15,16
LEDS are on header P9, pins 14,15,16,23
### Switch and light
this program maps each button to a led. it uses the gpiod library to do so. 
### Measuring GPIO pins via oscilloscope
1. What's the min and max voltage?
    the minimum and maximum voltages are 0V and 320 mV approximately
2. What period and frequency is it?
    the period is 290 ms and the frequency is 3.417 Hz
3. How close is it to 100ms?
    The period is almost 3x longer than the desired 100 ms
4. Why do they differ?
    They differ because the processor is waiting 100 ms in addition to the time it takes to toggle the pin
5. Run htop and see how much processor you are using.
    The shell version uses about 3.4% processor at max
6. Try different values for the sleep time (2nd argument). What's the shortest period you can get? Make a table of the fastest values you try and the corresponding period and processor usage. Try using markdown tables: https://www.markdownguide.org/extended-syntax/#tables

|sleep time | period | processor usage |
|-----------|--------|-----------------|
|0.1 | 290 | 3.4 |
|0.01 | 116 | 7.4 |
|0.001|88 | 9.5 |
|0.001 vscode off |45 | 18.9 |

Anything shorter than this is generally negligible waiting


7. How stable is the period?
    the period is very unstable to be honest, at least 10 ms fluctuations
8. Try launching something like vi. How stable is the period?
    the period has become even more unstable if that's possible
9. Try cleaning up togglegpio.sh and removing unneeded lines. Does it impact the period?
    getting rid of the writing things gets the period down to 20 ms
10. Togglegpio.sh uses bash (first line in file). Try using sh. Is the period shorter?
    the period is around 5 ms shorter or 15 ms. 

11. What's the shortest period you can get?
    with 0.0001 wait, period is 12.977 ms with sh

### timing comparison


## Etch - A - Sketch

### What it does
This program runs in any python enabled terminal which supports printing. It asks for what size board you would like and allows for movement of the cursor with the buttons mentioned above. 

### How to run
this program can be run with the command: 
`./etch_a_sketch.py`
it requires than the standard python utilities and the ability to print. 
It also requires 4 buttons. 

