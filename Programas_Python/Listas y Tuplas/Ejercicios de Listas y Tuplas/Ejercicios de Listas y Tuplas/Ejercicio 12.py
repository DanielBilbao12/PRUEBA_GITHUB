#Almacenar las matrices A(1 2 3)  B(-1 0)
#                        (4 5 6)   ( 0 1)
#                                  ( 1 1)
#en una lista y muestre por pantalla su producto.
#Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista.
# Las tuplas son como las listas pero se declaran con parentesis, no se pueden eliminar valores ni añadir etc.. tiempo de ejecucion menor

a=((1, 2, 3),
     (4, 5, 6))
b=((-1, 0),
     (0, 1),
     (1,1))
c=[[0, 0],
   [0, 0]]
for i in range(len(a)) : #de 0 a (numero de objetos en a)-1= 1
    for j in range(len(b[0])) : #de 0 a (numero de objetos en el primer objeto de b)-1=2
        for k in range(len(b)) : #de 0 a (numero de objetos en b)-1= 2
           c[i][j] += a[i][k] * b[k][j]
print("El resultado de la multiplicacion entre la matriz A y B representado por una LISTA es de: ")
for i in range(len(c)) :
    print(c[i])
#Para convertir el resultado en otra TUPLA de manera que quede guardado e inmodificable, siguiente codigo
for i in range(len(c)) :
    c[i]=tuple(c[i])
c=tuple(c)
print("El resultado de la multiplicacion entre la matriz A y B representado por una TUPLA es de: ")
for i in range(len(c)) :
    print(c[i])
print("\nNOTA: Las TUPLAS van entre PARENTESIS y las LISTAS van entre CORCHETES")
