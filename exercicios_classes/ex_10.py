"""Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:

Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
tipoCombustivel.
valorLitro
quantidadeCombustivel
Possua no mínimo esses métodos:
abastecerPorValor( ) - método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
abastecerPorLitro( ) - método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
alterarValor( ) - altera o valor do litro do combustível.
alterarCombustivel( ) - altera o tipo do combustível.
alterarQuantidadeCombustivel( ) - altera a quantidade de combustível restante na bomba.
OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba."""


class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade) -> None:
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade = quantidade

    def valida_abastecimento(self, litros_abastecidos, flag):
        if self.quantidade > litros_abastecidos:
            self.quantidade -= litros_abastecidos
            return (f"{litros_abastecidos} {flag}")
        else:
            return ("Sem combustivel o suficiente para abastecer")


    def abastecer_por_valor(self, valor):
        litros_abastecidos = valor / self.valor_litro
        return self.valida_abastecimento(litros_abastecidos, "litros")

    def abastecer_por_litro(self, litros):
        litros_abastecidos = litros * self.valor_litro 
        return self.valida_abastecimento(litros_abastecidos, "reais")

    def alterar_combustivel(self, tipo_combustivel, valor_litro):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro

    def alterar_quantidade_combustivel(self, quantidade):
        self.quantidade = quantidade

bomba = BombaCombustivel("gasolina", 5.00, 100)

print(bomba.abastecer_por_litro(10))
print(bomba.abastecer_por_valor(100))
print(bomba.quantidade)
print(bomba.abastecer_por_litro(1000))
