nome = input("Insira seu nome: ").upper()

x = len(nome)

for i in nome:
    print(nome[0:x])
    x = x - 1
