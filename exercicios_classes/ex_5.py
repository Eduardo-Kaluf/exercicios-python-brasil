"""Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. 
A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. 
Os métodos são os seguintes: alterarNome, depósito e saque; 
No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios."""


class ContaCorrente:
    def __init__(self, numero: int, titular: str, saldo: float = 0) -> None:
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def alterar_nome(self, nome: str) -> None:
        self.titular = nome

    def deposito(self, dinheiro: float) -> None:
        self.saldo += dinheiro

    def saque(self, dinheiro: float) -> None:
        self.saldo -= dinheiro

conta_corrente = ContaCorrente(1234567, "Jonas")
conta_corrente.deposito(1000)
conta_corrente.saque(200)
print(conta_corrente.saldo)
