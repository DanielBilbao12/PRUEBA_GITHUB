# Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'},
#  pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

diccionario= {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
divisa= input("Introduce una divisa: ")
print(diccionario.get(divisa.title(),"LA DIVISA INTRODUCIA NO FORMA PARTE DEL DICCIONARIO PREDEFINIDO"))