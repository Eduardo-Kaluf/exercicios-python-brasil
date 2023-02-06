"""Classe Ponto e Retangulo: Faça um programa completo utilizando funções e classes que:

Possua uma classe chamada Ponto, com os atributos x e y. 
Possua uma classe chamada Retangulo, com os atributos largura e altura.
Possua uma função para imprimir os valores da classe Ponto
Possua uma função para encontrar o centro de um Retângulo.
Você deve criar alguns objetos da classe Retangulo.
Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do retângulo, que deve ser um objeto da classe Ponto.
A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo ponto que indique os valores de x e y para o centro do objeto.
O valor do centro do objeto deve ser mostrado na tela
Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo."""


class Ponto:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def coordenadas(self):
        return (self.x, self.y)


class Retangulo:
    def __init__(self, largura, altura) -> None:
        self.largura = largura
        self.altura = altura

    def partida(self):
        return Ponto(0, 0)

    def centro(self):
        return Ponto(self.largura / 2, self.altura / 2)

    def set_largura(self, largura):
        self.largura = largura

    def set_altura(self, altura):
        self.altura = altura

retangulo = Retangulo(10, 20)

vertice_partida = retangulo.partida()
centro = retangulo.centro()

print(centro.coordenadas())
