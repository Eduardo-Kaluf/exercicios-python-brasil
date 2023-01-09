preço_unidade = 1.99
numero = range(1, 51)
itens = int(input("Quantos itens? "))
x = 0
while x < itens:
    if itens > 50:
        print("ERRO")
        itens = int(input("Quantos itens? "))
        continue
    elif x == 0:
        print("Lojas Quase Dois - Tabela de preços")
    preço = preço_unidade * x
    x = x + 1
    print(str(numero[x - 1]) + ' - ' + "R$" + str(preço))
    


