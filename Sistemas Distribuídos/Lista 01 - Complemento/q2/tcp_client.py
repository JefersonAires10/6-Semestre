from socket import *

class TCPClient:
    def __init__(self, server_address='localhost', server_port=12000):
        self.server_address = server_address
        self.server_port = server_port
        self.client_socket = None

    def connect(self):
        self.client_socket = socket(AF_INET, SOCK_STREAM)
        self.client_socket.connect((self.server_address, self.server_port))

    def send_request(self, request):
        self.client_socket.send(request.encode('utf-8'))

    def get_response(self):
        return self.client_socket.recv(1024).decode('utf-8')

    def close(self):
        self.client_socket.close()