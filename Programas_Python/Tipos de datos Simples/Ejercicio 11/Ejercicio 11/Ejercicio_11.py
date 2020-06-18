#Escribir un programa que pregunte al usuario una cantidad a invertir, 
#el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión redondeado en 2 decimales.
#NOTA: La formula la he obtenido de la solucion al ejercicio.

cantidad=float(input("Introduzca el numero de euros(€) que desea invertir: \n"))
interes=float(input("Introduzca el interes porcentuañ anual de dicha inversion: \n"))
años= int(input("Introduzca el numero de años de la inversion: \n"))
Capitalfinal= round((cantidad*(interes/100+1)**años),2) # Cambiando el segundo argumento de la funcion predefinida round() definimos el numero de decimales
print ("El capital obtenido de la inversion es de: ",str(Capitalfinal))