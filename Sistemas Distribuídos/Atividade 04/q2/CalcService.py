class Calculator:
    _instances = {}

    def __new__(cls):
        if cls not in cls._instances:
            cls._instances[cls] = super(Calculator, cls).__new__(cls)
        return cls._instances[cls]
    
    def calculate(self, op, num1, num2):
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