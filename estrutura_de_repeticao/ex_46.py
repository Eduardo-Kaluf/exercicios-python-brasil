x = 0
saltos = []
nome = None
while x < 5:
    if nome == None:
        nome = input("Insira o nome do atleta: ")
    salto = float(input("Insira os saltos: "))
    x = x + 1
    saltos.append(salto)
    if x == 5:
        print(f"Atleta: {nome}\n")

        print(f"Primeiro Salto: {saltos[0]} m")
        print(f"Segundo Salto: {saltos[1]} m")
        print(f"Terceiro Salto: {saltos[2]} m")
        print(f"Quarto Salto: {saltos[3]} m")
        print(f"Quinto Salto: {saltos[4]} m\n")

        media = (sum(saltos) - (max(saltos) + min(saltos))) / 3
        media = round(media, 2)
        print(f"Melhor Salto: {max(saltos)} m")
        print(f"Pior Salto: {min(saltos)} m")   
        print(f"Média dos demais saltos: {media} m\n")

        print(f"Resultado final:")
        print(f"{nome}: {media} m")
        x = 0
        nome = None
