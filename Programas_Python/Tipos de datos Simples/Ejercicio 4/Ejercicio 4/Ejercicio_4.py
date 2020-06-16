
#Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e 
#imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

Nombre= str(input("Introduzca su nombre: \n"))
NumeroEntero= int(input("Introduzca el numero de veces que desea ver su numero en pantalla: \n"))
aux=0
print ("A continuacion aparecera su nombre",NumeroEntero,"veces:")
while NumeroEntero>aux :
    aux=aux+1
    print(Nombre)