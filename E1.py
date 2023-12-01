#Perimetro y area
import math


base= int(input("Ingrese el valor de la base: "))
altura=int(input("Ingrese el valor de la altura: "))
radio=int(input("Ingrese el valor del radio: "))

perimetro= (base*2)+(altura*2)
area= base*altura
areaC= math.pi*(radio**2)
perimetroC= 2*math.pi*radio

print("El perimetro del rectangulo es de: ", perimetro)
print("El area del rectangulo es de: ", area)   

print("El area del circulo es de: ", areaC)
print("El perimetro del circulo es de: ", perimetroC)