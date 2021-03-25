import network
from time import sleep
from umqtt.simple import MQTTClient
from machine import Pin
from dht import DHT11


led = Pin(2, Pin.OUT)
sensor = DHT11(Pin(15, Pin.IN, Pin.PULL_UP))

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect("ssid","passwd")
while station.isconnected() == False:
  pass
print('Connection successful')
print(station.ifconfig())

#flash once 
led.value(1)
sleep(0.1)
led.value(0)
sleep(1)


SERVER = "test.mosquitto.org"
CLIENT_ID = 'ESP32_DHT22_Sensor'
TOPIC = b'temp_humidity'

client = MQTTClient(CLIENT_ID, SERVER)
client.connect()

#flash once
led.value(1)
sleep(0.1)
led.value(0)
sleep(1)

while True:
    try:    # si il y a DHT11
        sensor.measure()
        t = sensor.temperature()
        h = sensor.humidity()
        if isinstance(t, int) and isinstance(h, int):
            msg = (b'{0:3.1f}, {1:3.1f}'.format(t,h))
            client.publish(TOPIC, msg)
            led.value(1)
            sleep(0.1)
            led.value(0)
            sleep(0.1)
            led.value(1)
            sleep(0.1)
            led.value(0)
            print(msg)
        else:                # si il n'y a pas de DHT11
            msg = 'Invalid sensor readings.'
            client.publish(TOPIC, msg)
    except OSError:         # ou erreur de lecture
        msg = 'Failed to read sensor.'
        client.publish(TOPIC, msg)
    sleep(5)
