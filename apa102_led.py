import machine, apa102


'''
This configures an 60 pixel APA102 strip with clock on GPIO5 and data on GPIO4. 
You can adjust the pin numbers and the number of pixels to suit your needs.
'''
strip = apa102.APA102(machine.Pin(5), machine.Pin(4), 60)
strip.ORDER = (0, 2, 1, 3)

strip[0] = (255, 255, 255, 31) # set to white, full brightness
strip[1] = (255, 0, 0, 31) # set to red, full brightness
strip[2] = (0, 255, 0, 15) # set to green, half brightness
strip[3] = (0, 0, 255, 7)  # set to blue, quarter brightness

strip.write()