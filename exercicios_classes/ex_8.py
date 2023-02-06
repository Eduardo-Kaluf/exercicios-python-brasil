"""Classe Macaco: Desenvolva uma classe Macaco, que possua os atributos nome e bucho (estomago) e pelo menos os métodos comer(), verBucho() e digerir(). 
Faça um programa ou teste interativamente, criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição. """


class Macaco:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.bucho = []

    def comer(self, comida):
        self.bucho.append(comida)

    def get_bucho(self):
        return(self.bucho)

    def digerir(self):
        self.bucho = []

macaco1 = Macaco("Jonas")
macaco2 = Macaco("Jaime")

macaco1.comer("Maçã")
macaco2.comer("Abacate")

print(macaco1.get_bucho())
macaco2.digerir()
print(macaco2.get_bucho())
