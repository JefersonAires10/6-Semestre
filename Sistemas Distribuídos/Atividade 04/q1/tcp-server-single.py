import time
from socket import *

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

serverPort = 12001
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(100)
print("O servidor single thread está pronto para receber na porta 12001")

while True:
    connectionSocket, addr = serverSocket.accept()
    try:
        sentence = connectionSocket.recv(1024)
        time.sleep(0.1)
        text = sentence.decode('utf-8')
        
        parts = text.split(';')

        if len(parts) != 3:
            raise ValueError("Número de argumentos inválido")
            
        op, num1, num2 = parts[0], float(parts[1]), float(parts[2])
        result = calculate(op, num1, num2)
        
    except Exception as e:
        result = f"Erro ao processar a solicitação: {str(e)}"

    connectionSocket.send(str(result).encode('utf-8'))
    connectionSocket.close()