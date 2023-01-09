numero = int(input("Insira um número de 1 até 99: "))

if numero < 0 or numero > 99:
    print("Inválido")

dic = {0: 'zero', 1: 'um', 2: 'dois', 3: 'três', 4: 'quatro', 5: 'cinco',
    6: 'seis', 7: 'sete', 8: 'oito', 9: 'nove', 10: 'dez',
    11: 'onze', 12: 'doze', 13: 'treze', 14: 'quatorze', 15: 'quinze',
    16: 'dezesseis', 17: 'dezessete', 18: 'dezoito', 19: 'dezenove', 20: 'vinte',
    30: 'trinta', 40: 'quarenta', 50: 'cinquenta', 60: 'sessenta', 70: 'setenta',
    80: 'oitenta', 90: 'noventa'}

unidade = numero % 10
decimal = numero - unidade

if unidade != 0:
    unidade = dic[unidade]
else:
    unidade = ""
if decimal != 0:
    decimal = dic[decimal]
else:
    decimal = ""

if decimal != "" and unidade != "":
    e = " e "
else:
    e = ""

print(f"{decimal}{e}{unidade}")
