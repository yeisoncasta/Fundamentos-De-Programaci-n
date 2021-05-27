# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 18:48:15 2021

@author: Yeison David Aguirre
"""

#programa que calcula la nota de un estudiante

#entradas
#pedir las 3 notas de estudiante y sus parciales

canEst=int(input("cantidad de estudiantes: "))
#iniar la variable que controla el ciclo
conRep=0
#variable real para sumar las definitivas del grupo
#variable para calcular las notas promedio del grupo
while(conRep< canEst):
    
#instrucciones a repetir
    nomEst= input("nombre de estudiante: ")
    notUnoEst= float(input("parcial uno: "))
    notDosEst= float(input("parcial dos: "))
    notTresEst= float(input("parcial tres: "))

#calculos
notDefEst = (notUnoEst+notDosEst+notTresEst)/3

#imprimir resultados - salidas
print(f"La nota definitiva es: {notDefEst:.1f}")

#incrementar variable que controla el ciclo
conRep=conRep+1