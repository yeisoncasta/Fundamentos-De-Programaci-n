# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 18:46:01 2021

@author: Yeison David Aguirre
"""

#Metodo de ordenamiento

# Crear lista y darle valores

listaBase=[34,12,45,2,37,60,34,8]

print("lista base: ",listaBase)
#ordenar la lista con una funcion de python
listaBase.sort()
print("lista base de ordenada Ascendente: ",listaBase)

#Ordenar la lista con una funcion de python
listaBase.sort(reverse=True)
print("lista base Ordenada Descendente: ",listaBase)

#==================================================
#funcion desarrollada por el programador
# Ordenamiento Burbuja Ascendente
print("funcion desarrollada por el programador")
print("FUNCIÓN DESARROLLADA POR EL PROGRAMADOR")
def ordenamientoBurbujaAscendente(unaLista):
    for numPasada in range(len(unaLista)-1,0,-1):
        for i in range(numPasada):
            if unaLista[i]>unaLista[i+1]:
                temp = unaLista[i]
                unaLista[i] = unaLista[i+1]
                unaLista[i+1] = temp
                
#============================================

#funcion desarrollada por el programador
# Ordenamiento Burbuja desendente
print("FUNCIÓN DESARROLLADA POR EL PROGRAMADOR")
def ordenamientoBurbujaDescendente(unaLista):
    for numPasada in range(len(unaLista)-1,0,-1):
        for i in range(numPasada):
            if unaLista[i]>unaLista[i+1]:
                temp = unaLista[i]
                unaLista[i] = unaLista[i+1]
                unaLista[i+1] = temp


unaLista = [54,26,93,17,77,31,44,55,20]
print("Lista Original: ", unaLista)

ordenamientoBurbujaDescendente(unaLista)
print("Lista de ordenamiento descendente:  "),unaLista

#============================================
print("FUNCIÓN DESARROLLADA POR EL PROGRAMADOR")
def ordenamientoBurbuja(unaLista,tipo):
    
#======= Fin del desarrollo de la funcion =========
unaLista = [54,26,93,17,77,31,44,55,20]
print("Lista Original: ", unaLista)

ordenamientoBurbuja(unaLista,tipo)
print("lista ordenada decendente: "),unaLista