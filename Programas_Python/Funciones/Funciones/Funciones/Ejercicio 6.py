#Escribir una función que reciba una muestra de números en una lista y devuelva su media.

def Media (lista):
    """Funcion que retorna la media de una lista de numeros
    Parametros:
    Lista= Lista de numeros
    """
    return sum(lista)/len(lista)

print(Media([5,5,5,5,5,5,5,5,5,5]))
print(Media([1,2,3,4,5]))
