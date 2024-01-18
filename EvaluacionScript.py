# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 07:42:38 2024

@author: TheLittleScout
"""
import os

import pandas as pd
from pylatex import Document, Section, NoEscape, Figure, NewPage, Tabularx

from CrearEstadisticas import crear_estadisticas, generar_estadisticas_por_maestro, preguntas

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

estadisticas_lista = generar_estadisticas_por_maestro(resultados_por_maestro)

for i, estadistica in enumerate(estadisticas_lista):
    nombre_archivo = f'{resultados_por_maestro.iloc[i]["Docente"]}.png'
    estadistica.savefig(os.path.join(carpeta_estadisticas, nombre_archivo))

doc = Document(geometry_options={'margin': '1in', 'width': '8.5in'})
doc.preamble.append(NoEscape(r'\usepackage[utf8]{inputenc}'))
doc.preamble.append(NoEscape(r'\usepackage[spanish]{babel}'))
doc.preamble.append(NoEscape(r'\usepackage{graphicx}'))

for i, estadistica in enumerate(estadisticas_lista):
    nombre_maestro = resultados_por_maestro.iloc[i]["Docente"]
    P1 = resultados_por_maestro.iloc[i]["P1"]
    P2 = resultados_por_maestro.iloc[i]["P2"]
    P3 = resultados_por_maestro.iloc[i]["P3"]
    P4 = resultados_por_maestro.iloc[i]["P4"]
    P5 = resultados_por_maestro.iloc[i]["P5"]
    P6 = resultados_por_maestro.iloc[i]["P6"]
    P7 = resultados_por_maestro.iloc[i]["P7"]
    P8 = resultados_por_maestro.iloc[i]["P8"]
    P9 = resultados_por_maestro.iloc[i]["P9"]
    P10 = resultados_por_maestro.iloc[i]["P10"]
    P11 = resultados_por_maestro.iloc[i]["P11"]
    ruta_imagen = f'{carpeta_estadisticas}/{nombre_maestro}.png'

    with doc.create(Section('', numbering=False)):
        doc.append(NoEscape(r'\centering\Large'))
        doc.append(f'Evaluación Docente: {nombre_maestro}')

        with doc.create(Figure(position='h!')) as fig:
            fig.append(NoEscape(r'\centering'))
            fig.add_image(ruta_imagen, width=NoEscape(r'0.9\textwidth'))

        doc.append(NoEscape(r'\small'))
        with doc.create(Tabularx('X|c', width_argument=NoEscape(r'\textwidth'))) as table:
            table.add_hline()
            table.add_row(["Pregunta", "Promedio"], color="lightgray")
            table.add_row([preguntas[0], P1])
            table.add_row([preguntas[1], P2])
            table.add_row([preguntas[2], P3])
            table.add_row([preguntas[3], P4])
            table.add_row([preguntas[4], P5])
            table.add_row([preguntas[5], P6])
            table.add_row([preguntas[6], P7])
            table.add_row([preguntas[7], P8])
            table.add_row([preguntas[8], P9])
            table.add_row([preguntas[9], P10])
            table.add_row([preguntas[10], P11])

        doc.append(NewPage())

# Generar código LaTeX y guardar en un archivo
doc.generate_tex('Evaluacion.tex')

# Generar un archivo PDF
doc.generate_pdf("Evaluacion", clean_tex=True, clean=True)
print("Se ha generado el archivo PDF")

# %%
