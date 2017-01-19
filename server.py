#!/usr/bin/env python

import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

serverSocket.bind(("0.0.0.0", 8000))
serverSocket.listen(5) # keep up to 5 

while True:
	(incomingSocket, address) = serverSocket.accept() # address: who connect u
	print "Got a connection from %s" % (repr(address))
	clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# AF_INET means we want an Ipv4 socket
	# SOCK_STREAM means we want a TCP socket

	# connect
	clientSocket.connect(("www.google.com", 80)) # 80:port (()): c API
	
	incomingSocket.setblocking(0)
	clientSocket.setblocking(0)
	while True:
		request = bytearray()
		while True:
			try: # try to read, if nothing to read, break the loop
				part = incomingSocket.recv(1024)
			except IOError, e:
				if e.errno == socket.errno.EAGAIN:
					break
				else:
					raise
			if(part):
				request.extend(part)
				clientSocket.sendall(part)
			else: # ctrl C make part an empty string
				break;
		if len(request) > 0:
			print (request)

		# opposite side
		response = bytearray()
		while True:
			try: # try to read, if nothing to read, break the loop
				part = clientSocket.recv(1024)
			except IOError, e:
				if e.errno == socket.errno.EAGAIN:
					break
				else:
					raise
			#part = clientSocket.recv(1024)
			if(part):
				response.extend(part) # reading from google
				incomingSocket.sendall(part) # from browser
			else: # ctrl C make part an empty string
				break;
		if len(response) > 0:
			print (response)
