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
            return "Erro: Divisão por zero"
        return num1 / num2
    else:
        return "Operação inválida"

def decimal_to_binary(num):
    try:
        return bin(int(num))[2:]
    except ValueError:
        return "Erro: Entrada inválida para conversão"

def process_operation(connectionSocket):
    try:
        sentence = connectionSocket.recv(1024)
        text = sentence.decode('utf-8')
        print("From Client:", text)
        
        parts = text.split(',')

        if(parts.length < 4):
            raise ValueError("Número de argumentos inválido")
            

        service = parts[0]

        if service == "calc": 
            op, num1, num2 = parts[1], float(parts[2]), float(parts[3])
            result = calculate(op, num1, num2)
        elif service == "bin":  
            num = float(parts[1])
            result = decimal_to_binary(num)
        else:
            result = "Serviço inválido. Use 'calc' ou 'bin'."
    except Exception as e:
        result = f"Erro ao processar a solicitação: {str(e)}"

    connectionSocket.send(str(result).encode('utf-8'))
    connectionSocket.close()

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("O servidor está pronto para receber")

while True:
    connectionSocket, addr = serverSocket.accept()
    thread = threading.Thread(target=process_operation, args=(connectionSocket,))
    thread.start()
