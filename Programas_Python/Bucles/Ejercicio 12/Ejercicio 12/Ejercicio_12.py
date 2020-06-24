#Escribir un programa en el que se pregunte al usuario por una frase y una letra, 
#y muestre por pantalla el número de veces que aparece la letra en la frase.

frase= str(input("Introduzca una frase: "))
letra= str(input("Introduzca una letra: "))
kont=0
for i in range(len(frase)-1,-1,-1) :
    if frase[i].upper() == letra.upper() :
        kont=kont+1
print("La letra",str(letra),"aparece",str(kont),"veces en la frase que has introducido")
