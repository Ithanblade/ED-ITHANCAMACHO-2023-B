#Comisiones
#Ithan Camacho

sueldo = float(input("Ingrese su sueldo base: "))
venta1 = float(input("Ingrese el valor de la primera venta: "))
venta2 = float(input("Ingrese el valor de la segunda venta: "))
venta3 = float(input("Ingrese el valor de la tercera venta: "))

comisiones = (venta1 + venta2 + venta3) * 0.1 
total = sueldo + comisiones  

print("Obtendrá por comisiones un total de:", comisiones)
print("El total que recibirá es de:", total)
