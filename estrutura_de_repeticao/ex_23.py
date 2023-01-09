n = int(input("Até qual deseja calcular? "))
x = 2
n = range(2, n + 1)

primos = []

for y in n:
    x = 2
    determinaçoes = []
    while x <= y:
        if x != y:
            determinaçao = y % x
            determinaçoes.append(determinaçao)
            divisao = x - 2 + 1
        x = x + 1
    if 0 not in determinaçoes:
        primos.append(y)

print(primos)

print(divisao)
