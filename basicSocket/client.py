from socket import *

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1', 8080))

print('Complete the connection.')
clientSock.send('Hi. I am client :)'.encode('utf-8'))
print('Compelte the sending')

data = clientSock.recv(1024)
print('recieved the data: ', data.decode('utf-8'))
