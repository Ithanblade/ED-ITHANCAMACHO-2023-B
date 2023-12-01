#Aceptación
#Ithan Camacho

nota1 = int(input("Ingrese su nota 1: "))
nota2 = int(input("Ingrese su nota 2: "))
edad = int(input("Ingrese su edad: "))
sexo = input(("Ingrese la letra con su sexo(M:Masculino / F:Femenino): "))
if (nota1 >= 5 and nota2 >= 5) and (edad >= 18 and sexo == "F"):
    print("Aceptada.")
elif (edad >= 18 and sexo == "M"):
    print("Posible.")
else:
    print("No aceptada.")