#Este programa calcula a média de três notas e exibe o resultado na tela

p1 = float(input("Qual foi a nota da primeira prova?"))
p2 = float(input("Qual foi a nota da segunda prova?"))
p3 = float(input("Qual foi a nota da terceira prova?"))

final = (p1+p2+p3)/3

print ("A nota da P1 foi de", "%.2f"%p1, " a da P2 foi de", "%.2f"%p2 ," e da P3 foi","%.2f"%p3, ". A nota final foi:", "%.2f"%final )
