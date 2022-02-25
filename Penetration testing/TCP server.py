#CREATING TPC SERVER

import socket

#This is the server socket object, this specifies the socket family and the socket type
#AF_INET means we are working with IPV4 and SOCK_STREAM tells us what type of comunication we are using (in this case is TCP)

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#We need to create another object to store the hostname and define a port to listen (host = your IP address)

host = socket.gethostbyname()
port = 444

#Now we need to bind the values that we got back from the host and port to the object we created (server socket) 

serversocket.bind(host, port) # host = IP address

#Now we need to setup a TCP listener for TPC connections from client
#In the parameters of listen() we can specify how many connections we an listen at a time

serversocket.listen(3)

#As we can decide how many connections we have at a time we create a loop that while we got the address and the server socket accept the connection, if this is true, then print a message that we got the connection

while True:
    clientsocket, address = serversocket.accept()

    print("Received connection from: %s " % str(address))

    message = "Hello, thank you for connecting to the server" + "\r\n"
    clientsocket.send(message.encode('ascii'))

#Then we can close the socket

    clientsocket.close()