x = int(input("Primerio número: "))
y = int(input("Segundo número: "))

numeros_entre = [i for i in range(x + 1, y)]
soma = sum(numeros_entre)

print(numeros_entre, soma)
