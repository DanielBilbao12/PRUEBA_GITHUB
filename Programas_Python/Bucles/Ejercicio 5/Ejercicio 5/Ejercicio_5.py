#Escribir un programa que pregunte al usuario una cantidad a invertir, 
#el interés anual y el número de años, y muestre por pantalla el capital obtenido en la 
#inversión cada año que dura la inversión.

inversion= float (input("Introduzca una cantidad de euros a ivertir: "))
inversion2=inversion
interes= float(input("Introduzca el interes anual: "))
años= int(input("Introduzca el numero de años de la inversion: "))
for i in range(años) :
    #inversion = inversion*(1+interes/100)
    inversion2 *= 1+ interes/100
    #print("El capital tras ",str(i+1),"años:",str(round(inversion,2)))
    print("El capital tras ",str(i+1),"años:",str(round(inversion2,2)))
#El operador *= al igual que += o -= hace la operacion que se pide de la misma manera que lo comentado