#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m>
# son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.

n= int(input("Introduzca un numero entero: \n"))
m= int(input("Introduzca otro numero entero : \n"))
cociente= n//m
resto= n%m
print("El resultado de la division entre",str(n),"y",str(m),"es:")
print("Cociente: ",str(cociente))
print("Resto: ",str(resto))