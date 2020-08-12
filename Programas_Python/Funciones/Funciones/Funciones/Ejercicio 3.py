#Escribir una función que reciba un número entero positivo y devuelva su factorial.

def Factorial (entero):
    """
    Funcion que devuelve el factorial de un numero
    Ej: 4!=4*3*2*1=24
    Parametros:
    entero=Numero entero del que se calcula el factorial
    """
    factorial=1
    for i in range(entero):
        factorial*=i+1
    return factorial
numero=str(input("Introduzca un numero entero: "))
while not numero.isnumeric() :
    print("ERROR.")
    numero=str(input("Introduzca un numero entero POSITIVO: "))

print(Factorial(int(numero)))

