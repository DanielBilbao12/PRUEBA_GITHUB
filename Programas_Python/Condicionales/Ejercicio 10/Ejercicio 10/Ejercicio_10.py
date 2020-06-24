#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. 
#Los ingredientes para cada tipo de pizza aparecen a continuación.
#Ingredientes vegetarianos: Pimiento y tofu.
#Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, 
#y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. 
#Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. 
#Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y 
#todos los ingredientes que lleva.

print("Responda con un 'si' o un 'no'")
pregunta= str(input("Hola, ¿Desea una pizza vegetariana?\n"))
while pregunta.upper() != "SI" and pregunta.upper() != "NO" :
    print("ERROR, responda con un 'si' o un 'no'")
    pregunta=str(input("¿Desea una pizza vegetariana?\n"))
if pregunta.upper() == "SI" :
    print("Tenga en cuenta que solo puede añadir uno de los siguientes ingredientes además de la mozzarella y el tomate que estan en todas las pizzas")
    print("Los ingredientes disponibles para su pizza son los siguientes: Pimiento y Tofu.")
    ingrediente= str(input("Introduzca el nombre del ingrediente que desea añadirle: \n"))
    while ingrediente.upper() != "PIMIENTO" and ingrediente.upper() != "TOFU" :
        print("ERROR, introduzca el nombre del ingrediente correctamente.")
        ingrediente= str(input("¿Cual es el ingrediente que desea añadirle?: \n"))
    print("La pizza que ha elegido es VEGETARIANA y lleva los siguientes ingredientes: Mozzarella, tomate y",str(ingrediente))
else :
    print("Tenga en cuenta que solo puede añadir uno de los siguientes ingredientes además de la mozzarella y el tomate que estan en todas las pizzas")
    print("Los ingredientes disponibles para su pizza son los siguientes: Peperoni, Jamón y Salmón.")
    ingrediente= str(input("Introduzca el nombre del ingrediente que desea añadirle: \n"))
    while ingrediente.upper() != "PEPERONI" and ingrediente.upper() != "JAMON" and ingrediente.upper() != "SALMON" :
        print("ERROR, introduzca el nombre del ingrediente correctamente.")
        ingrediente= str(input("¿Cual es el ingrediente que desea añadirle?: \n"))
    print("La pizza que ha elegido NO es VEGETARIANA y lleva los siguientes ingredientes: Mozzarella, tomate y",str(ingrediente))

