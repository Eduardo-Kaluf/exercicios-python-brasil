fatorial = int(input("Insira o número da fatorial: "))
x = 1
resultado = fatorial
lista_de_resultado = []

while x < fatorial:
    resultado = resultado * (fatorial - x)    
    x = x + 1

print(resultado)
