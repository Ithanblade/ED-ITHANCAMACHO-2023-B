#Nota Final
#Ithan Camacho
parcial1 = float(input("Ingrese la nota del parcial 1: "))
parcial2 = float(input("Ingrese la nota del parcial 2: "))
parcial3 = float(input("Ingrese la nota del parcial 3: "))
examenF= float(input("Ingrese la nota del examen final: "))
trabajoF=float(input("Ingrese el nota del trabajo final: "))
promParcial= (parcial1+parcial2+parcial3)/3

notaFinal= (promParcial*0.55)+(examenF*0.3)+(trabajoF*0.15)
print("La nota final en la materia de Algoritmos es de: ", notaFinal)