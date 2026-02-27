'''
Generare un dataset di serie temporali utilizzando NumPy, analizzarlo con pandas e visualizzare i risultati con Matplotlib.

1. Generazione dei dati
    - Simulare 365 giorni di dati (un anno).
    - Rappresentare il numero giornaliero di visitatori di un parco.
    - Assumere:
        . Media = 2000 visitatori
        . Deviazione standard = 500
    - Aggiungere un trend crescente nel tempo per simulare l'aumento della popolarità del parco.

2. Creazione del DataFrame
    - Creare un DataFrame pandas.
    - Utilizzare le date come indice.
    - Inserire il numero di visitatori come colonna.

3. Analisi dei dati
    - Calcolare:
        . Media mensile dei visitatori.
        . Deviazione standard mensile.

4. Visualizzazione
    - Grafico a linee dei visitatori giornalieri.
    - Aggiungere la media mobile a 7 giorni.
    - Creare un secondo grafico con la media mensile.
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


np.random.seed(42) # Ottenuti sempre gli stessi numeri casuali


date = pd.date_range(start = '2026-01-01', periods = 365)               # Creazione date
visitatori_base = np.random.normal(loc = 2000, scale = 500, size = 365) # Generazione visitatori base (distribuzione normale)                            
visitatori_totali = visitatori_base + np.linspace(0, 1000, 365)         # Totale visitatori = Base + Trend crescente
visitatori_totali = np.round(visitatori_totali)                         # Arrotondamento valori interi e rimozione eventuali negativi
visitatori_totali = np.clip(visitatori_totali, a_min = 0, a_max = None)


df = pd.DataFrame({'Visitatori': visitatori_totali}, index = date)
print("DataFrame creato correttamente:\n", df.head(10))


media_mensile = df.resample('ME').mean()
std_mensile = df.resample('ME').std()

print("Media mensile visitatori:", media_mensile)
print("Deviazione standard mensile:", std_mensile)

# =========================
# MEDIA MOBILE 7 GIORNI
# =========================

df['Media_mobile_7gg'] = df['Visitatori'].rolling(window=7).mean()

# =========================
# GRAFICI
# =========================

plt.figure()
plt.plot(df.index, df['Visitatori'])
plt.plot(df.index, df['Media_mobile_7gg'])
plt.title("Visitatori giornalieri con Media Mobile (7 giorni)")
plt.xlabel("Data")
plt.ylabel("Numero visitatori")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


plt.figure()
plt.plot(media_mensile.index, media_mensile['Visitatori'])
plt.title("Media mensile dei visitatori")
plt.xlabel("Mese")
plt.ylabel("Numero medio visitatori")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()