from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = input('Input lowercase sentence:')

while sentence != 'exit':
    clientSocket.send(sentence.encode('utf-8'))
    modifiedSentence = clientSocket.recv(1024)
    print('From Server:', modifiedSentence.decode('utf-8'))
    sentence = input('Input lowercase sentence:')
    
clientSocket.close()