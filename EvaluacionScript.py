# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 07:42:38 2024

@author: TheLittleScout
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from CrearEstadisticas import crear_estadisticas


df = pd.read_csv("EvaDoc_202351.csv")
dfConEstadisticasCuantificadas = crear_estadisticas(df)
dfConEstadisticasCuantificadas = dfConEstadisticasCuantificadas.drop('Marca temporal', axis=1)


columnas_relevantes = ['Docente', 'P1', 'P2','P3','P4','P5','P6','P7','P8','P9','P10','P11']
df_con_estadisticas = df[columnas_relevantes]

resultados_por_maestro = df_con_estadisticas.groupby("Docente").mean() #Se obtienen los promedios y se agrupa por docente
resultados_por_maestro = resultados_por_maestro.reset_index() #Los maestros vuelven a ser Columna


plt.figure(figsize=(12, 8))

# Obtener el nombre del maestro y las calificaciones para la primera fila
maestro = df.loc[0, 'Docente']
calificaciones = df.loc[0, 'P1':'P11']

colores = ['#31AB58', '#15539E', '#31AB58', '#15539E', '#31AB58', '#15539E', '#31AB58', '#15539E', '#31AB58', '#15539E', '#31AB58']

# Graficar un gráfico de barras para las calificaciones
plt.bar(calificaciones.index, calificaciones, color=colores)

# Configurar el diseño del gráfico
plt.title(f'Evaluacion Docente: {maestro}')
plt.xlabel('Preguntas')
plt.ylabel('Promedio')

# Rotar los nombres de los periodos para mejorar la legibilidad
plt.xticks(rotation=45, ha='right')

# Mostrar el gráfico de barras
plt.show()