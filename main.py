import network

print('=====================================Connecting to wifi')
station = network.WLAN(network.STA_IF)
station.active(True)
station.ifconfig()
station.connect("SFR_F688","a9leffeadiceracychlo")

print('=============================================Connected!')
