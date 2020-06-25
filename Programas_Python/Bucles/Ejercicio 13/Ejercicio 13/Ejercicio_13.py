#Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.

usuario=str(input("Introduzca una frase, numero o lo que sea que quieras que se reproduzca como tu ECO: \n"))
while usuario.upper() != "SALIR" :
    print(usuario)
    usuario=str(input("Introduzca una frase, numero o lo que sea que quieras que se reproduzca como tu ECO: \n"))