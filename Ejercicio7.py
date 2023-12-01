#Internacional
#Ithan Camacho
print ("Contienente que se puede ir:")
print ("1:America del Norte")
print ("2:America del Central")
print ("3:America del Sur")
print ("4:Europa")
print ("5:Asia")
opciones = input("Seleccione el numero del contienente a enviar:")
peso = float(input("Escriba cuanto peso tiene su paquete en kg: "))
if peso > 5:
    print ("El paquete es muy pesado no puede viajar")
elif opciones == "1":
    print ("El costo por America del Norte es de: ", 24,"euros")
    print ("El valor total que debe pagar es de: ", peso * 24,"euros")
elif opciones == "2":
    print ("El costo por America del Central es de: ", 20,"euros")
    print ("El valor total que debe pagar es de: ", peso * 20,"euros")
elif opciones == "3":
    print ("El costo por America del Sur es de: ", 21,"euros")
    print ("El valor total que debe pagar es de: ", peso * 21,"euros")
elif opciones == "4":
    print ("El costo por Europa es de: ", 10,"euros")
    print ("El valor total que debe pagar es de: ", peso * 10,"euros")
elif opciones == "5":
    print ("El costo por Asia es de: ", 18,"euros")
    print ("El valor total que debe pagar es de: ", peso * 18,"euros")
else:
    print ("El valor no es valido")
