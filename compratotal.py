#Este proragra, através da função input, recebe, nome do produtdo, valor e quantiade.
#Então é calculado o valor total da compra e impresso na tela

produto = str(input("Insira o nome do produto: "))
valor   = float(input("Insira o valor do produto: "))
quantidade = int(input("Insira a quantidade: "))

valor = (valor * quantidade)

print ("O valor da compra foi: R$", valor)