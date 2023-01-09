numero = int(input("Insira seu número: "))

def piramede(x, numero):
    numeros = []
    x = 1
    while x < numero:
        numeros.append(x)
        print(numeros)
        x += 1

piramede(None, numero + 1)
