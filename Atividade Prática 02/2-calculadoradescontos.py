#Este programa, permite o calculo de desconto, 
#O usuário insere o nome do produto, preço e total de desconto.
#O programa imprime na tela o total com desconto.

nomeproduto  = str(input("Qual o nome do produto?"))
precoproduto = float(input("Qual o preço do produto?"))
desconto     = float(input("Qual o total e desconto, em % ?"))

desconto1 = (desconto / 100)
parcial = (precoproduto * desconto1)
total   = (precoproduto - parcial)

print("O produto ", nomeproduto, "no valor de", precoproduto, ", com desconto de", desconto, " e o total foi de R$ ", total)


                    