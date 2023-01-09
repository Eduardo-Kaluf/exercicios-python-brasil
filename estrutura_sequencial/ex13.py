h = float(input("Insira a sua altura: "))

Sexo = input("Você é homem ou mulher? ")

Peso_H = ((72.7 * h) - 58)

Peso_M = ((61.1 * h) - 44.7)



if Sexo == "mulher":
    print(Peso_M)
else:
    print(Peso_H)
