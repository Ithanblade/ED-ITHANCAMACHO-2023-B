#Dinero
#Ithan Camacho
dosEuros= float(input("Ingrese la cantidad de monedas de 2 euros: "))
unEuro= float(input("Ingrese la cantidad de monedas de 1 euro: "))
cincuentaC= float(input("Ingrese la cantidad de monedas de 50 centimos: "))
veinteC= float(input("Ingrese la cantidad de monedas de 20 centimos: "))
diezC= float(input("Ingrese la cantidad de monedas de 10 centimos: "))

totalE= (dosEuros*2)+(unEuro*1)+(cincuentaC*0.5)+(veinteC*0.2)+(diezC*0.1)


print("El total de dinero que tiene en euros: ", totalE)