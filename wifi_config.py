import network

# interface  access point
ap_if = network.WLAN(network.AP_IF)
ap_if.active()
# deactive access point
ap_if.active(False)
ap_if.ifconfig()

# interface station
sta_if = network.WLAN(network.STA_IF)

# test interface
sta_if.active()

# configure wifi
sta_if.active(True)

essid = ''
password = ''

sta_if.connect(essid, password)
sta_if.isconnected()
sta_if.ifconfig()


def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(essid, password)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

#do_connect()