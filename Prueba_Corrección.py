#Ithan Camacho
print("BIENVENIDOS AL CARBONERO")
print("Por favor ingrese los datos para la factura: ")
nombre = input("Ingrese su nombre: ")
cedula = input("Ingrese su número de cedula: ")
correo = input("Ingrese su correo electrónico: ")

print("El Carbonero le ofrece los siguientes tipos de hamburguesas: ")
print("1. Sencilla")
print("2. Doble")
print("3. Triple")
tipo = int(input("Ingrese el número del tipo de hamburguesa que desea: "))

if tipo != 1 and tipo != 2 and tipo != 3:
    print("Lo sentimos, en el Carbonero no tenemos ese tipo de hamburguesa")
else:
    if tipo == 1:
        valor = 1.5
    elif tipo == 2:
        valor = 2.5
    elif tipo == 3:
        valor = 3.25

    cantidad = int(input("Ingrese la cantidad de hamburguesas que desea: "))
    subtotal = valor * cantidad
    print("Por su compra debe cancelar:", subtotal)

    print("Por favor, ingrese un número para indicar el tipo de pago: ")
    print("1. Efectivo")
    print("2. Tarjeta de crédito")
    tipopago = int(input())

    total = 0
    if tipopago != 1 and tipopago != 2:
        print("Lo sentimos, en el Carbonero no tenemos ese tipo de pago")
    else:
        if tipopago == 1:
            total = subtotal
            print("Su pago es en efectivo, por favor cancele sin recarga: ",total, "dólares",nombre,"gracias por su compra, vuelva pronto")
        elif tipopago == 2:
            total = (subtotal * 0.90) + subtotal
            print("Su pago es con tarjeta de crédito, por favor cancele con recarga del 5%: ",total, "dólares",nombre,"gracias por su compra, vuelva pronto")