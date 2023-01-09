data = input("Insira sua data: ")

def mes_por_extenso(x):
    y = x[0:2]
    z = x[6:]
    x = int(x[3:5])
    if x == 1:
        x = "Janeiro"
    elif x == 2:
        x = "Fevereiro"
    elif x == 3:
        x = "Março"
    elif x == 4:
        x = "Abril"
    elif x == 5:
        x = "Maio"
    elif x == 6:
        x = "Junho"
    elif x == 7:
        x = "Julho"
    elif x == 8:
        x = "Agosto"
    elif x == 9:
        x = "Setembro"
    elif x == 10:
        x = "Outubro"
    elif x == 11:
        x = "Novembro"
    else:
        x = "Dezembro"
    return y + " de " + x + " de " + z

conversão = mes_por_extenso(data)

print(conversão)
