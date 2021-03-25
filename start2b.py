from microWebSrv import MicroWebSrv
from machine import Pin
from dht import DHT11
from time import sleep
from umqtt.simple import MQTTClient

# DHT11
sensor = DHT11(Pin(15, Pin.IN, Pin.PULL_UP))   # DHT-11 on GPIO 15

# MQTT
SERVER = '192.168.1.61' #MQTT Server address
CLIENT_ID = 'ESP32_DHT22_Sensor'
TOPIC = b'temp_humidity'

client = MQTTClient(CLIENT_ID, SERVER)
client.connect()


def _httpHandlerDHTGet(httpClient, httpResponse):
    try:
        sensor.measure()   # Poll sensor
        t, h = sensor.temperature(), sensor.humidity()
        if all(isinstance(i, int) for i in [t, h]):   # Confirm values
            data = '{0:.1f}&deg;C {1:.1f}%'.format(t, h)
	    msg = (b'{0:3.1f}, {1:3.1f}'.format(t,h))
	    client.publish(TOPIC, msg)	
        else:
            data = 'Invalid reading.'
    except:
        data = 'Attempting to read sensor...'
        
    httpResponse.WriteResponseOk(
        headers = ({'Cache-Control': 'no-cache'}),
        contentType = 'text/event-stream',
        contentCharset = 'UTF-8',
        content = 'data: {0}\n\n'.format(data) )

routeHandlers = [ ( "/dht", "GET",  _httpHandlerDHTGet ) ]
srv = MicroWebSrv(routeHandlers=routeHandlers, webPath='/www/')
srv.Start(threaded=False)
