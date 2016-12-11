#!/usr/bin/env python
import socket
TCP_IP = '172.20.3.235'
TCP_PORT = 8800
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
#FFFFFF
while True:
	data = s.recv(BUFFER_SIZE)
	print "El serve dijo: ", data
	msg=raw_input('Ingrese un texto: ')
	if msg !=0:
		s.send(msg)
		'''print "Mensaje enviado: ", msg''' 
	else:
		break
		print 'Hasta luego'
		s.close()
