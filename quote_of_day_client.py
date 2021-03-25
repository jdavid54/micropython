# ----- Example Python program to connect to a Quote of the Day server -----
# Launch quote_of_day_server in terminal :
#     python3 quote_of_day_server.py
# then run this program

import socket
import datetime
# Server IP address and Port
qotdServerIP    = "127.0.0.1"
qotdServerPort  = 32017

# Create client socket instance
qotdClient =  socket.socket()
# print(qotdClient)
# Connect to the quote of the day server
# No need to send any message to server
# Server replies with a quote upon receiving a client connection
qotdClient.connect((qotdServerIP, qotdServerPort))

# Get the reply
quoteOfTheDay = qotdClient.recv(1024)

# Decode message and print the reply
timeVal = datetime.datetime.now().ctime();

print("Quote of the day for %s:\n%s"%(timeVal,quoteOfTheDay.decode(encoding='utf-8')))
