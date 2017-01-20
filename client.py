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
        break

print response


# same output as tying curl -i www.google.com
'''
HTTP/1.0 302 Found
Cache-Control: private
Content-Type: text/html; charset=UTF-8
Location: http://www.google.ca/?gfe_rd=cr&ei=Y2-BWKbeNube8Afz54jwCw
Content-Length: 258
Date: Fri, 20 Jan 2017 02:01:07 GMT

<HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
<TITLE>302 Moved</TITLE></HEAD><BODY>
<H1>302 Moved</H1>
The document has moved
<A HREF="http://www.google.ca/?gfe_rd=cr&amp;ei=Y2-BWKbeNube8Afz54jwCw">here</A>.
</BODY></HTML>

'''

