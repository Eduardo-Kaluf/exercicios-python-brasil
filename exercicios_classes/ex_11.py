"""Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:

Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque.
O consumo é especificado no construtor e o nível de combustível inicial é 0.
Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância, 
reduzindo o nível de combustível no tanque de gasolina.
Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
Forneça um método adicionarGasolina( ), para abastecer o tanque. Exemplo de uso:
meuFusca = Carro(15);           # 15 quilômetros por litro de combustível. 
meuFusca.adicionarGasolina(20); # abastece com 20 litros de combustível. 
meuFusca.andar(100);            # anda 100 quilômetros.
meuFusca.obterGasolina()        # Imprime o combustível que resta no ta"""


class Carro:
    def __init__(self, consumo) -> None:
        self.consumo = consumo
        self.combustivel = 0

    def andar(self, distancia):
        gasto = distancia / self.consumo
        if gasto <= self.combustivel:
            self.combustivel -= gasto
        else:
            print("Combustivel insuficiente")

    def adicionar_gasolina(self, litros):
        self.combustivel += litros

    def get_gasolina(self):
        return self.combustivel

meuFusca = Carro(15)
meuFusca.adicionar_gasolina(20)
meuFusca.andar(100) 
print(meuFusca.get_gasolina()) 