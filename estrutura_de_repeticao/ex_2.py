while 1:
    nome = input("Nome de usuário: ")
    senha = input("Senha: ")
    if nome == senha:
        print("Nome de usuário não pode ser igual a senha")
        continue
else:
    print("Usuário e senha válidos")
