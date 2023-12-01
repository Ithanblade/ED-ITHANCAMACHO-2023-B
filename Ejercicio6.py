#Transporte
#Ithan Camacho
alumnos = int(input("Escriba cuantos alumnos van a ir: "))
if alumnos >= 100:
    print ("El costo por alumno es de: ", 65,"$")
    print ("El valor de la renta al autobus es: ", alumnos * 65,"$")
elif alumnos >= 50 and alumnos <= 99:
    print ("El costo por alumno es de: ", 70,"$")
    print ("El valor de la renta al autobus  es: ", alumnos * 70,"$")
elif alumnos >= 30 and alumnos <= 49:
    print ("El costo por alumno es de: ", 95,"$")
    print ("El valor de la renta al autobus es: ", alumnos * 95,"$")
else:
    print ("El valor de la renta al autobus es : ", 4000,"$")