y = int(input("Digite seu número: "))

def piramede(x, y):
    while x < y:
        print(str(x) * x) 
        x = x + 1

numeros = piramede(1, y + 1)

print(numeros)
