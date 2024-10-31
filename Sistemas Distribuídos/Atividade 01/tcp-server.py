import time
from socket import *
import threading

def calculate(op, num1, num2):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        if num2 == 0:
            return "Erro: Temos uma Indeterminação"
        return num1 / num2
    else:
        return "Operação inválida"

def process_operation(connectionSocket):
    try:
        sentence = connectionSocket.recv(1024)
        text = sentence.decode('utf-8')
        print("From Client:", text)
        
        op, num1, num2 = text.split(',')
        num1 = float(num1)
        num2 = float(num2)
        result = calculate(op, num1, num2)
    except ValueError:
        result = "Formato inválido. Use: op,num1,num2"
    
    connectionSocket.send(str(result).encode('utf-8'))
    connectionSocket.close()

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is ready to receive")

while True:
    connectionSocket, addr = serverSocket.accept()
    thread = threading.Thread(target=process_operation, args=(connectionSocket,))
    thread.start()