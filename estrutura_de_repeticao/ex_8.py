x = 0
perguntas = ["Número 1: ", "Número 2: ", "Número 3: ", "Número 4: ", "Número 5: " ]
respostas = []

while x < len(perguntas):
  p = int(input(perguntas[x]))
  respostas.append(p)
  x = x + 1

soma = sum(respostas)
média = soma / x

print(soma, média)
