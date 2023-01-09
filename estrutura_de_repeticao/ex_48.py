numeros = []

numero_inteiro = input("Insira um número: ")
for i in numero_inteiro:
    numeros.append(i)

numeros.reverse()

numeros = "".join(numeros)

print(numeros)
