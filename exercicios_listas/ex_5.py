x = 0
par = []
impar = []
while x < 20:
    numero = int(input("Insira números inteiros: "))
    if numero % 2 == 0:
        par.append(numero)
        x = x + 1
    else:
        impar.append(numero)
        x = x + 1

print(par)

print(impar)
