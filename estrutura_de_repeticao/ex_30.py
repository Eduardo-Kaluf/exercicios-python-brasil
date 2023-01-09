preço_do_pão = float(input("Insira o preço do pão: "))
x = 0
quantidade = int(input("Quantidade de pãos "))

while x < quantidade:
    if x == 0:
        print("Panificadora Pão de Ontem - Tabela de preços" + ' ' + "Preço do pão: " + str(preço_do_pão))
    valor = preço_do_pão * (x + 1)
    print(valor)
    x = x + 1
