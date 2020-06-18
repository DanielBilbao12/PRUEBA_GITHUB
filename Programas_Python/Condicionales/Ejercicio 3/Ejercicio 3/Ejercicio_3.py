#Escribir un programa que pida al usuario dos números y muestre por pantalla su división.
# Si el divisor es cero el programa debe mostrar un error.

a=float(input("Introduzca el dividendo: "))
b=float(input("Introduzca el divisor: "))
if b==0 :
    print("ERROR, dividendo igual a 0")
else :
    division = a/b
    print("El resultado de la division es:",str(round(float(division),2)))


