"""Classe Bichinho Virtual++: Melhore o programa do bichinho virtual, 
permitindo que o usuário especifique quanto de comida ele fornece ao bichinho e por quanto tempo ele brinca com o bichinho. 
Faça com que estes valores afetem quão rapidamente os níveis de fome e tédio caem."""


class Tamagushi:
    def __init__(self, nome, fome, saude, idade) -> None:
        self.nome = nome
        self.fome = fome 
        self.saude = saude
        self.idade = idade
        self.tedio = 0

    def set_nome(self, nome):
        self.nome = nome

    def set_fome(self, fome):
        self.fome = fome

    def set_saude(self, saude):
        self.saude = saude

    def set_idade(self, idade):
        self.idade = idade

    def get_nome(self):
        return self.nome

    def get_fome(self):
        return self.fome

    def get_saude(self):
        return self.saude

    def get_idade(self):
        return self.idade

    def humor(self):
        return self.saude + self.fome

    def alimenta(self, quantidade):
        self.fome += quantidade

    def brinca(self, tempo):
        self.tedio -= tempo
