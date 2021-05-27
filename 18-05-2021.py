# -*- coding: utf-8 -*-
"""
Created on Tue May 18 18:50:00 2021

@author: Yeison David Aguirre
"""

import pandas as pd

# Leer archivo de excel
df_archivoExcel = pd.read_excel ('ventas_productos_1.xlsx',index_col="producto")
df_archivoExcel = df_archivoExcel [:10].copy()
print (df_archivoExcel)

# Grafica vertcal
df_archivoExcel.plot(kind = 'bar')

# Grafico horizontal
df_archivoExcel.plot(kind = 'barh')

# Ocupar todo el espacio
df_archivoExcel.plot(kind = 'barh', width=1)