#Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.

numeros=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(numeros),-1,-1) :
    print (str(i),end=",")
print("")