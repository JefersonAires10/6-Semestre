from socket import *
from InquirerPy import prompt

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

menu = [
    {
        'type': 'list',
        'name': 'service',
        'message': 'Escolha o serviço:',
        'choices': ['Calculadora', 'Decimal para Binário']
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
        sentence = f"calc,{answers['op']},{answers['num1']},{answers['num2']}"

    elif service_choice == 'Decimal para Binário':
        pergunta_bin = [
            {
                'type': 'input',
                'name': 'num',
                'message': 'Digite um número decimal para converter em binário:'
            }
        ]
        num = prompt(pergunta_bin)['num']
        sentence = f"bin,{num}"
    
    clientSocket.send(sentence.encode('utf-8'))
    modifiedSentence = clientSocket.recv(1024)
    text = modifiedSentence.decode('utf-8')
    print("From Server:", text)

clientSocket.close()
print("Conexão encerrada.")
