"""Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor"""


class Bola:
    def __init__(self, cor, circunferencia, material) -> None:
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def troca_cor(self, cor):
        self.cor = cor

    def mostra_cor(self):
        print(self.cor)


bola = Bola("vermelha", 10, "borracha")
bola.mostra_cor()
bola.troca_cor("rosa")
bola.mostra_cor()
