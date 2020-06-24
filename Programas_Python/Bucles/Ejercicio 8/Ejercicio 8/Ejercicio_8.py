#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.

entero= str(input("Introduce un numero entero positivo para crear el triangulo: "))
while not entero.isnumeric() :
    print("ERROR, no has introducido un numero entero.")
    entero= str(input("Introduce un numero entero: "))
for i in range(1,int(entero),+2) :
    for j in range(i,int(entero),+2) :
        print(i,end="")
    print(j)