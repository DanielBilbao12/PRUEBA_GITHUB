#Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y 
#muestre por pantalla su media y desviación típica.

numeros= input("Introduzca una muestra de numeros separados por comas: ")
numeros=numeros.split(',') #Metodo para convertir unos datos de entrada separados por un caracter especifico en una lista, y si se quiere luego a tupla como siempre
for i in range(len(numeros)) :
    numeros[i] = int(numeros[i])
numeros=tuple(numeros)
suma=0
for i in range(len(numeros)) :
    suma += numeros[i]
media=float(suma/len(numeros))
print("La media de la muestra introducida es de:",str(media))
distmedia=0
for i in range(len(numeros)) :
    distmedia += (numeros[i]-media)**2
desbtipica=float((distmedia/len(numeros))**(1/2))
print("La desviacion estandar de la muestrra es de: ",str(desbtipica))