from datetime import datetime

data_nascimento_str = input("Digite sua data de nascimento (formato: DD/MM/AAAA): ")
data_nascimento = datetime.strptime(data_nascimento_str, "%d/%m/%Y")
data_atual = datetime.now()
dias_vivo = (data_atual - data_nascimento).days

print(f"Você está vivo há {dias_vivo} dias.")