import machine

servo = machine.PWM(machine.Pin(12), freq=50)
servo.duty(40)
servo.duty(115)
servo.duty(77)