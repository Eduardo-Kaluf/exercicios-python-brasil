número_de_repetições = int(input("Insira o número de repetições: "))
x = 0
numeros = []
anterior = 0 + 1
atual = 0

while x < número_de_repetições:
    resultado = anterior + atual
    anterior = atual
    atual = resultado
    numeros.append(resultado)
    x = x + 1

print(numeros)