"""
Date: 17/09/2024
Authors:Braz Amorim Campos, Gregorio Tavares de Matos
Professor: Ivairton
Discipline: Introducao a programacao
Project: Trabalho final I

ATENÇÃO: As linhas de código que mostram as informações no terminal estão comentadas e identificadas com: "<======== HERE"
"""
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

#Creating the dataFrame with atributeNames as columns, and registers as the mtx
registers_df = pd.DataFrame(registers, columns=atributeNames)

#Creating the describe() dataFrame
registersDes_df = registers_df.describe()
#print(registersDes_df) <======== HERE

#-----------------------------------------------------------SECOND REQUIREMENT
#Set the theme
sns.set_theme()

#Plot the desired data 
sns.relplot(data=registers_df, x="Longitude", y="Latitude")

#Show the graphic
#plt.pyplot.show()<======== HERE

#------------------------------------------------------------THIRD REQUIREMENT
#Getting the target atribute names
atributeNames0_6 = housing.feature_names[0:6]

#->Calculating the info
tempVetor = [0]*len(atributeNames0_6)
infoVector = []

#Mean
for i in range(6):
    tempVetor[i] = registers_df[atributeNames0_6[i]].mean()
infoVector.append(tempVetor.copy())

#Median
for i in range(6):
    tempVetor[i] = registers_df[atributeNames0_6[i]].median()
infoVector.append(tempVetor.copy())

#Mode
mode = registers_df[atributeNames0_6[0:6]].mode(dropna=False)

#Variance
for i in range(6):
    tempVetor[i] = registers_df[atributeNames0_6[i]].var()
infoVector.append(tempVetor.copy())

#Standard deviation
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
quantis_df = pd.DataFrame(quantisVec, index = atributeNames0_6, columns = ["1o quantile", "2o quantile", "3o quantile"])

#IQR
IQR = Q3 - Q1

#Creating the Data Frame: info_df, with other results
operations = ['Mean', 'Median', 'Variance', 'Standard deviation']
info_df = pd.DataFrame(infoVector, columns = atributeNames0_6, index = operations)

#Showing tables/data that could not get into infoVector <======== HERE
"""
print("-" * 87)
print("Modes:\n", mode)
print("-" * 87, end="")
print("\nQuantile:\n", quantis_df)
print("-" * 87, end="")
print("\nInterquartile range =", IQR)

#Showing the infoVector
print("-" * 87, end="")
print("\nOther info:")
print(info_df)
print("-" * 87)
"""
#------------------------------------------------------------FOURTH REQUIREMENT
#Plot the bloxPot  <======== HERE
"""
for i in range(len(atributeNames0_6)):
    sns.boxplot(data=registers_df[atributeNames0_6[i]], orient="h")
    plt.pyplot.show()

#Plot the histograma
for i in range(len(atributeNames0_6)):
    sns.histplot(data=registers_df[atributeNames0_6[i]], kde=True) 
    plt.pyplot.show()
"""

#------------------------------------------------------------FIFTH REQUIREMENT
#----->First Pair
#AveBedrms Skewness
AveBedrmsSkew = registers_df['AveBedrms'].skew()
#AveBedrms Kurtosis
AveBedrmsKurt = registers_df['AveBedrms'].kurtosis()

#AveRooms Skewness
AveRoomsSkew = registers_df['AveRooms'].skew()
#AveRooms Kurtosis
AveRoomsKurt = registers_df['AveRooms'].kurtosis()

#Creating and showing the data with a dataFrame
firstPairSkew_Df = pd.DataFrame([[AveBedrmsSkew, AveRoomsSkew], [AveBedrmsKurt, AveRoomsKurt]], ["Skewness", "Kurtosis"], ['AveBedrms', 'AveRooms'])
#print(firstPairSkew_Df, "\n")  <======== HERE

#----->Second Pair
#Population Skewness
PopulationSkew = registers_df['Population'].skew()
#Population Kurtosis
PopulationKurt = registers_df['Population'].kurtosis()

#HouseAge Skewness
HouseAgeSkew = registers_df['HouseAge'].skew()
#HouseAge Skewness
HouseAgeKurt = registers_df['HouseAge'].kurtosis()

#Creating and showing the data with a dataFrame
secondtPairSkew_Df = pd.DataFrame([[PopulationSkew, HouseAgeSkew], [PopulationKurt, HouseAgeKurt]], ["Skewness", "Kurtosis"], ['Population', 'HouseAge'])
#print(secondtPairSkew_Df)  <======== HERE