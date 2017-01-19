#!/usr/bin/env python

import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET means we want an Ipv4 socket
# SOCK_STREAM means we want a TCP socket

# connect
clientSocket.connect(("www.google.com", 80)) # 80:port (()): c API

request = "GET / HTTP/1.0\r\n\r\n" # \r\n indicate the end of the header

# send request
clientSocket.sendall(request)

# get respond back from google
response = bytearray()
while True:
    part = clientSocket.recv(1024)
    if(part):
        response.extend(part)
	#print 'aaaaaaaaaaaaaaa'
	#print part
    else:
        break;

#print response

