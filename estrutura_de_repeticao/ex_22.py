número_primo = int(input("insira um número: "))
x = 2
divisores = []
while x < número_primo:
    determinação = número_primo % x
    if determinação == 0:
        divisores.append(x)
    x = x + 1

if len(divisores) > 0:
    print(f"Não é primo, e seus divisores são {divisores}")
else:
    print("É primo!")
