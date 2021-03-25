import socket

# Query for socket information to connect to example.com
addrInfo = socket.getaddrinfo("example.com",80)
# print socket tuples
print(addrInfo)
print('addr',addrInfo[0][-1])

# Query for socket info - Criteria is IPv4, TCP
addressInfo4 = socket.getaddrinfo("example.com", 80, family=socket.AF_INET, proto=socket.IPPROTO_TCP)
# Print socket info
print(addressInfo4)
print('addr4',addressInfo4[0][-1])

# Query for socket info - Criteria is IPv6, TCP
addressInfo6 = socket.getaddrinfo("example.com", 80, family=socket.AF_INET6, proto=socket.IPPROTO_TCP)
# Print socket info
print(addressInfo6)
print('addr6',addressInfo6[0][-1])


# https://pythontic.com/modules/socket/socket
addr = addrInfo[0][-1]
s = socket.socket()
print(s)
#s.bind(addr)
#s.listen(1)

addrInfo = socket.getaddrinfo("192.168.1.61",1888)
addr = addrInfo[0][-1]
print('addr',addr)
s.bind(addr)
s.listen(1)
