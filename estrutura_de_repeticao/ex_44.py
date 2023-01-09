lista = []
while 1:
    voto = int(input("Insira seu voto: "))
    if voto < 7 and voto > 0:
        lista.append(voto)
    elif voto < 0:
        break

candidato_1 = [i for i in lista if i == 1]
candidato_2 = [i for i in lista if i == 2]
candidato_3 = [i for i in lista if i == 3]
candidato_4 = [i for i in lista if i == 4]
nulos = [i for i in lista if i == 5]
branco = [i for i in lista if i == 6]

print(candidato_1.count(1))
print(candidato_2.count(2))
print(candidato_3.count(3))
print(candidato_4.count(4))
print(nulos.count(5))
print(branco.count(6))

porcentagem_nulos = (100 * len(nulos)) / len(lista)

porcentagem_brancos = (100 * len(branco)) / len(lista)

print(porcentagem_nulos)

print(porcentagem_brancos)
