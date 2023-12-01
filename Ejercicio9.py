#Tipo de Motor
#Ithan Camacho
def dimeTipoMotor(motor):
    switcher = {
        0: "No hay establecido un valor definido para el tipo de bomba",
        1: "La bomba es una bomba de agua",
        2: "La bomba es una bomba de gasolina",
        3: "La bomba es una bomba de hormigón",
        4: "La bomba es una bomba de pasta alimenticia"
    }
    return switcher.get(motor, "No existe un valor válido para tipo de bomba")

motor = int(input("Seleccione el tipo de motor que desea: "))
print(dimeTipoMotor(motor))
