import os

base = os.getcwd()

arquivo = open(os.path.join(f"{base}", "Aulas_de_Python", "arquivos", "ips_2.txt"), "r")

conteudo = arquivo.readlines()

arquivo.close()

ips = []
invalidos = []

for i in conteudo:
    i = i.strip()
    i = i.split(".")
    z = [x for x in i if int(x) < 256]
    if len(z) == 4:
        z = ".".join(z)
        ips.append("\n" + z)
    else:
        i = ".".join(i)
        invalidos.append("\n" + i)

saida = open(os.path.join(f"{base}", "Aulas_de_Python", "arquivos", "ips_relatório.txt"), "w", encoding="utf-8")

saida.write("[Endereços válidos: ]")

for i in ips:
    saida.write(i)

saida.write("\n\n[Endereços inválidos: ]")

for i in invalidos:
    saida.write(i)
