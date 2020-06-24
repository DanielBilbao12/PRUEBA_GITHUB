#En una determinada empresa, sus empleados son evaluados al final de cada año. 
#Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, 
#traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 
#0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. 
#A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. 
#La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.
#Nivel	Puntuación
#Inaceptable	0.0
#Aceptable	0.4
#Meritorio	0.6 o más
#Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, 
#así como la cantidad de dinero que recibirá el usuario.

puntos= float(input("Introduzca su puntuacion en la empresa: \n"))
while (puntos> 0.0 and puntos< 0.4) or (puntos>0.4 and puntos<0.6) :
    print("ERROR, puntuacion no valida!")
    puntos= float(input("Introduzca su puntuacion en la empresa: \n"))
if puntos == 0.0 :
    print("Su nivel de rendimiento es INACEPTABLE.")
    print("Usted recibirá 0 euros.")
elif puntos == 0.4 :
    print("Su nivel de rendimiento es ACEPTABLE.")
    dinero= float(puntos*2400.0)
    print("Usted recibirá ",str(dinero),"euros.")
elif puntos>=0.6 :
    print("Su nivel de rendimiento es MERITORIO.")
    dinero= float(puntos*2400.0)
    print("Usted recibirá ",str(dinero),"euros.")
