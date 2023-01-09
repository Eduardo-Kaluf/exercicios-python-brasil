palindromo = input("Insira um palindromo: ").upper()

palindromo = palindromo.replace(" ", "")

if palindromo == palindromo[::-1]:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")
