from socket import *
from threading import Thread
import time

def client_request(port):
    try:
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect(('localhost', port))
        clientSocket.send("ADD;10;11".encode('utf-8'))
        response = clientSocket.recv(1024).decode('utf-8')
        clientSocket.close()
    except Exception as e:
        print(f"Erro ao enviar solicitação: {str(e)}")

def run_load_test(port):
    num_clients = 100
    threads = []

    start_time = time.time()

    for _ in range(num_clients):
        thread = Thread(target=client_request, args=(port,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"Tempo total de execução para porta {port}: {end_time - start_time} segundos")

if __name__ == "__main__":
    print("Testando servidor singlethread na porta 12001")
    run_load_test(12001)
    
    print("Testando servidor multithread na porta 12000")
    run_load_test(12000)