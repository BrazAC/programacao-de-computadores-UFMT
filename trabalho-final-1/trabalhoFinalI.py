"""
Date: 17/09/2024
Authors:Braz Amorim Campos, Gregorio Tavares de Matos
Professor: Ivairton
Discipline: Introducao a programacao
Project: Trabalho final I
"""
import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing

import seaborn as sns
import matplotlib as plt

#-----------------------------------------------------------FIRST REQUIREMENT
#Getting the data base
housing = fetch_california_housing()

#Getting the mtx with the info
registers = housing.data[:, 0:8]

#Getting the atributes names
atributeNames = housing.feature_names[0:8]
#['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude']

#Creating the dataFrame with atributeNames as columns and registers as the mtx
registers_df = pd.DataFrame(registers, columns=atributeNames)
print(registers_df)
#Creating the describe() dataFrame
registersDes_df = registers_df.describe()

#-----------------------------------------------------------SECOND REQUIREMENT
#Set the theme
sns.set_theme()

#Plot the desired data 
sns.relplot(data=registers_df, x="Latitude", y="Longitude")

#Show the graphic
#plt.pyplot.show()

#------------------------------------------------------------THIRD REQUIREMENT
#Getting the target atribute names
atributeNames0_6 = housing.feature_names[0:6]

#->Calculating the info
tempVetor = [0]*len(atributeNames0_6)
infoVector = []

#Media
for i in range(6):
    tempVetor[i] = registers_df[atributeNames0_6[i]].mean()
infoVector.append(tempVetor.copy())

#Mediana
for i in range(6):
    tempVetor[i] = registers_df[atributeNames0_6[i]].median()
infoVector.append(tempVetor.copy())

#Moda
moda = registers_df[atributeNames0_6[0:6]].mode(dropna=False)

#Variancia
for i in range(6):
    tempVetor[i] = registers_df[atributeNames0_6[i]].var()
infoVector.append(tempVetor.copy())

#Desvio padrao
for i in range(6):
    tempVetor[i] = registers_df[atributeNames0_6[i]].std()
infoVector.append(tempVetor.copy())

#Quantis
quantisVec = []
for i in range(6):
    Q1 = registers_df[atributeNames0_6[i]].quantile(0.25)
    Q2 = registers_df[atributeNames0_6[i]].quantile(0.5)
    Q3 = registers_df[atributeNames0_6[i]].quantile(0.75)
    quantisVec.append([Q1, Q2, Q3])
quantis_df = pd.DataFrame(quantisVec, index = atributeNames0_6, columns = ["1o quartil", "2o quartil", "3o quartil"])

#IQR
IQR = Q3 - Q1

#Creating info_df with other results
operations = ['Média', 'Mediana', 'Variância', 'Desvio padrão']
info_df = pd.DataFrame(infoVector, columns = atributeNames0_6, index = operations)

"""#Mostrando tabelas/Dados que não puderam entrar em infoVector
print("\nModas:\n", moda)
print("\nQuantis:\n", quantis_df)
print("\nIntervalo interquartil =", IQR)

#Showing the infoVector
print("\nOther info:")
print(info_df)"""

#------------------------------------------------------------FOURTH REQUIREMENT
#Plot the desired data
for i in range(len(atributeNames)):
    sns.boxplot(data=registers_df[atributeNames[i]], orient="h")
    plt.pyplot.show()