#Escribir un programa que permita gestionar la base de datos de clientes de una empresa. 
#Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF, 
#y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente), 
#donde preferente tendrá el valor True si se trata de un cliente preferente. 
#El programa debe preguntar al usuario por una opción del siguiente menú: 
#(1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. 
#En función de la opción elegida el programa tendrá que hacer lo siguiente:
#1- Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
#2- Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
#3- Preguntar por el NIF del cliente y mostrar sus datos.
#4- Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
#5- Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
#6- Terminar el programa.

clientes={}
datos={}
print("*********************************")
print("*1- Añadir cliente              *")
print("*2- Eliminar cliente            *")
print("*3- Mostrar datos               *")
print("*4- Mostrar todos los clientes  *")
print("*5- Mostrar clientes preferentes*")
print("*6- Salir                       *")
print("*********************************")
menu=0
while menu!=6 :
    if menu==1:
        dni=str(input("Introduce el dni del cliente:"))
        nombre= str(input("Introduzca su nombre:"))
        while not nombre.isalpha() :
            print("ERROR, EL NOMBRE NO PUEDE CONTENER NUMEROS NI CARACTERES DIFERENTES A LETRAS")
            nombre= str(input("Introduzca su nombre:"))
        datos["Nombre"]=nombre
        direccion= str(input("Introduzca su direccion: "))
        datos["Direccion"]=direccion
        telefono= str(input("Introduzca su numero de telefono: "))
        while not telefono.isnumeric() or len(telefono)<9 :
            print("ERROR, EL NUMERO DE TELEFONO TIENE QUE SER UN VALOR NUMERICO DE 9 DIGITOS")
            telefono= str(input("Introduzca su numero de telefono: "))
        datos["Telefono"]=telefono
        correo=str(input("Introduzca su correo electronico: "))
        datos["Correo"]=correo
        preferente=str(input("¿Es usted cliente preferente? (SI/NO): "))
        while preferente.upper()!="SI" and preferente.upper()!="NO" :
            print("ERROR, responda con SI o NO")
            preferente=str("¿Es usted cliente preferente? (SI/NO): ")
        if preferente.upper()=="SI" :
            preferencia=True
        else :
            preferencia=False
        datos["Preferente"]=preferencia
        clientes[dni]=datos
    elif menu==2:
        dni=str(input("Introduce el dni del cliente:"))
        if dni in clientes:
            del clientes[dni]
        else:
            print("No hay ningun cliente con ese DNI")
    elif menu==3:
        dni=str(input("Introduce el dni del cliente:"))
        if dni in clientes:
            print("Los datos del cliente con DNI: ",str(dni))
            for clave, valor in clientes[dni].items() :
                print(clave.title()+":",valor)
        else:
            print("No hay ningun cliente con ese DNI")
    elif menu==4:
        print("La lista de los clientes es la siguiente:")
        for clave, valor in clientes.items() :
            print(clave, valor["Nombre"])
    elif menu==5:
        print("La lista de los clientes preferentes: ")
        for clave, valor in clientes.items() :
            if valor["Preferente"] :
                print(clave, valor["Nombre"])
    menu=int(input("Que operacion desea realizar?"))
