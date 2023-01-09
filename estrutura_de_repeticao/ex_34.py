x = 2
número = int(input("Insira um número inteiro: "))

while x < número:
    verificação = número % x
    if verificação == 0:
        print("Não é primo! ")
        exit()
    x = x + 1

print("É primo! ")
