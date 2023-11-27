# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 11:22:50 2023

@author: MarcoJimenezRodrigue
"""
import random
import datetime as dt

def current_date():
    current_date = dt.date.today()
    # Extract the year and month from the current date
    year = current_date.year
    month = current_date.strftime('%m')
    # Create the formatted string
    formatted_date = f"{year}{month}"
    return formatted_date

def generar_pass(semilla):
    # Establece una semilla para el generador de números aleatorios
    random.seed(semilla)

    # Caracteres permitidos en la contraseña
    caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"

    # Longitud de la contraseña deseada
    longitud = 8  # Puedes ajustar esta longitud según tus necesidades

    # Genera la contraseña aleatoriamente
    contrasena = "".join(random.choice(caracteres) for _ in range(longitud))

    return contrasena


# print(generar_pass(current_date()))