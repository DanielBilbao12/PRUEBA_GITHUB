#Ejercicio para poner el practica las nociones basicas de python

contador=0
print ("Introduce un numero: ")
nUsuario=int(input())
print (f"El numero introducido por el usuario es: ",nUsuario)
while contador<=10 :
    multiplicacion= nUsuario*contador
    print("El resultado de ",nUsuario, " * ",contador," es: ", multiplicacion)
    contador=contador+1
