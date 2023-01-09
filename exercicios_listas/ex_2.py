lista = []

while len(lista) < 10:
    numero = int(input("Insira um número: "))
    lista.append(numero)

lista.reverse()

print(lista)
