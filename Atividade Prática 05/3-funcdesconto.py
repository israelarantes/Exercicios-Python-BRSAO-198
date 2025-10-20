def calcular_desconto(valor_original: float, porcentagem_desconto: float) -> float:
    return valor_original * (porcentagem_desconto / 100)

print("=== Calculadora de Desconto ===")

nome_produto = input("Digite o nome do produto: ")
valor_original = float(input("Digite o valor original do produto (R$): "))
porcentagem_desconto = float(input("Digite a porcentagem de desconto (%): "))

valor_desconto = calcular_desconto(valor_original, porcentagem_desconto)
preco_final = valor_original - valor_desconto

print(f"\nProduto: {nome_produto}")
print(f"Valor original: R$ {valor_original:.2f}")
print(f"Desconto de {porcentagem_desconto}%: R$ {valor_desconto:.2f}")
print(f"Preço final com desconto: R$ {preco_final:.2f}")
