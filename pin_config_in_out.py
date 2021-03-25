import machine

#pin = machine.Pin(0)

# config pin as input, pull-up
pin = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)


# read pin value
pin.value()

# config pin as oputput
pin = machine.Pin(0, machine.Pin.OUT)

# write value to pin
pin.value(0)
pin.value(1)