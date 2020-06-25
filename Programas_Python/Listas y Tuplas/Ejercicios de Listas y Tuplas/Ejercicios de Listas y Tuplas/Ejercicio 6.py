#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
#en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. 
#Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.

asignaturas= ["Matematicas", "Fisica", "Quimica", "Historia", "Informatica"]
notas=[]
for i in asignaturas :
    nota=str(input("Introduzca la nota de "+i+":"))
    while not nota.isnumeric() and (float(nota) <0.0 or float(nota)>10.0): #ERROR AQUI
        print("ERROR. la nota tiene que ser un valor numerico positivo entre 0 y 10!")
        nota=str(input("Introduzca la nota de "+i+":"))
    notas.append(float(nota))
for i in range(len(notas)-1,-1,-1):
    if notas[i] >= 5.0 :
        asignaturas.remove(asignaturas[i])
print("Las asignaturas a repetir son las siguientes:")
print(asignaturas)