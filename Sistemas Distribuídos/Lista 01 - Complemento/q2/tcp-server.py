from socket import *
from CalcService import CalcService
from BinaryService import BinaryService

class TCPServer:
    
    def get_request(self, connectionSocket):
        try:
            sentence = connectionSocket.recv(1024)
            text = sentence.decode('utf-8')
            print("From Client:", text)
            
            parts = text.split(',')

            if len(parts) < 2:
                raise ValueError("Número de argumentos inválido")
                
            service = parts[0]

            if service == "calc": 
                if len(parts) != 4:
                    raise ValueError("Número de argumentos inválido para o serviço de calculadora")
                op, num1, num2 = parts[1], float(parts[2]), float(parts[3])
                result = CalcService.process(op, num1, num2)
            elif service == "bin":  
                num = float(parts[1])
                result = BinaryService.convert_to_binary(num)
            else:
                result = "Serviço inválido. Use 'calc' ou 'bin'."
        except Exception as e:
            result = f"Erro ao processar a solicitação: {str(e)}"

        return result

    def send_response(self, connectionSocket, result):
        connectionSocket.send(str(result).encode('utf-8'))
        connectionSocket.close()

    def run(self):
        serverPort = 12000
        serverSocket = socket(AF_INET, SOCK_STREAM)
        serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        serverSocket.bind(('', serverPort))
        serverSocket.listen(1)
        print("O servidor está pronto para receber")

        while True:
            connectionSocket, addr = serverSocket.accept()
            result = self.get_request(connectionSocket)
            self.send_response(connectionSocket, result)

if __name__ == "__main__":
    server = TCPServer()
    server.run()