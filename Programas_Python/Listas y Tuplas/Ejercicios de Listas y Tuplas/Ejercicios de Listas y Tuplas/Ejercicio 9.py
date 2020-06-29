#Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.

vocales= ["a","e","i","o","u"]
palabra= str(input("Introduce una PALABRA: "))
while not palabra.isalpha() or palabra == "" :
    print("ERROR.¡¡PALABRA PALABRA PALABRA PALABRA!!")
    palabra= str(input("Introduce una PALABRA: "))
for vocal in vocales :
    kont=0
    for letra in palabra :
        if letra == vocal :
            kont+=1
    print("La vocal", str(vocal),"aparece", str(kont)," veces en la palabra que has introducido")