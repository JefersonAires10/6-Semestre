import time
from socket import *
import threading
from CalcService import Calculator

successful_operations = 0
lock = threading.Lock()

def process_operation(connectionSocket):
    global successful_operations
    try:
        sentence = connectionSocket.recv(1024)
        time.sleep(0.1)
        text = sentence.decode('utf-8')
        
        parts = text.split(';')

        if len(parts) != 3:
            raise ValueError("Número de argumentos inválido")
            
        op, num1, num2 = parts[0], float(parts[1]), float(parts[2])
        calculator = Calculator()
        result = calculator.calculate(op, num1, num2)
        
        with lock:
            successful_operations += 1
        
    except Exception as e:
        result = f"Erro ao processar a solicitação: {str(e)}"

    connectionSocket.send(str(result).encode('utf-8'))
    connectionSocket.close()

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(100)
print("O servidor multithread está pronto para receber na porta 12000")

while True:
    connectionSocket, addr = serverSocket.accept()
    thread = threading.Thread(target=process_operation, args=(connectionSocket,))
    thread.start()
    
    with lock:
        print(f"Operações bem-sucedidas: {successful_operations}")