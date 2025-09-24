#Neste programa empregamos a formuma que descreve o volume de uma caixa retângular.
#O usuário insere as dimensções da caixa, através da função input
#Através de operadores aritméticos realizamos a operação e atribuímos à uma variável e imprimimos o valor na tela.

x = int(input("Insira a largura da caixa: "))
y = int(input("Insira a altura da caixa: "))
z = int(input("Insira a profundidade da caixa: "))

x = (x*y*z)

print("O volume da caixa é: ", x, "cm³")
