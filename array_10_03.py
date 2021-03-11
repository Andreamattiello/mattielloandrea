import numpy
x= (input("Scrivi un numero:"))
y= (input("Scrivi un numero:"))
z= (input("Scrivi un numero:"))
a= (input("Scrivi un numero:"))
b= (input("Scrivi un numero:")) 
lista=[x,y,z,a,b]
x=numpy.array(lista)
print(lista)
lista.sort()
print (lista)
lista.reverse()
print(lista)

