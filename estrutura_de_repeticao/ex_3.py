"""

nome = input("Nome: maior que 3 caracteres: ")

perguntas = [
    "Idade: entre 0 e 150: ",
    "Salário: maior que zero: ",
    "Sexo: 'f' ou 'm': ",
    "Estado Civil: 's', 'c', 'v', 'd': "
]

respostas = []
x = 0

while x < len(perguntas):
    pergunta = input(perguntas[x])
    x = x + 1
    for perguntas in pergunta:
        respostas.append(pergunta)

print(respostas)

estados_válidos = ["s", "c", "v", "d"]

if len(respostas[0]) <= 3:
    print("Invalido")
elif int(respostas[7]) < 0 or int(respostas[7]) > 150:
    print("Inválido")
elif float(respostas[10]) < 0:
    print("Inválido")
elif respostas[13] != "f" or respostas[13] != "m":
    print("Inválido")
elif respostas[14] not in estados_válidos:
    print("Inválido")
else:
    print("Válido")

"""

#nome = input("Qual seu nome [minimo 4 caracteres]: ")
#idade = int(input("Sua idade: "))
#salario = float(input("Salário: "))
#sexo = input("Sexo ('f' para feminino ou 'm' para masculino): ")
#civil = input("Estado civil (s, c, v ou d): ")

estados_válidos = ["s", "c", "v", "d"]

while 1:
    nome = input("Qual seu nome [minimo 4 caracteres]: ")
    if len(nome) <= 3:
        print("Nome inválido")
    elif len(nome) > 3:
        break

while 1:
    idade = int(input("Sua idade: "))
    if idade < 0 or idade >= 150:
        print("Idade inválida")
    elif idade > 0 and idade < 150:
        break


while 1:
    salario = float(input("Salário: "))
    if salario < 0:
        print("Salário inválido")
    elif salario > 0:
        break

while 1:
    sexo = input("Sexo ('f' para feminino ou 'm' para masculino): ")
    if sexo != "f" and sexo != "m":
        print("Sexo inválido")
    elif sexo == "f" or sexo == "m":
        break

while 1:
    civil = input("Estado civil (s, c, v ou d): ")
    if civil not in estados_válidos:
        print("Estado civil inválido")
    elif civil in estados_válidos:
        break

print("Tudo correto!")
