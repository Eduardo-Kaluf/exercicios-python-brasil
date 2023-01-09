numeros = []

while 1:
    numero = (input("Digite um número (ou PARAR): "))
    if numero.upper() == "PARAR":
        break
    elif int(numero) not in range(0, 1000):
        print("Número inválido")
        continue
    numeros.append(float(numero))

soma = sum(numeros)
minimo = min(numeros)
maximo = max(numeros)


resultado = f"A soma é {soma} o menor numero é {minimo} e o maior numero é {maximo}"

print(resultado)