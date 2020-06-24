#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido 
#(desde 1 hasta su edad).

edad= int(input("Introduzca su edad: "))
print("A continuacion se imprimiran por pantalla todos los años que has cumplido desde el primer año: ")
for i in range(edad) : #La funcion range crea una lista inmutable, en este caso crea una lsita de (0,edad)
    print ("Has cumplido",str(i+1),"años")