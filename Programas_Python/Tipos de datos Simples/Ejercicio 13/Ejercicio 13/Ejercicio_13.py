# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
# Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. 
# Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. 
# Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. 
# Redondear cada cantidad a dos dec
#NOTA: la formula la he obtenido de la solucion propuesta en la WEB

Ianual= float(0.04)
DineroCuenta=float(input("Introduzca el dnero depositado en la cuenta de ahorros: \n"))
Balance1=float(DineroCuenta*(1+Ianual))
print("El resultado de tus ahorros el primer año es de: ",str(round(Balance1,2)),"euros")
Balance2=float(Balance1*(1+Ianual))
print("El resultado de tus ahorros el segundo año es de: ",str(round(Balance2,2)),"euros")
Balance3=float(Balance2*(1+Ianual))
print("El resultado de tus ahorros el primer año es de: ",str(round(Balance3,2)),"euros")