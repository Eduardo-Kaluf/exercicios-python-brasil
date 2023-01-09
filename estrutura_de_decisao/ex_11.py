Salário = float(input("Insira seu salário: "))

if Salário <= 280:
  Ajuste = 1.20
elif Salário > 280 and Salário <= 700:
  Ajuste = 1.15
elif Salário > 700 and Salário <= 1500:
  Ajuste = 1.10
else:
  Ajuste = 1.05

Aumento = ((Salário * Ajuste) - Salário)

Novo_salário = (Salário * Ajuste)

Resultado = f"Seu salário era {Salário}, O ajuste foi de {Ajuste}, o aumento igual à {Aumento} e o seu novo salário é igual à {Novo_salário}"

print(Resultado)




