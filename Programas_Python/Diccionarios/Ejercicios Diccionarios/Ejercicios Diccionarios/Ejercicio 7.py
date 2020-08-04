#Escribir un programa que cree un diccionario simulando una cesta de la compra. 
#El programa debe preguntar el artículo y su precio y añadir el par al diccionario, 
#hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, 
#con el siguiente formato

cesta={}
fin= False
preciototal=0
while fin == False :
    articulo=str(input("Introduzca el articulo que desea meter a su cesta: "))
    precio=str(input("Introduzca el precio del articulo "+str(articulo.upper())+":"))
    cesta[articulo.title()]=float(precio)
    salir=str(input("Desea seguir metiendo cosas a la cesta? (SI/NO):"))
    while salir.upper()!="SI" and salir.upper()!="NO" :
        print("ERROR. RESPONDA CON 'SI' O 'NO'")
        salir=str(input("Desea seguir metiendo cosas a la cesta? (SI/NO):"))
    if salir.upper()=="SI" :
        fin= False
    else :
        fin= True
for i,j in cesta.items() :
    preciototal+=j
cesta["Coste Total (€)"]=preciototal
print("La cesta contiene los siguientes articulos:")
print(cesta)