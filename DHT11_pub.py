import network

station = network.WLAN(network.STA_IF)
station.active(True)
station.ifconfig()
station.connect("SFR_F688","a9leffeadiceracychlo")


from time import sleep
from umqtt.simple import MQTTClient
from machine import Pin
from dht import DHT11


SERVER = '192.168.1.61' #MQTT Server address
CLIENT_ID = 'ESP32_DHT22_Sensor'
TOPIC = b'temp_humidity'

client = MQTTClient(CLIENT_ID, SERVER)
client.connect()

sensor = DHT11(Pin(15, Pin.IN, Pin.PULL_UP))


while True:
    try:
	sensor.measure()
	t = sensor.temperature()
	h = sensor.humidity()
	if isinstance(t, int) and isinstance(h, int):
	    msg = (b'{0:3.1f}, {1:3.1f}'.format(t,h))
	    client.publish(TOPIC, msg)
	    print(msg)
	else:
	    print('Invalid sensor readings.')
    except OSError:
	print('Failed to read sensor.')
    sleep(4)
