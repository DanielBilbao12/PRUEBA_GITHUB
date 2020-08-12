#Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.

def cuadrado (lista):
    lista2=[]
    for i in lista :
        lista2.append(i**2)
    return lista2

print(cuadrado([1,2,3,4,5]))
