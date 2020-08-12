#Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.

def AreaCirculo (radio):
    """
    Funcion que retorna el Area de un círculo
    Parametros:
    Radio: Valor del radio del circulo
    pi=Valor constante que vale 3,14
    """
    return 2*3.14*radio**2
def VolumenCilindro(longitud,radio):
    """
    Funcion que retorna el Area de un cilindro
    Parametros:
    longitud= valor de la distancia entre las tapas/bases del cilindro
    radio= Valor del radio de las tapas del cilindro
    """
    return AreaCirculo(radio)*longitud

print(VolumenCilindro(5,3))
