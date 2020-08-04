#Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona 
#(por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. 
#Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.

diccionario={}
nombre= str(input("Introduzca su nombre:"))
while not nombre.isalpha() :
    print("ERROR, EL NOMBRE NO PUEDE CONTENER NUMEROS NI CARACTERES DIFERENTES A LETRAS")
    nombre= str(input("Introduzca su nombre:"))
diccionario["Nombre"]=nombre
print(diccionario)
edad= str(input("Introduzca su edad: "))
while not edad.isnumeric() :
    print("ERROR, LA EDAD TIENE QUE SER UN VALOR NUMERICO MAYOR QUE 0")
    edad= str(input("Introduzca su edad: "))
diccionario["Edad"]=edad
print(diccionario)
direccion= str(input("Introduzca su direccion: "))
diccionario["Direccion"]=direccion
print(diccionario)
telefono= str(input("Introduzca su numero de telefono: "))
while not telefono.isnumeric() or len(telefono)<9 :
    print("ERROR, EL NUMERO DE TELEFONO TIENE QUE SER UN VALOR NUMERICO DE 9 DIGITOS")
    telefono= str(input("Introduzca su numero de telefono: "))
diccionario["Telefono"]=telefono
print(diccionario)
