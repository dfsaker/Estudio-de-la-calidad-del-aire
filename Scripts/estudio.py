import pandas as pd 

#Estudio Calidad de Aire

dataframe = pd.read_csv("city_air_quality.csv")

dataframe_2 = pd.read_csv("tablaEPA.csv")

print(dataframe.info())

print('--------------------------------------------')
 
print(dataframe.head())


# Asegurarse de que las fechas estén en formato datetime.

dataframe['Date'] = pd.to_datetime(dataframe['Date'])

# Eliminar outliers en concentraciones de gases.

# Crear un índice de calidad del aire (AQI simplificado).

print(dataframe_2)

dataframe.to_csv("city_air_quality_.csv")


import numpy as np

# 1. Cargar los datos
df = pd.read_csv('city_air_quality.csv')

# 2. Definir los puntos de corte (Breakpoints) para cada contaminante
# Estructura: (C_low, C_high, I_low, I_high)
breakpoints = {
    'PM2.5': [(0, 12, 0, 50), (12.1, 35.4, 51, 100), (35.5, 55.4, 101, 150), (55.5, 150.4, 151, 200), (150.5, 250.4, 201, 300)],
    'PM10':  [(0, 54, 0, 50), (55, 154, 51, 100), (155, 254, 101, 150), (255, 354, 151, 200), (355, 424, 201, 300)],
    'NO2':   [(0, 53, 0, 50), (54, 100, 51, 100), (101, 360, 101, 150), (361, 649, 151, 200), (650, 1249, 201, 300)],
    'SO2':   [(0, 35, 0, 50), (36, 75, 51, 100), (76, 185, 101, 150), (186, 304, 151, 200), (305, 604, 201, 300)],
    'CO':    [(0, 4.4, 0, 50), (4.5, 9.4, 51, 100), (9.5, 12.4, 101, 150), (12.5, 15.4, 151, 200), (15.5, 30.4, 201, 300)],
    'O3':    [(0, 54, 0, 50), (55, 70, 51, 100), (71, 85, 101, 150), (86, 105, 151, 200), (106, 200, 201, 300)]
}

# 3. Función para calcular sub-índice individual
def calcular_sub_indice(valor, contaminante):
    if contaminante not in breakpoints:
        return 0
    for (bl, bh, il, ih) in breakpoints[contaminante]:
        if bl <= valor <= bh:
            # Fórmula de interpolación lineal
            return ((ih - il) / (bh - bl)) * (valor - bl) + il
    return 301 # Valor fuera de rango (Peligroso)

# 4. Aplicar cálculo a cada fila
def calcular_aqi_fila(row):
    contaminantes = ['PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'O3']
    sub_indices = []
    
    for c in contaminantes:
        si = calcular_sub_indice(row[c], c)
        sub_indices.append(si)
    
    # El AQI es el máximo de los sub-índices
    return round(max(sub_indices))

# 5. Crear la nueva columna AQI
df['AQI'] = df.apply(calcular_aqi_fila, axis=1)

# 6. Clasificar por categoría
def categorizar_aqi(aqi):
    if aqi <= 50: return 'Bueno'
    if aqi <= 100: return 'Moderado'
    if aqi <= 150: return 'Dañino para grupos sensibles'
    if aqi <= 200: return 'Dañino'
    return 'Muy Dañino / Peligroso'

df['Categoria_AQI'] = df['AQI'].apply(categorizar_aqi)

# Ver resultados
print(df[['City', 'Date', 'AQI', 'Categoria_AQI']].head())

# Guardar a un nuevo CSV
df.to_csv('city_air_quality_with_AQI.csv', index=False)