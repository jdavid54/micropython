#from machine import Pin
#from machine import ADC
from time import sleep
import socket

#import machine

html = """
<h1> Test d'affichage de température !!!!!</h1>
<br>
 <h2>Température : %s °C</h2>
<br>
<h1>Fin de message !</h1>
"""

celsius_temp = '10.0'
'''
ledblue = Pin(16, Pin.OUT) #bleu
ledgreen = Pin(5, Pin.OUT) #vert
ledred = Pin(4, Pin.OUT) #rouge

adc = ADC(0) #LM35 sur l'analogique 0
 
# clignotement des LEDs
ledgreen.value(0)
ledblue.value(0)
ledred.value(0)
# alumme led bleue
ledblue.value(1)
sleep(.3)
# éteint led bleue et allume led verte
ledblue.value(0)
ledgreen.value(1)
sleep(.3)
# éteint led verte et allume led rouge
ledgreen.value(0)
ledred.value(1)
sleep(.3)
# # éteint led rouge
ledred.value(0)
sleep(1)
'''
#socket.getaddrinfo(host, port, family=0, type=0, proto=0, flags=0)
# return a tuple
addr = socket.getaddrinfo('127.0.0.1', 8080)[0][-1]  # first list element, last item
s = socket.socket()
s.bind(addr)
s.listen(1)

while True:
    print('Boucle ') 
    s.settimeout(2)
    
    try: 
        conn, addr = s.accept()
        print('accept', conn, addr)
    except OSError as er:
        pass
        print(er.args[0] in (110, 'timed out'))
        # 110 is ETIMEDOUT
    else:
        print('Client connecté de ', addr)
        conn_file = conn.makefile('rwb', 0)
        while True:
            line = conn_file.readline()
            print('Line ', line)
            if not line or line == b'\r\n':
                print('break')
                break
        print('============') 
        response = bytes(html % celsius_temp + '\n', 'latin8')
        print('Client receives ', response)
        conn.send(b'HTTP/1.1 200 OK\n')
        conn.send(b'Content-Type: text/html\n')
        conn.send(b'Connection: close\n\n')
        conn.sendall(response)
        conn.close()
        #conn.close()
        '''
        reading = adc.read()
        celsius_temp = round(reading/3.95, 1)
        #print(celsius_temp)

        ledgreen.value(0)
        ledblue.value(0)
        ledred.value(0)

        if (celsius_temp) > 24.0:
            ledred.value(1)
        elif (celsius_temp) < 22.0:
            ledblue.value(1)
        else:
            ledgreen.value(1)
        '''
