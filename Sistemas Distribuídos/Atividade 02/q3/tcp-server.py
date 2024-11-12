from socket import *
from threading import Thread

def handle_client(connectionSocket):
    while True:
        sentence = connectionSocket.recv(1024).decode('utf-8')
        if sentence == 'exit':
            print("Client disconnected")
            break
        print(f"Client: {sentence}")
        response = input("You: ")
        connectionSocket.send(response.encode('utf-8'))
        if response == 'exit':
            break
    connectionSocket.close()

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is ready to receive")

while True:
    connectionSocket, addr = serverSocket.accept()
    print(f"Connected to {addr}")
    client_thread = Thread(target=handle_client, args=(connectionSocket,))
    client_thread.start()