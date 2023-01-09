alunos = {}

while 1:
    cod = int(input("Digite o código do aluno: "))

    if not cod:
        break

    altura = float(input("Digite a altura: "))
    peso = float(input("Digite o peso: "))

    alunos[cod] = {
        "peso": peso,
        "altura": altura
    }

alto = None
baixo = None
gordo = None
magro = None

for key, value in alunos.items():
    
    if not alto:
        alto = (key, value["altura"])
    elif alto[1] < value["altura"]:
        alto = (key, value["altura"])

    if not baixo:
        baixo = (key, value["altura"])
    elif baixo[1] > value["altura"]:
        baixo = (key, value["altura"])

    if not gordo:
        gordo = (key, value["peso"])
    elif gordo[1] < value["peso"]:
        gordo = (key, value["peso"])

    if not magro:
        magro = (key, value["peso"])
    if magro[1] > value["peso"]:
        magro = (key, value["peso"])

if alto and baixo and gordo and magro:
    print(f"O mais alto é {alto[0]}, altura: {alto[1]}")
    print(f"O mais baixo é {baixo[0]}, altura: {baixo[1]}")
    print(f"O mais gordo é {gordo[0]}, peso: {gordo[1]}")
    print(f"O mais magro é {magro[0]}, peso: {magro[1]}")
else:
    print("Não há informações de alunos para apresentar")
