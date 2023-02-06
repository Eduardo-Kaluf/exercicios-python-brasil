"""Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;"""


class Quadrado:
    def __init__(self, lado) -> None:
        self.lado = lado

    def mudar_lado(self, lado):
        self.lado = lado

    def retorna_lado(self):
        return self.lado

    def area(self):
        area = self.lado * self.lado
        return area


quadrado = Quadrado(10)
lado = quadrado.retorna_lado()
print(lado)
quadrado.mudar_lado(20)
lado = quadrado.retorna_lado()
print(lado)
area = quadrado.area()
print(area)
