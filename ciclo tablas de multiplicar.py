# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 18:52:57 2021

@author: Yeison David Aguirre
"""

#Programa que lee una tabla, la imprime del 1 hasta el 20 y suma los resutados

#Declarar varibles

Tabla=0
multiplicador= 1
Resultado= 0
Sumaderesultado= 0
conRepCiclo= 1

#Leer el numero de la tabla para la cual vamos ha realizar las operaciones

Tabla= int(input("tabla: "))
#leer el multiplicador
multiplicador= int(input("Multiplicador: "))

#inico de ciclo repetitivo WHILE
for conRepCiclo in range (5,15):
        Resultado= Tabla*conRepCiclo
        Sumaderesultado= Sumaderesultado + Resultado
        print(tabla," * ", conRepCiclo, "= ", resultado
              # Incrementar la variable que controla el ciclo
              # Se imprime la suma por fuera del ciclo
print ("la suma de los resultado es: ", Sumaderesultado)