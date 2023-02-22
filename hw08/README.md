# hw08
PRU
## PRU
 make table with results summary and inline screen captures to support the data

### blinking an led
none of the commands actually require make start -  the make with target will autostart them (and kill anything currently running)


### PWM generator
 the output is already set for P9_31? 
 pwm_max_freq is from pwm2.pru0


### controlling pwm frequency
 it works nicely. 
 surprisingly pwm4 is set for max speed but running a modified pwm-test (delay 4 instead of 20) achieves faster results


|question | answer|
|------------------|--------------------|
|What command starts pru code| make start |
|what command stops pru code | make stop |
| how fast can toggle pin | 12.5 MHz |
|is there jitter? is it stable | infrequent mild jitter but consistent over/undershoot on both sides and fairly stable frequency|
|------------- | -----------|
| PWM stability | the waveform is very stable  |
| PWM std dev | 300 kHz |
| PWM jitter | there's definitely mild jitter but it's running at a good 50 MHz |
|------------- | -----------|
| PWM pins | P9_28-31 |
| PWM R30 used | bits 0-3 |
| PWM highest freq possible | 401 kHz |
| PWM jitter | none |
| PWM change on/off via pwm-test.c | yes, had to modify pwm-test to achieve 400 kHz |
|------------- | -----------|

### reading input at regular intervals
 input max speed was at least 15 MHz, around 15.7 MHz it starts to have errors 
 input delay was approx 20 ns both edges

### analog wave generator
 the analog wave worked fairly nice. the captures are in this folder. 


# hw08 grading

| Points      | Description | |
| ----------- | ----------- |-|
| 14/14 | PRU
|  2/2 | Controlling the PWM Frequency - optional
|  2/2 | Reading an Input at Regular Intervals - optional
|  2/2 | Analog Wave Generator - optional
| 20/20 | **Total**

*My comments are in italics. --may*
