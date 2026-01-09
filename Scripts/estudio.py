import pandas as pd 

dataframe = pd.read_csv("city_air_quality.csv")

dataframe_2 = pd.read_csv("tablaEPA.csv")

print(dataframe.info())

print('--------------------------------------------')

print(dataframe.head())

#Eliminar filas desde 367 en adelante

dataframe.drop(dataframe.index[365:], inplace=True)

print(dataframe.info())



# Asegurarse de que las fechas estén en formato datetime.

dataframe['Date'] = pd.to_datetime(dataframe['Date'])

# Eliminar outliers en concentraciones de gases.

# Crear un índice de calidad del aire (AQI simplificado).

print(dataframe_2)

dataframe.to_csv("city_air_quality_.csv")

