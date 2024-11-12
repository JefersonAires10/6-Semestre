from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is ready to receive")

connectionSocket, addr = serverSocket.accept()
print(f"Connected to {addr}")

while True:
    sentence = connectionSocket.recv(1024).decode('utf-8')
    print("Received message: ", sentence)
    if sentence == 'exit':
        print("Client disconnected")
        break

    response = input("You: ")
    connectionSocket.send(response.encode('utf-8'))
    if response == 'exit':
        break
    connectionSocket.close()
    
serverSocket.close()