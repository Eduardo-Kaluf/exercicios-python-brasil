def porcentagem(todo, parte):
    porcentagem = (parte * 100) / todo
    porcentagem = round(porcentagem, 2)
    return(porcentagem)

def contador(x, y):
    z = x.count(y)
    return(z)

voto = None
votos = []
x = 1
y = 0
while voto != 0:
    voto = int(input("Insira um número de 1 a 23 (0 para encerrar): "))
    if voto == 0:
        break
    elif voto not in range(1, 24):
        print("Invalido")
        continue
    votos.append(voto)


soma = (len(votos))

print("Resultado da votação: \n")

print(f"Foram computados {soma} votos\n")

print("Jogador".ljust(20),"Votos".ljust(19),"%")
for i in votos:
    contagem = contador(votos, x)
    if contagem > y:
        y = contagem
        maximo = [x, contagem]
    if contagem != 0:
        print(f"{str(x).ljust(21)}{str(contagem).ljust(20)}{porcentagem(soma, contagem)} %")
    x = x + 1

print(f"\nO jogador com mais votos foi o de camisa {maximo[0]} com um total de {maximo[1]} votos e um percentual de {porcentagem(soma, maximo[1])}")
