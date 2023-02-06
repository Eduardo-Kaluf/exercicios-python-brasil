"""Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

Atributos: Nome, Fome, Saúde e Idade 
Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade 
Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, este humor é uma combinação entre os atributos Fome e Saúde, 
ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento."""


class Tamagushi:
    def __init__(self, nome, fome, saude, idade) -> None:
        self.nome = nome
        self.fome = fome 
        self.saude = saude
        self.idade = idade

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
