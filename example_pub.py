import network

station = network.WLAN(network.STA_IF)
station.active(True)
station.ifconfig()
station.connect("SFR_F688","a9leffeadiceracychlo")

from umqtt.simple import MQTTClient

# Test reception e.g. with:
# mosquitto_sub -t foo_topic

# Default MQTT server to connect to
SERVER = "192.168.1.61"
CLIENT_ID = "ESP32"   #ubinascii.hexlify(machine.unique_id())
TOPIC = b"foo_topic"
MSG = b"hello from ESP32" 

def send_msg(server=SERVER, client_id=CLIENT_ID, topic=TOPIC, msg=MSG):
	print(server, client_id, topic)
	c = MQTTClient(client_id, server)
	c.connect()
	c.publish(topic, msg)
	print('Message sent')
	c.disconnect()

'''
if __name__ == "__main__":
    main()
'''