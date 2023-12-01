#triangulos
#Ithan Camacho

A = float(input("Ingrese la longitud del primer lado: "))
B = float(input("Ingrese la longitud del segundo lado: "))
C = float(input("Ingrese la longitud del tercer lado: "))
if (pow(A,2)+pow(B,2)) == pow(C,2) or (pow(A,2)+pow(C,2)) == pow(B,2) or (pow(B,2)+pow(C,2)) == pow(A,2):
    print("El triángulo es rectángulo.")
elif A == B and B == C:
    print("El triángulo es equilátero.")
elif A == B or B == C or A == C:
    print("El triángulo es isósceles.")
elif A != B and B != C and A != C:
    print("El triángulo es escaleno.")
else:
    print("Los datos ingresados no corresponden a un triángulo.")