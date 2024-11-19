class BinaryService:
    @staticmethod
    def convert_to_binary(num):
        try:
            return bin(int(num))[2:]
        except ValueError:
            return "Erro: Entrada inválida para conversão"
