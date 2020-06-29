#Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8,
# y muestre por pantalla el menor y el mayor de los precios.

precios=[50,75,46,22,80,65,8]
precios.sort()
print ("El menor de los precios es de:",str(precios[0]),"€")
print ("El mayor de los precios es de:",str(precios[6]),"€")
###################################################################
# En caso de no usar el metodo sort ni saber la longitud de la lista, este codigo tambien funciona
#min = max = precios[0]
#for precio in precios:
 #   if precio < min:
  #      min = precio
   # elif precio > max:
    #    max = precio
#print("El mínimo es ", str(min)) 
#print("El máximo es ", str(max))