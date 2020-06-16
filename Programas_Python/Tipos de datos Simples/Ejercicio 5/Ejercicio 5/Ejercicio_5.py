#Escribir un programa que pregunte el nombre del usuario en la consola y 
#después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> 
#letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.

Nombre = str(input("Introduzca su nombre: \n"))
NumeroLetras= len(Nombre) #Metodo len() que obtiene el numero de elementos en un contenedor
print (Nombre.upper(),"tiene",NumeroLetras,"letras") #Metodo upper() que convierte los caracteres de un string a MAYUSC

