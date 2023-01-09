def fat(x, fatorial, resultado):
    while x < fatorial:
        resultado = resultado * (fatorial - x) 
        x = x + 1
        if x > fatorial:
            break
        else:
            continue
    return resultado


while 1:
    fatorial = int(input("Insira o número da fatorial: "))
    if fatorial > 16 or fatorial < 0:
        print("Número não possível")
        continue
    x = 1
    resultado = fatorial
    calculo = fat(x, fatorial, resultado)
    print(calculo)
