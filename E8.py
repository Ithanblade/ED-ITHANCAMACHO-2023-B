#velocidades   
#Ithan Camacho
import math
v1= float(input("Ingrese la velocidad del primer coche: "))
v2= float(input("Ingrese la velocidad del segundo coche: "))
d= float(input("Ingrese la distancia entre los dos coches: "))
if v1>v2:
    t=d/(v1-v2)
elif v1<v2:
    t=d/(v2-v1)
else:
    print("Los coches tienen la misma velociad, no se acercan ni se alejan")
tiempo=t*60
print("El tiempo que tardaran en encontrarse es de: ", tiempo, "minutos")