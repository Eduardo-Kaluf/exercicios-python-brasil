x = 1
preços = []
produtos = []
while 1:
    preço = input("Produto " + str(x) + ': ')
    if int(preço) == 0:
        print("Lojas Tabajara")
        [print(i) for i in produtos]
        x = 1
        produtos = []
        preços = []
        continue
    preços.append(preço)
    produtos.append(("Produto " + str(x) + ':' + 'R$' + str(preços[x - 1])))
    x = x + 1
