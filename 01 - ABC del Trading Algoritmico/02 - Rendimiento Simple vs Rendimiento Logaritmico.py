# Importaciones
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Configuracion de parametros
ticker = "TSLA"
fecha_inicial="2023-01-01"
fecha_final="2024-01-01"
intervalo = "1d"

# Descargar datos
datos = yf.download(ticker,start=fecha_inicial, end=fecha_final, interval=intervalo, multi_level_index=False)

# Calcular el rendimiento simple
datos["Rendimiento Simple"] = datos["Close"].pct_change() # datos["Cose"] / datos["Cose"].shift(1) - 1

# Calcular el rendimiento logaritmico
datos["Rendimiento Logaritmico"] = np.log(datos["Close"] / datos["Close"].shift(periods= 1))

# Mostrar los primeros registros
print("Datos con Rendimiento Simple y Logaritmico")
print(datos[["Close","Rendimiento Simple","Rendimiento Logaritmico"]].head())

# Graficas
plt.figure(figsize=(14,7))

# Graficas de Rendimiento Simple
plt.subplot(2,1,1)
plt.plot(datos.index, datos["Rendimiento Simple"], label="Rendimiento Simple", color="blue")
plt.title("Rendimiento Simple")
plt.xlabel("Fecha")
plt.ylabel("Rendimiento Simple")
plt.legend()

# Graficas de Rendimiento Logaritmico 
plt.subplot(2,1,2)
plt.plot(datos.index, datos["Rendimiento Logaritmico"], label="Rendimiento Logaritmico", color="green")
plt.xlabel("Fecha")
plt.ylabel("Rendimiento Logaritmico")
plt.title("Rendimiento Logaritmico")
plt.legend()

plt.tight_layout()
plt.show()


# Comparar la relevancia de cada rendimiento
rendimiento_simple_promedio_anual = datos["Rendimineto Simple"].mean() * datos.dropna().shape[0]
rendimiento_logaritmico_promedio_anual = np.exp(datos["Rendimiento Logaritmico"].mean * datos.dropna().shape[0]) - 1
print(f"Rendimiento Simple Promedio Anual: {rendimiento_simple_promedio_anual}")
print(f"Rendimiento Logaritmico Promedio Anual: {rendimiento_logaritmico_promedio_anual}")





