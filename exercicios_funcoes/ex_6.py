while 1:
    horario = int(input("Insira dois valores inteiros: "))
    if horario > 23 or horario < 0:
        print("Erro")
        continue
    def conversão(x):
        if x >= 12 and x <= 23:
            parametro = "P"
        else:
            parametro = "A"

        if x >= 13 and x <= 23:
            x = x - 12
        elif x == 00:
            x = 12

        return x, parametro

    horario_alterado = conversão(horario)

    print(horario_alterado)
