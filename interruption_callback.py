

def callback(p):
	print('pin change', p)

from machine import Pin
p0 = Pin(0, Pin.IN)
p2 = Pin(2, Pin.IN)

# on change, call callback method
# on p0, interrupt when high to low value
p0.irq(trigger=Pin.IRQ_FALLING, handler=callback)

# on p2, interrupt when both high to low, low to high value
p2.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=callback)