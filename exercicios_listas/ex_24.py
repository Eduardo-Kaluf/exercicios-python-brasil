from random import randint
x = 0
numeros = []
while x < 100:
    dado = randint(1, 6)
    numeros.append(dado)
    x = x + 1

um = numeros.count(1)
dois = numeros.count(2)
tres = numeros.count(3)
quatro = numeros.count(4)
cinco = numeros.count(5)
seis = numeros.count(6)
print(f"A quantia de números foi respectivamente: {um} {dois} {tres} {quatro} {cinco} {seis}")
