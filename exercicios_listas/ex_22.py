def contador(x, y):
    x = str(x.count(y)).ljust(20)
    return(x)

def percentual(x):
    convertido = (x * 100) / quantia
    convertido = round(convertido, 2)
    return(str(convertido))


situaçoes = ["necessita da esfera", "necessita de limpeza", "necessita troca do cabo ou conector", "quebrado ou inutilizado"]
identificaçoes = []
identificaçao = None
x = 0

while identificaçao != 0:
    identificaçao = int(input("Insira o numero do mouse: "))
    if identificaçao != 0:
        identificaçoes.append(identificaçao)

quantia = len(identificaçoes)

print(f"Quantidade de mouses: {quantia}\n")

print("Situação".ljust(40) + "Quantidade".ljust(25) + "Percentual\n")

for i in situaçoes:
    try:
        print(f"{x + 1} - {situaçoes[x].ljust(40)} {contador(identificaçoes, x + 1)}{percentual(int(contador(identificaçoes, x + 1)))} %")
    except:
        print(f"{x + 1} - {situaçoes[x].ljust(40)} 0".ljust(20) + "0 %")
    x = x + 1
