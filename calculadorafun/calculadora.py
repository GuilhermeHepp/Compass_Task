class Calculadora:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def somar(self):
        return self.num1 + self.num2
    
    def subtrair(self):
        return self.num1 - self.num2
    
    def multiplicar(self):
        return self.num1 * self.num2
    
    def dividir(self):
        if self.num2 == 0:
            raise ValueError("Erro: Divisão por zero")
        return self.num1 / self.num2
    
    def potencia(self):
        return self.num1 ** self.num2

    def raiz_quadrada(self):
        if self.num1 < 0 or self.num2 < 0:
            raise ValueError("Erro: Raiz quadrada de número negativo")
        return (self.num1 ** 0.5, self.num2 ** 0.5)