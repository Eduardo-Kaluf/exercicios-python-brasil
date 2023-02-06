"""Classe Retangulo: Crie uma classe que modele um retangulo:
Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. 
Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local."""


class Retangulo:
    def __init__(self, base, altura) -> None:
        self.base = base
        self.altura = altura

    def mudar_lados(self, base, altura):
        self.base = base
        self.altura = altura

    def retorna_lados(self):
        return self.base, self.altura

    def area(self):
        area = self.base * self.altura
        return area

    def perimetro(self):
        perimetro = self.base * 2 + self.altura * 2
        return perimetro

AZULEJO = 2 # m²

terreno = Retangulo(10, 20)
area = terreno.area()
perimetro = terreno.perimetro()

pisos = area / AZULEJO
rodapes = perimetro

print(pisos, rodapes)
