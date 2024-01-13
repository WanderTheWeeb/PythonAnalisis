# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 07:56:08 2024

@author: TheLittleScout
"""

import matplotlib as plt


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




#%%
