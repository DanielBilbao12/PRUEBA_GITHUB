#Escribir un programa que realice la siguiente operación aritmética ((3+2)/(2⋅5))^2.

from fractions import Fraction #Uso del modulo Fraction
Operacion= ((3+2)/(2*5))**2 # Para elevar dos '*'
print ("El resultado de la operacion en numero es :",Operacion)
print ("El resultado de la operacion en fraccion es :", Fraction(Operacion))