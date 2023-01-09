fatorial = int(input("Insira o número desejado: "))
x = 1
base = fatorial
while x < base:
    fatorial = fatorial * (base - x)
    x = x + 1

print(fatorial)
