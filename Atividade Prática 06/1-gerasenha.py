import random
import string

def gerar_senha(tamanho: int) -> str:
    
    if tamanho < 8:
        return "A senha deve ter pelo menos 8 caracteres."
    
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

print("=== Gerador de Senhas Seguras ===")
tamanho = int(input("Digite o tamanho desejado da senha: "))

senha_gerada = gerar_senha(tamanho)
print(f"\nSenha gerada: {senha_gerada}")