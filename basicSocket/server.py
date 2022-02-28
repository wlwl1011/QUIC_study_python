from socket import *

# server socket setting
serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', 8080))
serverSock.listen(1)

# accept 함수는 누군가가 접속을 해야지 return 함
clientSock, addr = serverSock.accept()
print(str(addr), 'accesses now')

data = clientSock.recv(1024)
print('recieved the data: ', data.decode('utf-8'))

clientSock.send('Hi. I am server :)'.encode('utf-8'))
print('Compelte the sending')
