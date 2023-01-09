numero_avaliado = int(input("Insira seu número: "))

def filtro(x):
    if x <= 0:
        Res = "N"
    else:
        Res = "P"
    return Res

teste = filtro(numero_avaliado)

print(teste)
