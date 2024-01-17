# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 07:56:08 2024

@author: TheLittleScout
"""
from io import BytesIO
import matplotlib.pyplot as plt
import numpy as np


def crear_estadisticas(tabla):
    tabla["P1"] = tabla["Ambiente"].apply(
        lambda x: 10 if x == "Excelente" else (8 if x == "Bueno" else (6 if x == "Regular" else 0)))
    tabla["P2"] = tabla["Participación"].apply(
        lambda x: 10 if x == "Siempre" else (8 if x == "Casi siempre" else (6 if x == "Pocas veces" else 0)))
    tabla["P3"] = tabla["Dudas"].apply(
        lambda x: 10 if x == "Siempre" else (8 if x == "Casi siempre" else (6 if x == "Pocas veces" else 0)))
    tabla["P4"] = tabla["Apoyo"].apply(
        lambda x: 10 if x == "Excelente" else (8 if x == "Bueno" else (6 if x == "Regular" else 0)))
    tabla["P5"] = tabla["Conocimiento"].apply(
        lambda x: 10 if x == "Excelente" else (8 if x == "Bueno" else (6 if x == "Regular" else 0)))
    tabla["P6"] = tabla["Correcciones"].apply(
        lambda x: 10 if x == "Siempre" else (8 if x == "Casi siempre" else (6 if x == "Pocas veces" else 0)))
    tabla["P7"] = tabla["Avisar"].apply(
        lambda x: 10 if x == "Siempre" else (8 if x == "Casi siempre" else (6 if x == "Pocas veces" else 0)))
    tabla["P8"] = tabla["Entrada"].apply(
        lambda x: 10 if x == "Siempre" else (8 if x == "Casi siempre" else (6 if x == "Pocas veces" else 0)))
    tabla["P9"] = tabla["Salida"].apply(
        lambda x: 10 if x == "Siempre" else (8 if x == "Casi siempre" else (6 if x == "Pocas veces" else 0)))
    tabla["P10"] = tabla["Clase_Español"].apply(
        lambda x: 10 if x == "Nunca" else (8 if x == "Pocas veces" else (6 if x == "Casi siempre" else 0)))
    tabla["P11"] = tabla["Programado"].apply(lambda x: 10 if x == "Sí" else (5 if x == "No" else 0))

    return tabla


def generar_estadisticas_por_maestro(resultados_por_maestro):
    estadisticas_por_maestro = []

    colores = ['#31AB58', '#15539E'] * 6

    for index, row in resultados_por_maestro.iterrows():
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

        # Almacenar la figura en la lista
        estadisticas_por_maestro.append(plt.gcf())

        plt.close()

    return estadisticas_por_maestro


def plot_to_image(plt):
    image_stream = BytesIO()
    plt.savefig(image_stream, format='png')
    image_stream.seek(0)
    return image_stream


preguntas = [
    "El ambiente de trabajo y la interacción en clase promovidos han sido:",
    "El docente impulsa la participación de los estudiantes durante las clases para mejorar el aprendizaje:",
    "¿El docente apoya y aclara dudas cuando se le solicita?",
    "¿En qué nivel de calidad el apoyo y las clases brindados te permiten mejorar tu aprendizaje?",
    "En tu opinión, ¿Cuál es el nivel de conocimiento y dominio del idioma que demuestra el docente?",
    "¿El docente lee, revisa y devuelve los trabajos y tareas solicitados con observaciones que te permite "
    "corregir tus errores?",
    "¿El docente avisa a los alumnos en caso de no atender la clase en el horario programado?",
    "¿El docente es puntual en su horario de clase programado?",
    "¿El horario que el docente imparte la clase coincide con el horario programado?",
    "¿Con qué frecuencia el docente imparte la clase en español?",
    "¿Te gustaría recibir otro curso con el mismo docente?"
]