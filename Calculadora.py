#Calculadora
#Ithan Camacho
print("CALCULADORA")
n1=float(input("Por favor ingrese el primer valor: "))
n2=float(input("Por favor ingrese el segundo valor: "))
print("Por favor ingrese el número de la operación que desea realizar: ")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. Potenciación")
print("6. Modulo")
operacion=int(input())
if operacion ==4 and n2==0:
    print("No se puede dividir entre cero")
    exit()
else:
    match operacion:
        case 1:
            resultado=n1+n2
            print("El resultado de la suma es: ",resultado)
        case 2:
            resultado=n1-n2
            print("El resultado de la resta es: ",resultado)
        case 3:
            resultado=n1*n2
            print("El resultado de la multiplicación es: ",resultado)
        case 4:
            resultado=n1/n2
            print("El resultado de la división es: ",resultado)
        case 5:
            resultado=n1**n2
            print("El resultado de la potenciación es: ",resultado)
        case 6:
            resultado=n1%n2
            print("El resultado del módulo es: ",resultado)
        case _:
            print("Por favor ingrese un número válido")
