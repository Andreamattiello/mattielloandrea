import numpy

from random import randint
numeri=""
for x in range(8):
    numeri= numeri + "," + str(randint(1,8))
lista=numeri.split(",")
lista.pop(0)
Vettore=numpy.array(lista)
print(lista)
numero_scelto=input("scegli un numero:")
volte=lista.count(numero_scelto)
print(volte)
