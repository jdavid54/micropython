from machine import Pin

'''
Available Pins are from the following ranges (inclusive):
 0-19, 21-23, 25-27, 32-39. 
These correspond to the actual GPIO pin numbers of ESP32 chip. 

Pins 1 and 3 are REPL UART TX and RX respectively
Pins 6, 7, 8, 11, 16, and 17 are used for connecting the embedded flash, and are not recommended for other uses
Pins 34-39 are input only, and also do not have internal pull-up resistors

The pull value of some pins can be set to Pin.PULL_HOLD to reduce power consumption during deepsleep.
'''

p0 = Pin(0, Pin.OUT)    # create output pin on GPIO0
p0.on()                 # set pin to "on" (high) level
p0.off()                # set pin to "off" (low) level
p0.value(1)             # set pin to on/high

p2 = Pin(2, Pin.IN)     # create input pin on GPIO2
print(p2.value())       # get value, 0 or 1

p4 = Pin(4, Pin.IN, Pin.PULL_UP) # enable internal pull-up resistor
p5 = Pin(5, Pin.OUT, value=1) # set pin high on creation