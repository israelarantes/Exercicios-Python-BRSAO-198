pares = 0
impares = 0

quantidade = int(input("Quantos números você deseja analisar? "))

for i in range(quantidade):
    numero = int(input(f"Digite o número {i + 1}: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"\nTotal de números pares: {pares}")
print(f"Total de números ímpares: {impares}")