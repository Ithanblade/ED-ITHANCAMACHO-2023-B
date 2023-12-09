#Ithan Camacho
print("BIENVENIDOS AL CARBONERO")
print("Por favor ingrese los datos para la factura: ")
nombre=input("Ingrese su nombre: ")
cedula=input("Ingrese su número de cedula: ")
correo=input("Ingrese su correo electrónico: ")
print("El Carbonero le ofrece los siguientes tipos de hamburguesas: ")
print("1. Sencilla")
print("2. Doble")
print("3. Triple")
tipo=int(input("Ingrese el númmero del tipo de hamburguesa que desea: "))
match tipo:
    case 1:
        valor=1.5
    case 2: 
        valor=2.5
    case 3:
        valor=3.25
    case _:
        print("Lo sentimos, en el Carbonero no tenemos ese tipo de hamburguesa")
        exit()
cantidad=int(input("Ingrese la cantidad de hamburguesas que desea: "))
subtotal=valor*cantidad
print("Por su compre debe cancelar: ",subtotal)
print("Por favor, ingrese un número para indicar el tipo de pago: ")
print("1. Efectivo")
print("2. Tarjeta de crédito")
tipopago=int(input())
match tipopago:
    case 1:
        total=subtotal
        print("Su pago es en efectivo, por favor cancele sin recarga: ",total, "dólares",nombre,"gracias por su compra, vuelva pronto")
    case 2:
        total=(subtotal*0.05) + subtotal
        print("Su pago es con tarjeta de crédito, por favor cancele con recarga del 5%: ",total, "dólares",nombre,"gracias por su compra, vuelva pronto")
    case _:
        print("Por favor ingrese un número válido")
        exit()   