from random import randint

x = input("Deseja jogar? ").upper()

if x != "SIM":
    print("Ok!")
    exit()

def dados(x):
    if x == "RODAR":
        dado_1 = randint(1, 6)
        dado_2 = randint(1, 6)
        return (dado_1 + dado_2)

rolagem = input("Rode os dados! ").upper()

resultado = dados(rolagem)

print(resultado)

if resultado == 7 or resultado == 11:
    print("Ganhou! ")
    exit()
elif resultado == 2 or resultado == 3 or resultado == 12:
    print("Perdeu! ")
    exit()
elif resultado in range(4, 11):
    resultado_2 = dados(rolagem)
    print(resultado_2)
    if resultado_2 == 7:
        print("Perdeu! ")
        exit()
    while resultado != resultado_2:
        resultado_2 = dados(rolagem)
        print(resultado_2)
        if resultado == resultado_2:
            print("Ganhou! ")
            exit()
        elif resultado_2 == 7:
            print("Perdeu! ")
            exit
