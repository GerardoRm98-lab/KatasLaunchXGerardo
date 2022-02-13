# Alerta Asteroide
import string

print(" Bienvenido al programa de alerta de Asteroide!!! ")
v = input(" Introduzca por favor la velocidad del Asteroide en Km/s: ")
if float(v)>25:
    print("Alerta!!! El asteroide viaja a: " + v+"Km/s"+" y representa un peligro!!")
elif float(v)<=25:
    print("A esta velocidad el asteroide no representa un peligro C:")
else:
    print("Verifica los datos de entrada c:")

#Alerta avistamiento
print(" \nBienvenido al programa de avistamiento de Asteroides!!! ")
print(" Si un asteroide entra en la atmósfera de la Tierra a una velocidad " 
+ "mayor o igual a 20 km/s, a veces produce un rayo de luz que se puede ver desde la Tierra.")
v = input(" Introduzca por favor la velocidad del Asteroide en Km/s: ")
if float(v)>=20:
    print("Probablemente puedas ver el asteroide desde la tierra O-O")
elif float(v)<20:
    print("A esta velocidad el asteroide no puede verse desde la superficie terrestre :c")
else:
    print("Verifica los datos de entrada c:")

#Alerta tamaño y velocidad
print(" \nBienvenido al programa de defensa planetaria!!!")
print("Nuestros sensores indican que se aproxima un Asteroide a la Tierra")
v = input(" Introduzca por favor la velocidad del Asteroide en Km/s: ")
d = input(" Introduzca por favor las dimensiones del Asteroide en m: ")
if float(v)>=20:
    print("Probablemente puedas ver el asteroide desde la tierra")
if float(v)>25:
    print("Advertencia Asteroide con velocidad superior a 25Km/s")
if float(v)<=25 and float(d)<25:
    print("Probablemente se quemará a medida que entren en la atmósfera de la Tierra.")
elif float(v)>=25 and float(d)>25:
    print("Un asteroide de este tamaño causaria muchisimo daño!!")
else:
    print("Verifica los datos de entrada c:")
