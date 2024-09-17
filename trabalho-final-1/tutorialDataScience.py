"""
Exemplo DataFrame:
dataFrame = pd.DataFrame([[123, 432, 954, 234],[123, 432, 954, 234]], index=['janeiro', 'fevereiro'], columns=['Year', 'Semester', 'Bimester', 'month'])
print(dataFrame)
"""

import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris

#Carregando objeto com pares key:pair sobre as plantas
iris = load_iris()
#print(iris)

#Matriz com dados de tamanhos de cada planta
x = iris.data[:, 0:4]

#Matriz com espécie de cada planta
y = iris.target

# Criamos a lista com os nomes de cada atributo
feature_names = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
target_names = iris.target_names[0:3]

x_df = pd.DataFrame(x, columns=feature_names, index=range(1, len(x) + 1))
print(x_df)