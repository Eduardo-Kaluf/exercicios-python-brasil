while 1:
    nota = int(input("Nota entre 0 e 10: "))
    if nota < 1 or nota > 9:
        print("Erro")
        continue
    else:
        print("Válido")
