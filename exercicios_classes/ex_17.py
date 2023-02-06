"""Crie uma Fazenda de Bichinhos instanciando vários objetos bichinho e mantendo o controle deles através de uma lista. 
Imite o funcionamento do programa básico, mas ao invés de exigir que o usuário tome conta de um único bichinho, exija que ele tome conta da fazenda inteira. 
Cada opção do menu deveria permitir que o usuário executasse uma ação para todos os bichinhos 
(alimentar todos os bichinhos, brincar com todos os bichinhos). 
Para tornar o programa mais interessante, dê para cada bichinho um nivel inicial aleatório de fome e tédio.
"""


from ex_16 import Tamagushi


class Fazenda:
    def __init__(self) -> None:
        self.bichinho = []

    def adicionar_bichinho(self, bicho):
        self.bichinho.append(bicho)

    def alimentar_fazenda(self, comida):
        for bicho in self.bichinho:
            bicho.fome += comida
    
    def brincar_fazenda(self, tempo):
        for bicho in self.bichinho:
            bicho.tedio -= tempo

    def __iter__(self) -> str:
        informacoes = []
        for bicho in self.bichinho:
            informacoes.append(f"Nome: {bicho.nome}, Fome: {bicho.fome}, Saúde: {bicho.saude}, Idade: {bicho.idade}, Tédio: {bicho.tedio}")
        return (bichinho for bichinho in informacoes)

bichinho = Tamagushi("Jonas", 20, 100, 4)
bichinho2 = Tamagushi("Joanete", 30, 100, 6)
fazenda = Fazenda()

fazenda.adicionar_bichinho(bichinho)
fazenda.adicionar_bichinho(bichinho2)
for bichinho in fazenda:
    print(bichinho)
fazenda.alimentar_fazenda(10)
for bichinho in fazenda:
    print(bichinho)
fazenda.brincar_fazenda(20)
for bichinho in fazenda:
    print(bichinho)
