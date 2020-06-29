#Almacenar las matrices A(1 2 3)  B(-1 0)
#                        (4 5 6)   ( 0 1)
#                                  ( 1 1)
#en una lista y muestre por pantalla su producto.
#Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista.
#-> ESTO SON TUPLAS

a=[(1, 2, 3),
     (4, 5, 6)]
b=[(-1, 0),
     (0, 1),
     (1,1)]
c=[(0, 0),
   (0, 0)]
for i in range(len(a)) :
    for j in range (len(b[0])) :
        for k in range (len(b)) :
            c[i][j]=