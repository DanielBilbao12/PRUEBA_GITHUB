#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces

palabra=str(input("Introduzca una palabra para mostrarla por pantalla 10 veces: \n"))
aux=0
print("A continuacion se imprimira por pantalla la palabra introducida: ")
while aux<10 :
    print (palabra)
    aux=aux+1