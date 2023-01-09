x = 0
temperaturas = []
while 1:
    temperatura = (input("Insira as suas temperaturas aqui: "))
    if temperatura == "parar":
        break
    temperaturas.append(float(temperatura))

soma, minima, maxima = sum(temperaturas), min(temperaturas), max(temperaturas)
media = soma / len(temperaturas)

resultado = f"A minima foi de {minima}, a maxima de {maxima} e a média das temperaturas foi de {media}"

print(resultado)
