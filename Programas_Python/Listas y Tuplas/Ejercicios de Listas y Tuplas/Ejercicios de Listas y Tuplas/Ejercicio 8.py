#Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo/capicua

palabra=str(input("Introduzca una PALABRA para determinar si es palindromo/capicua: "))
while not palabra.isalpha() or palabra == "" :
    print("ERROR. La palabra que has introducido no es una palabra, LEE BIEN INUTIL")
    palabra=str(input("Introduzca una PALABRA para determinar si es palindromo/capicua: "))
lPalabra=palabra
palabra=list(palabra)
lPalabra=list(lPalabra)
lPalabra.reverse()
if palabra == lPalabra :
    print("LA PALABRA ES PALINDROMO/CAPICUA")
else :
    print("LA PALABRA NO ES PALINDROMO/CAPICUA")

##############################################################################################
#OTRA MANERA DE HACERLO SIN CONOCER EL METODO .reverse() ni la conversion a lista de un objeto
#palindromo=False
#indice=0
#for i in range(len(palabra)-1,-1,-1) :
 #   if palabra[indice]==palabra[i] :
  #      palindromo=True
   # else :
    #    palindromo=Falsegdsf
    #indice+=1
#if palindromo==True :
 #   print("LA PALABRA ES PALINDROMO/CAPICUA")
#else :
 #   print("LA PALABRA NO ES PALINDROMO/CAPICUA")