import logging
import yaml
import json

# Ler as configurações do arquivo YAML.
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

# Configurar o sistema de logging.
logging.basicConfig(
    filename=config["logging"]["file"],
    level=getattr(logging, config["logging"]["level"]),
    format=config["logging"]["format"],
)

# Ler e processar os dados JSON.
with open(config["data"]["file"], "r") as file:
    data = json.load(file)

# Registrar eventos no log.
logging.info("Configurações lidas com sucesso.")
logging.info(f"Arquivo JSON '{config['data']['file']}' carregado com sucesso.")

# Processar os dados JSON.
for record in data:
    try:
        logging.info(f"Processando registro: {record}")
        if record.get('age') is None:
            raise ValueError(f"Dado inválido: {record}")
    except ValueError as e:
        logging.warning(f"Erro no registro: {e}")
