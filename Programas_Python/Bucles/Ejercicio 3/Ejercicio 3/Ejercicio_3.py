#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números 
#impares desde 1 hasta ese número separados por comas.

numero=int(input("Introduzca un numero entero positivo: \n"))
while numero<0 :
    print("ERROR, el numero introducido es negativo.")
    numero=int(input("Introduzca un numero entero positivo: \n"))
for i in range(numero) :
    if (i+1)%2 !=0 :
        print(str(i+1),end=",")