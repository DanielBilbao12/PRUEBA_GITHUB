# Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. 
# Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.

nombre= str(input("Introduzca su nombre:"))
while not nombre.isalpha() :
    print("ERROR, EL NOMBRE NO PUEDE CONTENER NUMEROS NI CARACTERES DIFERENTES A LETRAS")
    nombre= str(input("Introduzca su nombre:"))
edad= str(input("Introduzca su edad: "))
while not edad.isnumeric() :
    print("ERROR, LA EDAD TIENE QUE SER UN VALOR NUMERICO MAYOR QUE 0")
    edad= str(input("Introduzca su edad: "))
direccion= str(input("Introduzca su direccion: "))
telefono= str(input("Introduzca su numero de telefono: "))
while not telefono.isnumeric() or len(telefono)<9 :
    print("ERROR, EL NUMERO DE TELEFONO TIENE QUE SER UN VALOR NUMERICO DE 9 DIGITOS")
    telefono= str(input("Introduzca su numero de telefono: "))
diccionario= {'NOMBRE': nombre,'EDAD': edad, 'DIRECCION' : direccion, 'TELEFONO' : telefono }
print(diccionario['NOMBRE'], "tiene",diccionario['EDAD'], "años, vive en",diccionario['DIRECCION'],"y su numero de telefono es",diccionario['TELEFONO'])
