# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 07:42:38 2024

@author: TheLittleScout
"""

import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt
from CrearEstadisticas import crear_estadisticas

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

# Definir colores para las barras
colores = ['#31AB58', '#15539E'] * 6

for index, row in resultados_por_maestro.iterrows():
    # Obtener el nombre del maestro y las calificaciones para la fila actual

    maestro = row['Docente']
    calificaciones = row['P1':'P11']

    plt.figure(figsize=(12, 8))
    plt.bar(calificaciones.index, calificaciones, color=colores, edgecolor='black', linewidth=1.2)
    plt.title(f'Evaluacion Docente: {maestro}', fontsize=18, pad=20)
    plt.xlabel('Preguntas', fontsize=14)
    plt.ylabel('Promedio', fontsize=14)
    plt.ylim(0, 10)
    plt.yticks(np.arange(0, 11, 1))
    plt.xticks(rotation=45, ha='right')

    # Guardar la imagen en la carpeta "Estadisticas" con un nombre único
    plt.tight_layout()
    ruta_guardado = os.path.join(carpeta_estadisticas, f'{maestro}_Estadistica.png')
    plt.savefig(ruta_guardado)

    # Cerrar la figura para liberar recursos
    plt.close()