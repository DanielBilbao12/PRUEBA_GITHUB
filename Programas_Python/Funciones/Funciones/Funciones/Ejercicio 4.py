#Escribir una función que calcule el total de una factura tras aplicarle el IVA.
# La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. 
# Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

def Factura(cantidad,iva=21):
    """
    Funcion que devuelve el valor de una factura, dependiendo de la cantidad y el porcetaje IVA a aplicar
    Parametros:
    cantidad= Cantidad en euros de la factura
    IVA= impuesto al valor añadido, un valor que en caso de ser nulo es 21.
    """
    return cantidad + cantidad*iva/100

print(Factura(1000,10))
print(Factura(1000))
