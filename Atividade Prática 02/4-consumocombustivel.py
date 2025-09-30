distancia = float(input("Quantos Quilômetros foram rodados na viagem?"))
consumo   = float(input("Quantos litros de combustível foram consumidos?"))

media = (distancia/consumo)
 
print ("A média de consumo foi de ", "%.2f"%media, " km/l. A distancia percorrida foi de ", "%.2f"%distancia,"Km e o consumo total foi de ", "%.2f"%consumo, "l de combustível")
