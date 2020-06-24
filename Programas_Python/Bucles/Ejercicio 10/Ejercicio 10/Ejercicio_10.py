#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

entero= str(input("Introduzca un numero entero positivo: "))
while not entero.isnumeric() :
    print("ERROR.")
    entero= str(input("Introduzca un numero entero positivo: "))
#Para que un numero sea primo tiene que ser divisible por 1 y por el mismo solamente, en el caso de 1 se considera primo
kont=0
for i in range(1,int(entero)+1,1) :
    if int(entero)%i == 0 :
        kont=kont+1
if kont<=2 :
    print("NUMERO PRIMO")
else:
    print("NUMERO NO PRIMO")