n = float(input("Insira n: "))
numeros = []
numeros_decimal = []
cima = 0
baixo = 0
while cima != n:
    cima = cima + 1
    if cima == 1:
        baixo = 1
        numeros.append(f"{cima}" + "/" + f"{baixo}")
        numeros_decimal.append(cima / baixo)
    elif cima != 1:
        baixo = baixo + 2
        numeros.append(f"{cima}" + "/" + f"{baixo}")
        numeros_decimal.append(cima / baixo)

soma = sum(numeros_decimal)

numeros = " + ".join(numeros)

print(f"S = {numeros}")
print(soma)
