"""Aprimore a classe do exercício anterior para adicionar o método aumentarSalario 
(porcentualDeAumento) que aumente o salário do funcionário em uma certa porcentagem."""


class Funcionario:
    def __init__(self, nome: str, salario: float) -> None:
        self.nome = nome
        self.salario = salario

    def get_nome(self):
        return self.nome

    def get_salario(self):
        return self.salario

    def aumenta_salario(self, percentual):
        self.salario += (self.salario / 100) * percentual

func = Funcionario("Jonas", 1000)

print(func.get_nome())
print(func.get_salario())
func.aumenta_salario(10)
print(func.get_salario())
