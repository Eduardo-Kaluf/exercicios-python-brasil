divida = float(input("Insira a divida: "))
x = 0
valor_divida = []
valor_juros = []
quantia_parcelas = []
valores_parcelas = []
parcela = 1

while x < 5:
    if parcela == 1:
        juros = 0
        valor_parcela = divida
        quantia_parcelas.append(parcela)
        valor_juros.append(juros)
        valores_parcelas.append(valor_parcela)
        valor_divida.append(divida)
        parcela = parcela + 2
        x = x + 1
    elif parcela == 3:
        juros = 1.10
        valor_parcela = (divida * juros) / parcela
        quantia_parcelas.append(parcela)
        valor_juros.append(juros)
        valores_parcelas.append(valor_parcela)
        valor_divida.append(divida * juros)
        parcela = parcela + 3
        x = x + 1
    elif parcela == 6:
        juros = 1.15
        valor_parcela = (divida * juros) / parcela
        quantia_parcelas.append(parcela)
        valor_juros.append(juros)
        valores_parcelas.append(valor_parcela)
        valor_divida.append(divida * juros)
        parcela = parcela + 3
        x = x + 1
    elif parcela == 9:
        juros = 1.20
        valor_parcela = (divida * juros) / parcela
        quantia_parcelas.append(parcela)
        valor_juros.append(juros)
        valores_parcelas.append(valor_parcela)
        valor_divida.append(divida * juros)
        parcela = parcela + 3
        x = x + 1
    else:
        juros = 1.25
        valor_parcela = (divida * juros) / parcela
        quantia_parcelas.append(parcela)
        valor_juros.append(juros)
        valores_parcelas.append(valor_parcela)
        valor_divida.append(divida * juros)
        x = x + 1

print(valor_divida)
print(valor_juros) 
print(quantia_parcelas)
print(valores_parcelas)
