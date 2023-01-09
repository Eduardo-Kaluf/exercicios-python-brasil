número_primo = int(input("insira um número: "))
x = 2

while x < número_primo:
    determinação = número_primo % x
    x = x + 1
    if determinação == 0:
        print("Não é primo!")
        exit()


print("É primo!")
