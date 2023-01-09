vetor_1 = [i for i in range(1, 11)]

vetor_2 = [i for i in range(11, 21)]

vetor_3 = [i for i in range(21, 31)]

vetor_4 = []

x = 0

while x < 10:
    vetor_4.append(vetor_1[x])
    vetor_4.append(vetor_2[x])
    vetor_4.append(vetor_3[x])
    x = x + 1

print(vetor_4)
