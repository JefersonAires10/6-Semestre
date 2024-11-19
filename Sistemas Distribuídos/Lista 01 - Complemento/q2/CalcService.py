class CalcService:
    @staticmethod
    def process(op, num1, num2):
        try:
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
        except Exception:
            return "Erro ao realizar operação matemática"