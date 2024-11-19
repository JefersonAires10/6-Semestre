from InquirerPy import prompt
from tcp_client import TCPClient

class User:
    def __init__(self, client):
        self.client = client

    def run(self):
        menu = [
            {
                'type': 'list',
                'name': 'service',
                'message': 'Escolha o serviço:',
                'choices': ['Calculadora', 'Decimal para Binário', 'Sair']
            }
        ]

        while True:
            service_choice = prompt(menu)['service']

            if service_choice == 'Calculadora':
                pergunta_calc = [
                    {
                        'type': 'list',
                        'name': 'op',
                        'message': 'Escolha a operação:',
                        'choices': ['+', '-', '*', '/']
                    },
                    {
                        'type': 'input',
                        'name': 'num1',
                        'message': 'Digite o primeiro número:'
                    },
                    {
                        'type': 'input',
                        'name': 'num2',
                        'message': 'Digite o segundo número:'
                    }
                ]
                answers = prompt(pergunta_calc)
                request = f"calc,{answers['op']},{answers['num1']},{answers['num2']}"

            elif service_choice == 'Decimal para Binário':
                pergunta_bin = [
                    {
                        'type': 'input',
                        'name': 'num',
                        'message': 'Digite um número decimal para converter em binário:'
                    }
                ]
                num = prompt(pergunta_bin)['num']
                request = f"bin,{num}"

            elif service_choice == 'Sair':
                print("Encerrando o cliente...")
                break

            self.client.connect()  
            self.client.send_request(request)
            response = self.client.get_response()
            print("From Server:", response)
            self.client.close()  

if __name__ == "__main__":
    client = TCPClient()
    user = User(client)
    user.run()