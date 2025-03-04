# IMportando librerias
import datetime
import os
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Configuracion de parametros
ticker = "AAPL"
fecha_inicio = "2023-01-01"
fecha_final = "2024-01-01"
intervalo = "1d"

# Descargar datos historicos de Yahoo Finance
datos = yf.download(ticker, start=fecha_inicio, end=fecha_final, interval=intervalo)

# Mostrar los primeros registros
print("Datos Históricos:")
print(datos.head())

# Guardar los datos
if not os.path.isdir("../datos"):
    os.mkdir("../datos")

datos.to_csv("../datos/datos_historicos.csv")
    
# Intervalos disponibles y sus limitaciones:

# |----------|------------|--------------|    
# |  Código  |   Tiempo   |  Limitación  |
# |----------|------------|--------------|
# |   1m     | 1 minuto   |    7 días    |
# |----------|------------|--------------|
# |   2m     | 2 minutos  |    60 días   |
# |----------|------------|--------------|
# |   5m     | 5 minutos  |    60 días   |
# |----------|------------|--------------|
# |   15m    | 15 minutos |    60 días   |
# |----------|------------|--------------|
# |   30m    | 30 minutos |    60 días   |
# |----------|------------|--------------|
# |   60m    | 1 hora     |    730 días  |
# |----------|------------|--------------|
# |   90m    | 90 minutos |    60 días   |
# |----------|------------|--------------|
# |   1h     | 1 hora     |    730 días  |
# |----------|------------|--------------|
# |   1d     | 1 día      |    Ninguna   |
# |----------|------------|--------------|
# |   5d     | 5 días     |    Ninguna   |
# |----------|------------|--------------|
# |   1wk    | 1 semana   |    Ninguna   |
# |----------|------------|--------------|
# |   1mo    | 1 mes      |    Ninguna   |
# |----------|------------|--------------|
# |   3mo    | 3 meses    |    Ninguna   |
# |----------|------------|--------------|


# Ejemplos de uso de dieferntes activos e intervalos de tiempo

# Ejemplo 1: Descargar datos con intervalo de 1 minuto (limitado a aproximadamente 7 días)
intervalo_1m = yf.download(tickers="EURUSD=X", interval="1m")
print("Datos de 1 minuto:")
print(intervalo_1m)

# Ejemplo 2: Descargar datos con intervalo de 15 minutos (limitado a aproximadamente 60 días)
fecha_final = datetime.now()
fecha_inicial = fecha_final = datetime.timedelta(days=30)
















