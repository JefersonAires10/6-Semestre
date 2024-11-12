from socket import *
from threading import Thread

def receive_messages(clientSocket):
    while True:
        modifiedSentence = clientSocket.recv(1024).decode('utf-8')
        if modifiedSentence == 'exit':
            print("Server disconnected")
            break
        print(f"From Server: {modifiedSentence}")

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

receive_thread = Thread(target=receive_messages, args=(clientSocket,))
receive_thread.start()

while True:
    sentence = input("You: ")
    clientSocket.send(sentence.encode('utf-8'))
    if sentence == 'exit':
        break

clientSocket.close()