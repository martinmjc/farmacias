import pandas as pd #permite trabajar con excel
import numpy as np #para trabajar con matematicas
import random #generar numeros aleatorios
import copy
from src.funciones import calculo_fitness

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
# 3) m: obtenemos la cantidad de enfermedades

# Ejemplo minimo de uso de la funcion objetivo de compras
w_ejemplo = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
x_ejemplo = np.array([[[2, 1], [0, 3]], [[4, 2], [1, 5]]])
PRA_ejemplo = np.array([[10, 20], [30, 40]])
PRE_ejemplo = np.array([[1, 2], [3, 4]])
fitness_ejemplo = calculo_fitness(w_ejemplo, x_ejemplo, PRA_ejemplo, PRE_ejemplo)
print("Fitness ejemplo = ", fitness_ejemplo)
