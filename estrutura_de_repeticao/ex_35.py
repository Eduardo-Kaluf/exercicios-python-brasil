numero = int(input("Digite um número: "))

lista = [i for i in range(numero + 1) if i % 2 == 1 and i != 2]

print(lista)
