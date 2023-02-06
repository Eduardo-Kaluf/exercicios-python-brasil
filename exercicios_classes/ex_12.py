"""Classe Conta de Investimento: Faça uma classe contaInvestimento que seja semelhante a classe contaBancaria, com a diferença de que se adicione um atributo taxaJuros. 
Forneça um construtor que configure tanto o saldo inicial como a taxa de juros. Forneça um método adicioneJuros (sem parâmetro explícito) que adicione juros à conta. 
Escreva um programa que construa uma poupança com um saldo inicial de R$1000,00 e uma taxa de juros de 10%. 
Depois aplique o método adicioneJuros() cinco vezes e imprime o saldo resultante."""


class ContaInvestimento:
    def __init__(self, numero: int, titular: str, juros, saldo: float = 0) -> None:
        self.numero = numero
        self.titular = titular
        self.juros = juros
        self.saldo = saldo

    def alterar_nome(self, nome: str) -> None:
        self.titular = nome

    def deposito(self, dinheiro: float) -> None:
        self.saldo += dinheiro

    def saque(self, dinheiro: float) -> None:
        self.saldo -= dinheiro

    def adiciona_juros(self):
        self.saldo += (self.saldo / 100) * self.juros


conta_investimento = ContaInvestimento(1234567, "Jonas", 10, 1000)
print(conta_investimento.adiciona_juros())
print(conta_investimento.adiciona_juros())
print(conta_investimento.adiciona_juros())
print(conta_investimento.adiciona_juros())
print(conta_investimento.adiciona_juros())

print(conta_investimento.saldo)
