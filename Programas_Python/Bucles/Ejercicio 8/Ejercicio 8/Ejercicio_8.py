#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.

entero= str(input("Introduce un numero entero positivo para crear el triangulo: "))
while not entero.isnumeric() :
    print("ERROR, no has introducido un numero entero.")
    entero= str(input("Introduce un numero entero: "))
for i in range(1,int(entero),2) : #i inicia el bucle valiendo 1, hasta que i=entero-1 se repite e bucle, de 2 en 2
    for j in range(i,0,-2) : #j inicia en el valor de i, hasta j=0 se repite el bucle, de -2 en -2
        print(j,end=" ")
    print("")