#DEFINIR UNA FUNCION
def print_lyrics ():
    print("la la la")
    print("le le le")
    return 4

#Donde esta definida la funcion (imprime un hexadecimal)
print(print_lyrics)

#Imprime la funcion
print(print_lyrics())

#Corre la funcion
print_lyrics()

#Imprimir el tipo del resultado de la funcion
print(type(print_lyrics()))

#Usar una funcion dentro de otra funcion
def repetir_lyrics ():
    print(print_lyrics())
    print(print_lyrics())

print(repetir_lyrics())

#Function with a parameter
def print_twice(x):
    print(x)
    print(x)

import math
print_twice(17)
print_twice("Spam"*4)
print_twice(math.cos(math.pi))

Hola="Helloooooo"
print_twice(Hola)

#Functions with a result
def addtwo(a, b):
    added = a+b
    return added

x = addtwo(5,7)
print(x)