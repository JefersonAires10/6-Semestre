from socket import *

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

while True:
    sentence = input('Digite sua operação no formato op,num1,num2 (ou "sair" para encerrar): ')
    if sentence.lower() == 'sair':
        break
    clientSocket.send(sentence.encode('utf-8'))
    modifiedSentence = clientSocket.recv(1024)
    text = modifiedSentence.decode('utf-8')
    print("From Server:", text)

clientSocket.close()
print("Conexão encerrada.")