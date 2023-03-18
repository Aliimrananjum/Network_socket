import sys
from socket import *

argument = sys.argv ##creating a array with arguements from terminal.

clientSocket = socket(AF_INET, SOCK_STREAM) ##Creating a client socket indicating IPV4 and TCP

serverName = argument[1] #adding element in index 1 into variabel
serverPort = int(argument[2]) #adding element in index 2 into variabel. Convert as integer
path = argument[3] #adding element in index 3 into variabel. request file.
clientSocket.connect((serverName,serverPort))##Intiates the TCP connection between the client and server.
sendmsg = "GET /" + path + " HTTP/1.1" #creating header 
clientSocket.send(sendmsg.encode()) ##sending the header to server
receiveMsg1 = clientSocket.recv(1024).decode() ##receving response from server with kode 200 
response = receiveMsg1
while len(receiveMsg1) > 0:
    receiveMsg1 = clientSocket.recv(1024).decode() ##continue to receive content from html file.
    response += receiveMsg1
print(response)

