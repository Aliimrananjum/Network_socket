import string
import sys
from socket import *

argument = sys.argv #

clientSocket = socket(AF_INET, SOCK_STREAM)

serverName = argument[1]
serverPort = int(argument[2])
path = argument[3]
clientSocket.connect((serverName,serverPort))
sendmsg = "GET /" + path + " HTTP/1.1"
clientSocket.send(sendmsg.encode())
receiveMsg1 = clientSocket.recv(1024).decode()
response = receiveMsg1
while len(receiveMsg1) > 0:
    receiveMsg1 = clientSocket.recv(1024).decode()
    response += receiveMsg1
print(response)

