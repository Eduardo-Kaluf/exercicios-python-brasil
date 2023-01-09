while 1:
    nomes = []
    saltos = []
    nome = input("Insira o nome: ")
    if nome == "":
        break
    x = 0
    nomes.append(nome)
    saltos.append(nome)
    saltos[x] = []
    salto_1 = input("Insira o primeiro salto: ")
    salto_2 = input("Insira o segundo salto: ")
    salto_3 = input("Insira o terceiro salto: ")
    salto_4 = input("Insira o quarto salto: ")
    salto_5 = input("Insira o quinto salto: ")
    saltos[x].append(salto_1)
    saltos[x].append(salto_2)
    saltos[x].append(salto_3)
    saltos[x].append(salto_4)
    saltos[x].append(salto_5)
    print(f"Nome: {nomes[x]}")
    print(f"Primeiro salto: {saltos[x][0]}")
    print(f"Segundo salto: {saltos[x][1]}")
    print(f"Terceiro salto: {saltos[x][2]}")
    print(f"Quarto salto: {saltos[x][3]}")
    print(f"Quinto salto: {saltos[x][4]}")

"""
atletas = ["1"]
saltos = {}
x = 1
primeiro = "primeiro_salto: "
segundo = "segundo_salto: "
terceiro = "terceiro_salto: "
quarto = "quarto_salto: "
quinto = "quinto_salto: "

while 1:
    atleta = input("Insira o nome do atleta: ")
    saltos[x] = {}
    if atleta == None:
        break
    atletas.append(atleta)
    salto_1 = input("Insira o primeiro salto: ")
    salto_2 = input("Insira o segundo salto: ")
    salto_3 = input("Insira o terceiro salto: ")
    salto_4 = input("Insira o quarto salto: ")
    salto_5 = input("Insira o quinto salto: ")
    saltos[x]['salto_1'] = (int(salto_1))
    saltos[x]['salto_2'] = (salto_2)
    saltos[x]['salto_3'] = (salto_3)
    saltos[x]['salto_4'] = (salto_4)
    saltos[x]['salto_5'] = (salto_5)
    print(f"Atleta: {atleta[x]}")
    print((primeiro) + str({saltos[x]["salto_1"]}))
    print((segundo) + str({saltos[x]["salto_2"]}))
    print((terceiro) + str({saltos[x]["salto_3"]}))
    print((quarto) + str({saltos[x]["salto_4"]}))
    print((quinto) + str({saltos[x]["salto_5"]}))
    x = x + 1
"""
