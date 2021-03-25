# ----- Python program for querying whois information -----

import socket
# Create a TCP socket

# By default family=AF_INET, type=SOCK_STREAM
whoisClient = socket.socket()

# Make a connect to the server - TCP does a 3 way handshake
whoisClient.connect(("whois.avalidwhoisserver.tld", 43))
#whoisClient.connect(("whois.avalidwhoisserver.tld", 43))   # Active open
whoisClient.sendall("example.com".encode())   

# Buffer size to receive reply from whois server
bufferSize = 4096
# Read the whole reply from whois server

while(True):
    data = whoisClient.recv(4096)
    lines = data.decode().splitlines()
    if(len(lines) > 0):
        for line in lines:
            if(len(line)>0):
                print(line)
    if(data==b''):
        print("Connection closed")
        break