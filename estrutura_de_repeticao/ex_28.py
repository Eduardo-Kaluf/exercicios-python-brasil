quantia = int(input("Insira a quantidade de CDs desejados: "))

x = 0
CDs = []
while x < quantia:
    pergunta = int(input("Qual o valor do cd de número " + str(x) + ' '))
    CDs.append(pergunta)
    x = x + 1

soma = sum(CDs)
média = soma / quantia

resultado = f"O total gasto foi de {soma} e a média por CD foi de {média}"

print(resultado)
