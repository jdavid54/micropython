from machine import Pin, I2C

'''
# scl = 18, sda = 19
i2c = I2C(0)

# scl = 25, sda = 26
i2c = I2C(1)

# or define pins and frequency
i2c = I2C(1, scl=Pin(5), sda=Pin(4), freq=400000)
'''
# construct an I2C bus
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)

i2c.readfrom(0x3a, 4)   # read 4 bytes from slave device with address 0x3a
i2c.writeto(0x3a, '12') # write '12' to slave device with address 0x3a

buf = bytearray(10)     # create a buffer with 10 bytes
i2c.writeto(0x3a, buf)  # write the given buffer to the slave