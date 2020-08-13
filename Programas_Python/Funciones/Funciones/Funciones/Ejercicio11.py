#Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y su frecuencia. 
#Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.

def CuentaPalabras (cadena):
    """Funcion que recibe una cadena y devuelve un diccionario con cada palabra y las veces que esta repetida
    Parametros:
        -cadena: Variable que almacena la frase introducida por el usuario
    Return:
        - Devuelve un diccionario con cada palabra y la frecuencia {Palabra:frecuencia)} en la que se repite
    """
    cadena=cadena.split()
    diccionario={}
    for i in cadena:
        if i in diccionario :
            diccionario[i]+=1
        else:
            diccionario[i]=1
    return diccionario

def MasRepetida (diccionario):
    """Funcion que determina que palabra aparece con mas frecuencia en la frase
    Parametros:
        -diccionario: Un diccionario palabnra:frecuencia
    Return:
        -Devuelve una tubla con la palabra mas repetida y su frecuencia en la frase
    """
    Maxpalabra=""
    Maxfrecuencia=0
    for palabra, frecuencia in diccionario.items():
        if frecuencia>Maxfrecuencia :
            Maxpalabra=palabra
            Maxfrecuencia=frecuencia
    return Maxpalabra, Maxfrecuencia

cadena=str(input("Introduzca una frase:"))
print(CuentaPalabras(cadena))
print(MasRepetida(CuentaPalabras(cadena)))