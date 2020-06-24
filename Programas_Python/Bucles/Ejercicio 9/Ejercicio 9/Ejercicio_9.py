#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
#pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

contraseña="contraseña"

usuario=str(input("Introduzca la contraseña: "))
while usuario.lower() != contraseña :
    print("ERROR.")
    usuario=str(input("Introduzca la contraseña: "))
print("CORRECTO!")




