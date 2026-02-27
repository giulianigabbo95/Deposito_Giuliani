'''
Creare un programma che generi un dataset di temperature giornaliere di una città per un mese e calcoli alcune statistiche di base.

Dataset:
    - Deve essere un DataFrame pandas con una sola colonna chiamata temperature.
    - La colonna contiene la temperatura giornaliera per 30 giorni.
    - Puoi generare le temperature in modo casuale (ad esempio tra 10 e 30 gradi).

Statistiche da calcolare:
    - Temperatura massima
    - Temperatura minima
    - Temperatura media
    - Mediana delle temperature

Stampa dei risultati:
    - Visualizzare le statistiche calcolate in modo chiaro, arrotondando eventualmente i valori a due decimali.
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


np.random.seed(42)                          # Ottenuti sempre gli stessi numeri casuali
temperature = np.random.uniform(10, 30, 30) # Simulati 30 giorni di temperature tra 10 e 30 gradi

df = pd.DataFrame({
    "temperature": temperature
})


print("Dataset temperature:")
print("G", df)


print("")
print("Statistiche del mese:")
print("Temperatura massima:", round(df["temperature"].max(), 2))
print("Temperatura minima:", round(df["temperature"].min(), 2))
print("Temperatura media:", round(df["temperature"].mean(), 2))
print("Mediana:", round(df["temperature"].median(), 2))



#Come cazzo si fanno i disegni?

plt.figure(figsize=(10, 5))

plt.plot(df["temperature"], marker="o")

# Linea della media
plt.axhline(round(df["temperature"].mean(), 2), linestyle = "--")

plt.title("Andamento delle Temperature nel Mese")
plt.xlabel("Giorno del mese")
plt.ylabel("Temperatura (°C)")

plt.grid(True)

plt.show()


