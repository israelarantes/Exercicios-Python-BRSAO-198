def contem_numero(senha):
    for caractere in senha:
        if caractere.isdigit():
            return True
    return False


senha = input("Digite sua senha: ")


if len(senha) >= 8 and contem_numero(senha):
    print(" Senha válida!")
else:
    print(" Senha inválida. Ela deve ter pelo menos 8 caracteres e conter pelo menos um número.")