def toggle(p):
	p.value(not p.value())

import time
pin = 4
while True:
	toggle(pin)
	time.sleep_ms(500)