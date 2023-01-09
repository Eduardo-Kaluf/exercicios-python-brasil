x = 0
alturas = []
idades = []

while x < 5:
    altura = float(input("Insira sua altura: "))
    idade = int(input("Insira sua idade: "))
    alturas.append(altura)
    idades.append(idade)
    x = x + 1

alturas.reverse()
idades.reverse()

print(alturas, idades)
