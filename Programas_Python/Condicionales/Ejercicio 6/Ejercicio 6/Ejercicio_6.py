#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
#El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. 
#Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

nombre=str(input("Introduzca su nombre: "))
sexo= str(input("Introduzca su sexo (Hombre o Mujer): "))
while sexo.upper()!= "HOMBRE" and sexo.upper()!= "MUJER" :
    print("ERROR!")
    sexo= str(input("Introduzca su sexo (Hombre o Mujer): "))
#********************GRUPO A***********************
if 