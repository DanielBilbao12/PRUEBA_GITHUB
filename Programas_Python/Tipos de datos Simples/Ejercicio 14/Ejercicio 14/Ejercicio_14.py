# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. 
# Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual 
# de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.

PrecioBarra=float(3.49)
PanViejo= float(0.6)
VendidasVejas=int(input("Introduzca el numero de barras vendidas que no son del dia: \n"))
print("El precio habitual de una barra es de: ",str(PrecioBarra),"€")
print("El descuento que se hace por no ser fresca es del 60%")
CosteBarras=float(PrecioBarra*VendidasVejas)
CosteTotal=float(CosteBarras-(CosteBarras*PanViejo))
print("El coste de las barras de pan que ha comprado es de: ",str(round(CosteTotal,2)))