
#Escribir una función que convierta un número decimal en binario y otra que convierta un número binario en decimal.

def ConversioBinaria (numero):
    """Funcion que convierte un valor decimal en binario
    Parametros:
        -numero: Numero entero
    Return:
    Valor en binario
    """
    restos=[]
    aux=numero
    while aux//2 != 1 :
        restos.append(aux%2)
        aux//=2
    restos.append(0)
    restos.append(1)
    restos.reverse()
    return restos
print(ConversioBinaria(2))