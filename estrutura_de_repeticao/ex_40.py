dic = {

}
x = 0
keys = []
veiculos_list = []
acidentes_list = []
while x < 5:
    codigo_da_cidade = input("Insira o código da cidade: ")
    veiculos = input("Insira o número de veículos: ")
    acidentes = input("Insira o número de acidentes: ")
    dic[codigo_da_cidade] = {"veiculos": (veiculos), "acidentes": (acidentes)}
    x = x + 1

for key in dic:
    keys.append(key)
x = 0
while x < 5:
    veiculos_list.append((int(dic[keys[x]]["veiculos"])))
    acidentes_list.append((dic[keys[x]]["acidentes"]))
    x = x + 1

maximo = max(acidentes_list)
minimo = min(acidentes_list)

local_max = acidentes_list.index(maximo)
local_min = acidentes_list.index(minimo)

print(f"Maior índice de acidentes: {keys[local_max], maximo}")
print(f"Menor índice de acidentes: {keys[local_min], minimo}")

media = sum(veiculos_list) / len(veiculos_list)

print(f"Media de veículos: {media}")

menor_2000 = [int(i) for i in acidentes_list if int(i) < 2000]

media_2000 = sum(menor_2000) / len(menor_2000)

print(f"Média de acidentes em cidades com menmos de 2000 veículos: {media_2000}")
