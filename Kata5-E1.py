# programa que pueda calcular la distancia entre dos planetas.
from turtle import distance


print("Bienvenido a  programa que pueda calcular la distancia entre dos planetas.")
print("Comencemo introduciendo las distancias a las que se encuentra cada planeta" 
+"con respecto del sol")
planeta1 = 149597870
planeta2 = 778547200
#planeta1 = input("Ingresa la distancia del planeta1: ")
#palneta2 = input("Ingresa la distancia del planeta2: ")
distancia = abs(planeta2-planeta1)
print("La distancia en Km es: "+str(distancia))
distancia = round(distancia *0.621)
print("La distancia en millas es: "+str(distancia))
