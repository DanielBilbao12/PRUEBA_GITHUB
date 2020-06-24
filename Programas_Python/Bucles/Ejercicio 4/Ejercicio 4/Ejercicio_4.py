#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la 
#cuenta atrás desde ese número hasta cero separados por comas.

numero= int(input("Introduzca un numero entero positivo: \n"))
while numero<0 :
    print("ERROR. Numero negativo")
    numero= int(input("Introduzca un numero entero positivo: \n"))
for i in range(numero+1) :
    print(numero-i,end=",")