import machine
p12 = machine.Pin(12)

# Then create the PWM object using:
pwm12 = machine.PWM(p12)

#You can set the frequency and duty cycle using:

# set values
pwm12.freq(500)
pwm12.duty(512)

pwm12

# get values
pwm12.freq()
pwm12.duty()