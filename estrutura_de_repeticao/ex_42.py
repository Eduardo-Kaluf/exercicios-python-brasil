lista = []

while 1:
    numero = int(input("Insira um número: "))
    if numero < 0:
        break
    lista.append(numero)

range_1 = [i for i in lista if i in range(0, 26)]
range_2 = [i for i in lista if i in range(26, 51)]
range_3 = [i for i in lista if i in range(51, 76)]
range_4 = [i for i in lista if i in range(76, 100)]

print(len(range_1))
print(len(range_2))
print(len(range_3))
print(len(range_4))
