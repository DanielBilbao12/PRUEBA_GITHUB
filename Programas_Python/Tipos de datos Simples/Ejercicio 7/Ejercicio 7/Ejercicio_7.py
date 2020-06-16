#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora.
# Después debe mostrar por pantalla la paga que le corresponde.

horas=float(input("Introduza el numero de horas trabajadas (h): \n"))
coste= float(input("Introduzca el coste por hora (€): \n"))
print("Su paga correspondiente es de:",round(horas*coste,3), "€") #Uso de la funcion round() para redondear
