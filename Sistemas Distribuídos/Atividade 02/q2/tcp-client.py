from socket import *

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

while True:
    sentence = input("You: ")
    clientSocket.send(sentence.encode('utf-8'))
    if sentence == 'exit':
        break

    modifiedSentence = clientSocket.recv(1024).decode('utf-8')
    print('From Server:', modifiedSentence)
    if modifiedSentence == 'exit':
        print("Server disconnected")
        break

clientSocket.close()