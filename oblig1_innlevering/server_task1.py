from socket import *
import sys
import _thread as thread


serverSocket = socket(AF_INET,SOCK_STREAM) ##Creating a socket indicating IPV4 and TCP
serverPort = 20069
serverSocket.bind(("",serverPort)) #Assigning localhost and serverport to socket
serverSocket.listen(1) ##Listen for TCP connection
while True:
    print("Ready to server...")
    connectionSocket, addr = serverSocket.accept() #Accepting connection from browser and adding into connectionSocket
    try:
        message = connectionSocket.recv(1024).decode() #Receiving get request message from browser
        filename = message.split()[1] #adding /*requested file* into filename
        f = open(filename[1:]) #opening the requested file
        outputdata = f.read() #adding content from html file into outout data.
        f.close()
        responseHTTP = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: " + str(len(outputdata)) + "\r\n\r\n" #creating the first header respose
        connectionSocket.send(responseHTTP.encode()) # sending the header

        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode()) #sending the content in output data one element at time
        connectionSocket.send("r\n".encode()) #indicating end of header
        connectionSocket.close() #closing connection

    except IOError:
        htmlError="HTTP/1.1 400\r\n\r\n"
        connectionSocket.send(htmlError.encode())
        connectionSocket.close()
        #thread.start_new_thread(handleClient, (connectionSocket,))
        print('Server connected by ', addr) 
    
serverSocket.close()
sys.exit()   

