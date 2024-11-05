import time
from socket import *
from threading import Thread

def handle_client(connectionSocket):
    while True:
        sentence = connectionSocket.recv(1024).decode('utf-8')
        print("Received message: ", sentence)
        if sentence == 'exit':
            break
        capitalizedSentence = sentence.upper()
        connectionSocket.send(capitalizedSentence.encode('utf-8'))
    connectionSocket.close()

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is ready to receive")

while True:
    connectionSocket, addr = serverSocket.accept()
    thread = Thread(target=handle_client, args=(connectionSocket,))
    thread.start()