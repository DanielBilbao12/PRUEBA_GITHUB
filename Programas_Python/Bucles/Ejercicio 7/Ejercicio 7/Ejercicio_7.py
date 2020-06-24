#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

#Mediante dos for se modifican los valores de tablas
for i in range(1,11) :
    for j in range (1,11) :
        print (i*j, end="\t") #Relleno las columnas y mediante el \t genero sangria
    print("") #Añado salto de linea a la siguiente fila
