
A = int(input("Habitantes da primeira: "))
B = int(input("Habitantes da segunda: "))
taxa_A = float(input("Taxa de crescimento de A: "))
taxa_B = float(input("Taxa de crescimento de B: "))
anos = 0

while A <= B:
    A = A * taxa_A
    B = B * taxa_B
    anos = anos + 1

print(anos)
