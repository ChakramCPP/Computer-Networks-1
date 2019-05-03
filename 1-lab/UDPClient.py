from socket import *
# import socket
serverName = 'localhost'
serverPort = 2000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input lowercase sentence: ').encode()
clientSocket.sendto(message, (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()
