x = float(input("insira o primeiro número: "))
y = float(input("insira o segundo número: "))

operação = input("Qual operação deseja realizar? (+, -, *, /) ")

if operação == "+":
  execução = x + y
elif operação == "-":
  execução = x - y
elif operação == "*":
  execução = x * y
else:
  execução = x / y

par_impar = execução % 2

if par_impar == 0:
  par_impar = "Par"
else:
  par_impar = "Ímpar"

if execução > 0:
  positivo_negativo = "Positivo"
elif execução < 0:
  positivo_negativo = "Negativo"
else:
  positivo_negativo = "Nulo"

decimal_inteiro = round(execução)

if execução == decimal_inteiro:
  decimal_inteiro = "Inteiro"
else:
  decimal_inteiro = "Decimal"

resultado = f"Resultado = {execução} \nPar/ímpar = {par_impar} \nPositivo/negativo - {positivo_negativo} \nDecimal/inteiro = {decimal_inteiro}"

print(resultado)