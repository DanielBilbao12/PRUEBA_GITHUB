#Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
#los almacene en una lista y los muestre por pantalla ordenados de menor a mayor

lista=[]
cantidad=str(input("Introduce la cantidad de numeros de loteria que desea ordenar de menor a mayor: "))
while not cantidad.isnumeric() :
    print("ERROR. La cantidad de numeros de loteria tiene que ser un numero entero positivo!")
    cantidad=str(input("Introduce la cantidad de numero de loteria que desea ordenar de mayor a menor: "))
for i in range(int(cantidad)) :
    lista.append(int(input("Introduce el "+str(i+1)+". numero de la loteria primitiva: ")))
lista.sort() #Funcion que ordena la lista, igual que en c#, deja la lista ordenada de MENOR a MAYOR
print("Los numeros que has introducido ordenados son los siguientes:")
print(str(lista))