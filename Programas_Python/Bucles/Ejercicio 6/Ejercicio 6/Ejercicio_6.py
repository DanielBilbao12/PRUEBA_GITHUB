# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, 
# de altura el número introducido.

numero= str(input("Introduzca un numero entero: "))
#Comprobacion de que se introdujo un numero
while not numero.isnumeric() :
    print("ERROR. No ha introducido un numero entero. ")
    numero=str(input("Introduzca un numero entero: "))
for i in range(int(numero)) :
    for j in range(i+1) :
        print("*",end="")
    print("")