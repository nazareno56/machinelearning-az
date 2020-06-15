#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 13:19:06 2019

@author: juangabriel
"""

# Plantilla de Pre Procesado - Datos Categóricos

# Cómo importar las librerías
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importar el data set
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

# Codificar datos categóricos
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import make_column_transformer

labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0]) # se encarga de transformar a datos numericos

# Generar variables dummys, columnas que llevan un 0 False, 1 True
onehotencoder = make_column_transformer((OneHotEncoder(), [0]), # The column numbers to be transformed (here is [0] but can be [0, 1, 3])
                                        remainder = "passthrough") # Leave the rest of the columns untouched
X = onehotencoder.fit_transform(X).astype('float64') 


labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)