numeros = []

while 1:
    numero = int(input("Insira um número: "))
    if numero == -1:
        break
    numeros.append(numero)

print(len(numeros))
print(numeros)
c = numeros
c.reverse()
print(c)
d = [print(i) for i in numeros]
e = sum(numeros)
print(e)
f = e / len(numeros)
print(f)
acima_media = [i for i in numeros if i > f]
print(len(acima_media))
abaixo_sete = [i for i in numeros if i < 7]
print(len(abaixo_sete))

print("Final do programa")
