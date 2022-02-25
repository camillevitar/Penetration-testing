#CREATING TPC CLIENT

import socket

#This is the client socket object, this specifies the socket family and the socket type
#AF_INET means we are working with IPV4 and SOCK_STREAM tells us what type of comunication we are using (in this case is TCP)

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#This is going to be the server IP now, here you'd have to specify it every time or make sure the client does know the IP address

host = socket.gethostbyname()
port = 444 #Port is supposed to match with server

clientsocket.connect(host, port) #host is the IP address, can use this or the address instead

#We have to make sure the units the data is coming or the certain amount of bytes, to not accept more data than we need

message = clientsocket.recv(1024) #1024 is the maximum amount of data we will receive

#Since we have received the data we now have to decode the message (message is encoded in ascii) 
#Decoding the message will take a while so we can close the socket and then decode the message

clientsocket.close()

print(message.decode('ascii'))