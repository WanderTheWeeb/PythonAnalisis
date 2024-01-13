# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 07:56:08 2024

@author: TheLittleScout
"""
import os
import numpy as np
import matplotlib.pyplot as plt

def crear_estadisticas(tabla):
    tabla["P1"] = tabla["Ambiente"].apply(lambda x: 10 if x == "Excelente" else (8 if x == "Bueno" else (6 if x == "Regular" else 0)))
    tabla["P2"] = tabla["Participación"].apply(lambda x: 10 if x == "Siempre" else (8 if x == "Casi siempre" else (6 if x == "Pocas veces" else 0)))
    tabla["P3"] = tabla["Dudas"].apply(lambda x: 10 if x == "Siempre" else (8 if x == "Casi siempre" else (6 if x == "Pocas veces" else 0)))
    tabla["P4"] = tabla["Apoyo"].apply(lambda x: 10 if x == "Excelente" else (8 if x == "Bueno" else (6 if x == "Regular" else 0)))
    tabla["P5"] = tabla["Conocimiento"].apply(lambda x: 10 if x == "Excelente" else (8 if x == "Bueno" else (6 if x == "Regular" else 0)))
    tabla["P6"] = tabla["Correcciones"].apply(lambda x: 10 if x == "Siempre" else (8 if x == "Casi siempre" else (6 if x == "Pocas veces" else 0)))
    tabla["P7"] = tabla["Avisar"].apply(lambda x: 10 if x == "Siempre" else (8 if x == "Casi siempre" else (6 if x == "Pocas veces" else 0)))
    tabla["P8"] = tabla["Entrada"].apply(lambda x: 10 if x == "Siempre" else (8 if x == "Casi siempre" else (6 if x == "Pocas veces" else 0)))
    tabla["P9"] = tabla["Salida"].apply(lambda x: 10 if x == "Siempre" else (8 if x == "Casi siempre" else (6 if x == "Pocas veces" else 0)))
    tabla["P10"] = tabla["Clase_Español"].apply(lambda x: 10 if x == "Nunca" else (8 if x == "Pocas veces" else (6 if x == "Casi siempre" else 0)))
    tabla["P11"] = tabla["Programado"].apply(lambda x: 10 if x == "Sí" else (5 if x == "No" else 0))

    return tabla

def generar_estadisticas_por_maestro(resultados_por_maestro, carpeta_estadisticas):
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