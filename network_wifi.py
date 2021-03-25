import network

station = network.WLAN(network.STA_IF)
station.active(True)
station.ifconfig()
station.connect("SFR_F688","a9leffeadiceracychlo")