import yaml

dados = {
    'nome': 'João',
    'idade': 25,
    "cursos": ['Python', 'Django', 'Flask']
}

with open('dados.yaml', 'w') as file:
    yaml.dump(dados, file)