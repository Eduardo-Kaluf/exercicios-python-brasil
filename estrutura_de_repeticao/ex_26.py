total_de_eleitores = int(input("Número total de eleitores: "))
x = 0
votos = []
possibilidades = list(range(1, 1000))
lista = [str(i) for i in possibilidades]

while x < total_de_eleitores:
    voto = input("Eleitor" + ' ' + lista[x] + ' ')
    if voto == '1' or voto == '2' or voto == '3':
        votos.append(voto)
    x = x + 1

candidato_1 = votos.count("1")
candidato_2 = votos.count("2")
candidato_3 = votos.count("3")

print(candidato_1)
print(candidato_2)
print(candidato_3)
