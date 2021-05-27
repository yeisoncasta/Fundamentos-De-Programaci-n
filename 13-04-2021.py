# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 19:26:29 2021

@author: Yeison David Aguirre
"""

# Practica_ con Arreglos-vector

# Almacenar en un vecros 5 notas del parcial

# Declarar el vector
listaNotas=[]
sumaNotas=0.0

# Asignar valor a la lista con ciclo
for porLista in range(5):
    #leer desde teclado la nota
    notaEst=float(input("Digite Nota:  "))
    sumaNotas=sumaNotas+notaEst
    #Almacenamos la escalar en el arreglo
    listaNotas.append(notaEst)
    
#  Imprimir el arreglo
print(listaNotas)
print("la suma de las notas es: "), sumaNotas

#================================