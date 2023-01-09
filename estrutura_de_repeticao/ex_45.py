dic = {"1": "A",
    "2": "B",
    "3": "C",
    "4": "D",
    "5": "E",
    "6": "E",
    "7": "D",
    "8": "C",
    "9" : "B",
    "10": "A"
}
pontos = 0
pontos_lista = []
x = 0
print("Aluno 1:")
while 1:
    resposta = input("Insira sua resposta" + " de número " + (str(x + 1)) + ": ").upper()
    if resposta == "PARAR":
        break
    elif resposta == dic[str(x + 1)]:
        pontos = pontos + 1
    x = x + 1
    if x == 10:
        print("Próximo aluno: ")
        pontos_lista.append(pontos)
        pontos = 0
        x = 0
        continue

print(max(pontos_lista))
print(min(pontos_lista))
print(len(pontos_lista))
print(sum(pontos_lista) / len(pontos_lista))
