'''
The deep-sleep mode will shut down the ESP8266 and all its peripherals, 
including the WiFi (but not including the real-time-clock, which is used 
to wake the chip). This drastically reduces current consumption and is a 
good way to make devices that can run for a while on a battery.

To be able to use the deep-sleep feature you must connect GPIO16 to the 
reset pin (RST on the Adafruit Feather HUZZAH board). 
'''

import machine

# configure RTC.ALARM0 to be able to wake the device
rtc = machine.RTC()
rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)

# set RTC.ALARM0 to fire after 10 seconds (waking the device)
rtc.alarm(rtc.ALARM0, 10000)

# put the device to sleep
machine.deepsleep()

#test to include in boot.py
if machine.reset_cause() == machine.DEEPSLEEP_RESET:
    print('woke from a deep sleep')
else:
    print('power on or hard reset')