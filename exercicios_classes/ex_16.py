"""Crie uma "porta escondida" no programa do programa do bichinho virtual que mostre os valores exatos dos atributos do objeto. 
Consiga isto mostrando o objeto quando uma opção secreta, não listada no menu, for informada na escolha do usuário. """


class Tamagushi:
    def __init__(self, nome, fome, saude, idade) -> None:
        self.nome = nome
        self.fome = fome 
        self.saude = saude
        self.idade = idade
        self.tedio = 30

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

    def __str__(self):
        return (f"Nome: {self.nome}, Fome: {self.fome}, Saúde: {self.saude}, Idade: {self.idade}")

bichinho = Tamagushi("Jonas", 100, 100, 4)
print(bichinho)
