# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 07:42:38 2024

@author: TheLittleScout
"""

import os

import pandas as pd

from CrearEstadisticas import crear_estadisticas, generar_estadisticas_por_maestro

carpeta_estadisticas = 'Estadisticas'
os.makedirs(carpeta_estadisticas, exist_ok=True)

df = pd.read_csv("EvaDoc_202351.csv")
dfConEstadisticasCuantificadas = crear_estadisticas(df)
dfConEstadisticasCuantificadas = dfConEstadisticasCuantificadas.drop('Marca temporal', axis=1)

columnas_relevantes = ['Docente', 'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P10', 'P11']
df_con_estadisticas = df[columnas_relevantes]

resultados_por_maestro = df_con_estadisticas.groupby(
    "Docente").mean()  # Se obtienen los promedios y se agrupa por docente
resultados_por_maestro = resultados_por_maestro.reset_index()  # Los maestros vuelven a ser Columna
resultados_por_maestro = resultados_por_maestro.round(2)  # Se redondean los promedios a 2 decimales
resultados_por_maestro.to_csv("Resultados.csv", index=False)  # Se guardan los resultados en un archivo csv

generar_estadisticas_por_maestro(resultados_por_maestro, carpeta_estadisticas)

