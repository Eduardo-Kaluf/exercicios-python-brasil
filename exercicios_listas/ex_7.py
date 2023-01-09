vetor = [1, 2, 3, 4, 5]
soma = sum(vetor)
x = 0
mult = 1
while x < len(vetor):
    mult = mult * vetor[x]
    x = x + 1


print(soma, vetor, mult)
