vetor_1 = [i for i in range(1, 11)]

vetor_2 = [i for i in range(11, 21)]

vetor_3 = []

x = 0

while x < 10:
    vetor_3.append(vetor_1[x])
    vetor_3.append(vetor_2[x])
    x = x + 1

print(vetor_3)
