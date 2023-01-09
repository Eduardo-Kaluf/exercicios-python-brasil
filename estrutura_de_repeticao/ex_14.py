x = 0

pergunta = int(input("Escreva números inteiros até chega na décima vez: "))
números = []


while x < 10:
    pergunta = int(input("Escreva números inteiros até chega na décima vez: "))
    números.append(pergunta)
    x = x + 1

par = [i for i in números if i % 2 == 0]

ímpar = [i for i in números if i % 2 != 0]

resultado = f"Números pares: {par} \n Números ímpares: {ímpar}"

print(resultado)
