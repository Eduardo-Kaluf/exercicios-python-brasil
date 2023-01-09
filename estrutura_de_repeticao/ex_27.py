x = 0
turmas = int(input("Insira a quantia de turmas: "))
alunos = []

while x < turmas:
    aluno = int(input("Quantos alunos nesta turma? "))
    alunos.append(aluno)
    x = x + 1

soma = sum(alunos)
media = soma / turmas
print(media)
