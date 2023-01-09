n = int(input("Insira um número n: "))

cima = 1
baixo = 2

numeros = []

while baixo < n + 2:
    if baixo == 2:
        numeros.append(str(cima))
        baixo = baixo + 1
    numeros.append(f"{cima}" + "/" + f"{baixo - 1}")
    baixo = baixo + 1

numeros = " + ".join(numeros)

print(f"H = {numeros}")
