import pandas as pd #permite trabajar con excel
import numpy as np #para trabajar con matematicas
import random #generar numeros aleatorios
import copy

#cargamos los datos de consumos REALES
datosConsumoReal = pd.read_excel('data/input/ConsumoReal(MEDICAMENTOS)2022-2024.xlsx')
#cargamos los datos de PRECIOS de diferentes fuentes
datosPrecios = pd.read_excel('data/input/Precios(MEDICAMENTOS)2022-2024Completo.xlsx')
#cargo los datos del POA 2024
datosPoa = pd.read_excel('data/input/POA(IMEDICAMENTOS) 20242.xlsx')
#cargo los datos inventario
datosInventario = pd.read_excel('data/input/Inventarios.xlsx')

#PARAMETROS
# 1) TP: sumamos todo los registros de "TOTAL COSTO" de datosPOA
#TP = datosPoa["TOTAL COSTO"].sum()
TP = (datosPoa["CATIDAD A PEDIR"]*datosPrecios['Precio LINAME Junio 2024']).sum() #
print("Techo presupuestario TP = ",np.round(TP,2))
# 2) n: obtenemos la cantidad de variables en datosConsumoReal
n = datosConsumoReal.shape[0]

