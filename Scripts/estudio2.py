#Análisis exploratorio con Python:

import pandas as pd 

dataframe = pd.read_csv("city_air_quality_AQI.csv")

print(dataframe)


#Calcular promedios mensuales de cada contaminante.

#son 6 contaminantes 

#vamos a calcular para Enero de 2024 PM2.5, tenemos q hacer un filtro de 2024-01-01 y 2024-01-31 y PM2.5

#mask = (dataframe['Date'] >= '2024-01-01') & (dataframe['Date'] <= '2024-01-31')

dataframe_filtrado = (dataframe['Date'] >= '2024-01-01') & (dataframe['Date'] <= '2024-01-31')  & (dataframe['City'] == 'Buenos Aires')

print(dataframe.loc[dataframe_filtrado])


#Analizar correlación entre temperatura, humedad y contaminación.

#Determinar qué ciudades superan los niveles recomendados por la OMS.


