#Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario con su media, 
#varianza y desviación típica.

def cuadrado (lista):
    """Funcion que calcula el cuadrado de cada uno de los valores en una lista de numeros
    Parametros:
    Lista= Lista de numeros a los que se le aplicara el cuadrado
    """
    lista2=[]
    for i in lista :
        lista2.append(i**2)
    return lista2

def ParametrosEstadisticos (lista):
    """Funcion que calcula los parametros estadisticos(Media, variaza y desviacion tipica) de una lista de valores numericos
    Parametros:
    lista= Lista de numeros
    Return:
    Devuelve un diccionario con los parametros estadisticos de la lista de numeros
    """
    diccionario={}
    diccionario['Media']=sum(lista)/len(lista)
    diccionario['Varianza']=sum(cuadrado(lista))/len(lista)-diccionario['Media']**2
    diccionario['Desviacion tipica']= diccionario['Varianza']**0.5
    return diccionario

print(ParametrosEstadisticos([1,2,3,4,5]))

