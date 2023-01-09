perguntas = [
    "Telefonou para a vítima? ",
    "Esteve no local do crime? ",
    "Mora perto da vítima? ",
    "Devia para a vítima? ",
    "Já trabalhou com a vítima? "
]
respostas = []
x = 0
while x < 5:
    respostas.append(input(perguntas[x]).upper())
    x = x + 1

quantia = respostas.count("SIM")

if quantia == 2:
    print("Suspeita")
elif quantia > 2 and quantia < 5:
    print("Cúmplice")
elif quantia == 5:
    print("Assassino")
else:
    print("Inocente")
