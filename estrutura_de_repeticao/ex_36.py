while 1:
    numero = int(input("Tabuada de que número? "))
    começo = int(input("Começo da tabuada: "))
    final = int(input("Final da tabuada: "))
    if final < começo:
        print("Erro")
        continue
    else:
        break

tabuada = [i * numero for i in range(começo, final + 1)]



print(tabuada)
