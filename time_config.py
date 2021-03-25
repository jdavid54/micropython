import time

# put to sleep = wait
#time.sleep(1)           # sleep for 1 second
#time.sleep_ms(500)      # sleep for 500 milliseconds
#time.sleep_us(10)       # sleep for 10 microseconds

# compute delta time
start = time.ticks_ms()  # get millisecond counter
time.sleep_us(100)
delta = time.ticks_diff(time.ticks_ms(), start) # compute time difference
print(delta)  # must be about 100