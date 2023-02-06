"""Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
"""

CRESCIMENTO_PADRAO = 0.05
IDADE_CRESCIMENTO = 21

class Pessoa:
    def __init__(self, nome: str, idade: int, peso: float, altura: float) -> None:
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade += 1
        if self.idade < IDADE_CRESCIMENTO:
            self.crescer(CRESCIMENTO_PADRAO)

    def engordar(self, peso):
        self.peso += peso

    def emagrecer(self, peso):
        self.peso -= peso

    def crescer(self, altura):
        self.altura += altura

pessoa = Pessoa("Jonas", 10, 47.534, 1.60)
pessoa.crescer(0.05)
print(pessoa.altura)
print(pessoa.idade)
pessoa.envelhecer()
print(pessoa.altura)
print(pessoa.idade)
