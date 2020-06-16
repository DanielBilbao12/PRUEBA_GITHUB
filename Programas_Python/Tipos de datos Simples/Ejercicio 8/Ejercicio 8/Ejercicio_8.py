#Escribir un programa que lea un entero positivo, 𝑛, introducido por el usuario y después muestre en 
#pantalla la suma de todos los enteros desde 1 hasta 𝑛.
# La suma de los 𝑛 primeros enteros positivos puede ser calculada de la siguiente forma: (Formula en la web)

entero =int(input("Introduzca un numero entero: \n"))
sumatodos= (entero *(entero+1))/2
print ("La suma de los 'n' primeros enteros positivos del numero que has introducido es: ",sumatodos)