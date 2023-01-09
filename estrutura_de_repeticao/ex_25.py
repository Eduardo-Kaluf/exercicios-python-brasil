x = 1
idades = []
quantidade_de_pessoas = int(input("Qual a quantidade de pessoas? "))

while 1:
    idade = int(input("Qual a sua idade? "))
    idades.append(idade)
    if x == quantidade_de_pessoas:
        break
    x = x + 1

soma = sum(idades)

media = soma / quantidade_de_pessoas

if media in range(0, 25):
    print("Jovens!")
elif media in range(26, 60):
    print("Adultos!")
else:
    print("Idosos")
