# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#entrada de informacion
var_ent_producto=int(input("digite valor del producto: "))
print ("valor del producto es: ", var_ent_producto)
#proceso
var_ent_producto_coniva = var_ent_producto*1.19
var_ent_descuento = var_ent_producto*1.19-0.5
#salida
print("valor prodcto con iva:  ", var_ent_producto_coniva)
print("valor total con descuento:  ", var_ent_descuento)
