#Escribir una función que convierta un número decimal en binario y otra que convierta un número binario en decimal.


def ConversionBinaria (numero):
    """Funcion que convierne un valor entero en binario
    Parametros:
        -numero: Numero entero
    Return:
    Valor binario
    """
    binario=[]
    while numero>0 :
        binario.append(str(numero%2))
        numero//=2
    binario.reverse()
    return "".join(binario)

def ConversionDecimal (numero):
    """Funcion que convierte un valor binario en decimal
    Parametros:
        -numero: Numro expresado en base 2
    Return:
    Valor decimal
    """
    numero=list(numero)
    numero.reverse()
    decimal=0
    for i in range(len(numero)):
        decimal += int(numero[i])*2**i
    return decimal

print(ConversionBinaria(3))
print(ConversionDecimal("11"))