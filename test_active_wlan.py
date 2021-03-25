
'''
import network
station = network.WLAN(network.STA_IF)
station.active(True)
'''
import wifi
import sys

print(help(wifi))

from wifi import scan
print(dir(scan))