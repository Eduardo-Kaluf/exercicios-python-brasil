"""Classe TV: Faça um programa que simule um televisor criando-o como um objeto. 
O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. 
Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas."""

#  canais de 1 a 20
#  volume de 0 a 100

ULTIMO_CANAL = 20
PRIMEIRO_CANAL = 1


class Tv:
    def __init__(self, canal: int, volume: int = 0) -> None:
        self.canal = canal
        self.volume = volume

    def selecionar_canal(self, canal):
        self.canal = canal

    def proximo_canal(self):
        self.canal += 1
        if self.canal > ULTIMO_CANAL:
            self.canal = PRIMEIRO_CANAL

    def canal_anterior(self):
        self.canal -= 1
        if self.canal < PRIMEIRO_CANAL:
            self.canal = ULTIMO_CANAL

    def aumenta_volume(self):
        if self.volume != 100:
            self.volume += 1

    def abaixa_volume(self):
        if self.volume != 0:
            self.volume -= 1

    def seleciona_volume(self, volume):
        self.volume = volume

tv = Tv(12)
tv.proximo_canal()
print(tv.canal)
tv.canal_anterior()
print(tv.canal)
tv.selecionar_canal(1)
tv.canal_anterior()
print(tv.canal)
tv.proximo_canal()
print(tv.canal)
tv.seleciona_volume(100)
tv.aumenta_volume()
print(tv.volume)
