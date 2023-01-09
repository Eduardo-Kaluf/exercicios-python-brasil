cardapio = {
    "Cachorro Quente":  {
        "100": "1.20"
    },
    "Bauru Simples": {
        "101": "1.30"
    },
    "Bauru com ovo": {
        "102": "1.50"
    },
    "Hambúrguer": {
        "103": "1.20"
    },     
    "Cheeseburguer": {
        "104": "1.30"
    },
    "Refrigerante": {
        "105": "1.00"
    }
}

def codigo():
    for i in x:
        return(str(i))

total = []
preços = []
preço = 0

while 1:
    pedidos = input("Qual seu pedido? ").title()
    if pedidos == "Encerrar":
        break
    quantia = int(input("Quantos? "))
    x = cardapio.get(pedidos)
    y = codigo()
    y = cardapio[pedidos][str(y)]
    preço = preço + (float(y) * quantia)
    total.append(preço)
    preços.append(str(pedidos) + ": R$" + str(preço))
    preço = 0

print(preços)
print(sum(total))
