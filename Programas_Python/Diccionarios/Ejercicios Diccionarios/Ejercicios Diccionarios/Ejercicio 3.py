#Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, 
#pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. 
#Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

diccionario= {'Platano':1.35,'Manzana':0.80,'Pera':0.85,'Naranja':0.70}
fruta=str(input("Introduzca una fruta: ")).title()
while not fruta.isalpha() :
    print("ERROR, ESCRIBE BIEN, NO UTILIZES NUMEROS NI CARACTERES")
    fruta=str(input("Introduzca una fruta: ")).title()
kilos= float(input("Introduzca la cantidad de kilos de "+str(fruta)+" que desea: "))
if fruta in diccionario :
    print(kilos,"kilos de",fruta,"valen",diccionario[fruta]*kilos)
else :
    print("LO SIENTO, LA FRUTA QUE HAS PEDIDO NO ESTA DISPONIBLE")