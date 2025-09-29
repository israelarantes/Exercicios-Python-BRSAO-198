# Este programa, converte moedas, do real para euro e dolar, utilizando variáveis pré-definidas 
# O usuário insere o valor em reais, programa faz a operação, e imprime na tela os valores correspondentes


dolar = 5.5
euro  = 6.15

real = float(input("Insira o valor em reais: "))

dreal = real * dolar 
ereal = euro * real 

print ("O valor em Reais é R$", "%.2f"%real ,".Convertido em euros €", "%.2f"%ereal ,"e convertido em dólares $", "%.2f"%dreal)