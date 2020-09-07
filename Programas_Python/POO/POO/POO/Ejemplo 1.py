# Creacion de una clase
#NOTA: EL ARGUMENTO SELF ES PARA QUE LA INSTANCIA DEL OBJETO PUEDA USAR EL METODO

class Humano :
    #METODO CONSTRUCTOR--> Aqui declaramos los atributos de la clase
    def __init__(self,edad): #Se le ponen las barras bajas porke python lo reconoce y cuando se cree un objeto hace de constructor
        self.edad=edad
        print("SOY UN NUEVO HUMANO")
    #METODOS DE LA CLASE
    def hablar(self, mensaje):
        print(mensaje)
#Instancias de la clase humano--> Creacion de objetos
pedro = Humano(26)
raul= Humano(18)
pedro.hablar("HOLA! Soy Pedro y tengo "+str(pedro.edad)+" años")
raul.hablar("Hola Pedro... yo tengo "+str(raul.edad)+" años")


