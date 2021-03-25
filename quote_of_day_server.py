# ----- A Python program implementing a Quote of the Day server -----
# Run this program then
# Launch quote_of_day_client in terminal :
#     python3 quote_of_day_client.py

import socket
import datetime
from random import randint

quotes = [ ("I love going to coffee shops and just sitting and listening.", "Julie Roberts"),

           ("Know thyself", "Socrates"),

           ("For knowledge itself is Power", "Francis Bacon"),

           ("Nothing is worth more than this day", "Goethe"),

           ("Ah! happy years! once more who would not be a boy","Byron: Child Harold")];

qotdPortNumber      = 32017;
qotdServerSocket    = socket.socket();
qotdServerSocket.bind(("127.0.0.1", qotdPortNumber));
qotdServerSocket.listen();
print("Quote of the day requests welcome:");

while(True):
    # accept when client connect on socket
    (socketForClient, clientIP) = qotdServerSocket.accept();
    # Pick a random quote
    quoteIndex      = randint(0, 4);
    quoteOfTheDay   = "%s - %s"%(quotes[quoteIndex][0],quotes[quoteIndex][1]);
    # encode message
    encodedMsg      = quoteOfTheDay.encode();
    # send message
    socketForClient.send(encodedMsg);
    # get time
    timeVal = datetime.datetime.now();
    # report
    print("%s Just served: %s, to client with IP address and port: %s"%(timeVal, quoteOfTheDay, clientIP));
    # close connection
    socketForClient.close();