idades = [i for i in range(1, 31)]
alturas = [i for i in range(150, 181)]
media = sum(alturas) / len(alturas)
validaçao_idade = []
validaçao_altura = []
abaixo_da_media = []
x = 0

while x < len(idades):
    if idades[x] > 13:
        validaçao_idade.append(idades[x])
        validaçao_altura.append(alturas[x])
    x = x + 1
x = 0
while x < len(validaçao_idade):
    if alturas[x] < media:
        abaixo_da_media.append(alturas)
    x = x + 1

resultado = f"A quantia de alunos com mais de 13 anos e média de altura inferior da sala é: {len(abaixo_da_media)}"

print(resultado)
