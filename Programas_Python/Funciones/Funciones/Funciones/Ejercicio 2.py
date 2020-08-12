#Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!.

def Saludo(nombre):
    """
    Funcion que devuelve un saludo por pantalla
    Parametros:
    nombre: Nombre de usuario
    """
    print("¡Hola "+nombre+"!")
    return
izena=str(input("Introduzca su nombre: "))
Saludo(izena)

