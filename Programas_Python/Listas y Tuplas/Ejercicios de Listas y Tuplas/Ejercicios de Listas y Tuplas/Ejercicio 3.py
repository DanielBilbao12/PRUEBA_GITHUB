#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
#pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> 
#donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.

asignaturas= ["Matematicas", "Fisica", "Quimica", "Historia", "Informatica"]
notas=[]
for i in asignaturas :
    nota=float(input("Introduzca la nota de "+i+":"))
    notas.append(nota)
print("")
for i in range(len(notas)) :
    print("Tu nota en",str(asignaturas[i]),"es de",str(notas[i]))