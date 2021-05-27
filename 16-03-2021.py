# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 19:11:30 2021

@author: Yeison David Aguirre
"""

#Factura de venta

def f_titulo():
    print("calculo valor factura")
    
def f_despedida():
    print("..... ADIOS ...")
    
def f_valorfactura():  #encabezado de la funcion
    #desarrollo de la funcion
    #definicion de la funcion
    # Definicion de variables
    ve_nomArt = ""
    ve_canArt = 0
    ve_valUniArt= 0.0
    cons_porIva= 0.19
    vps_netPag=0.0
    vps_ivaPag=0.0
    vps_totPag=0.0

# Entrada de datos
    ve_nomArt = input("Articulo: ")
    ve_canArt = int(input("Cantidad: "))
    ve_valUniArt = float(input("Valor Unitario: "))

# Procesos
    vps_netPag=ve_canArt * ve_valUniArt
    vps_ivaPag=vps_netPag * cons_porIva
    vps_totPag=vps_netPag + vps_ivaPag

# Salidas
    print( "Neto: ", vps_netPag)
    print( "Iva: ", vps_ivaPag)
    print( "Total: ",vps_totPag)
    
#llamado a la funcion

f_titulo()
f_valorfactura()
f_despedida()