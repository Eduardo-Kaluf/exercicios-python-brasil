def valor_pagamento(x, y):
    multa = x * 1.03
    z = 1
    while z < y:
        juros = multa * ((1 + 0.001)**y)
        z += 1
    return juros

while 1:
    valor = float(input("Insira o valor da prestação: "))
    if valor == 0:
        break
    dias = int(input("Dias de atraso: "))
    total = valor_pagamento(valor, dias)
    print(total)
