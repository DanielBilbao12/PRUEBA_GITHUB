#Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo.

def mcd(numero1,numero2):
    """Funcion que calcula el maximo comun divisor de dos numeros
    Parametros:
        -numero1: Un numero entero
        -numero2: Un numero entero
    Return:
    Se devuelve el maximo comun divisor entre esos 2 numeros
    """
    aux=0
    while(numero2>0):
        aux=numero2
        numero2=numero1%numero2
        numero1=aux
    return numero1

def mcm(numero1,numero2):
    """Funcion que calcula el minimo comun mutiplo de dos numeros
    Parametros:
        -numero1: Un numero entero
        -numero2: Un numero entero
    Return:
    El minimo comun multiplo de esos dos numeros
    """
    if numero1>numero2:
        mayor=numero1
    else:
        mayor=numero2
    while(mayor%numero1 !=0) or (mayor%numero2 !=0):
        mayor+=1
    return mayor

print(mcd(36,24))
print(mcm(24,36))