#Ordenar
#Ithan Camacho
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer numero: "))
if num1 > num2:
    if num2 > num3:
        print ("El orden es", num1,", ", num2,", ", num3,".")
    elif num3 > num2:
        print("El orden es", num1,", ", num3,", ", num2,".")
elif num3 > num1:
    if num1 > num2:
        print("El orden es", num3,", ", num1,", ", num2,".")
    elif num2 > num1:
        print("El orden es", num3,", ", num2,", ", num1,".")
elif num2 > num3:
    if num3 > num1:
        print("El orden es", num2,", ", num3,", ", num1,".")
    elif num1 > num3:
        print("El orden es", num2,", ", num1,", ", num3,".")