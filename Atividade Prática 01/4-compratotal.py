#Este proragra, através da função input, recebe, nome do produto, valor e quantiade.
#Então é calculado o valor total da compra e impresso na tela o extrato da compra. 

produto    = str(input("Insira o nome do produto: "))
valor      = float(input("Insira o valor unitário do produto R$: "))
quantidade = int(input("Insira a quantidade: "))

total = (valor * quantidade)

print ("Você comprou", quantidade ,"unidades do produto" , produto , "totalizando em R$", total)