x = 0
medias = []
while x < 3:
    nota_1 = float(input("Insira sua 1 nota: "))
    nota_2 = float(input("Insira sua 2 nota: "))
    nota_3 = float(input("Insira sua 3 nota: "))
    nota_4 = float(input("Insira sua 4 nota: "))
    media = (nota_1 + nota_2 + nota_3 + nota_4) / 4
    medias.append(media)
    x = x + 1

passou = [m for m in medias if m > 7]

print(passou)
