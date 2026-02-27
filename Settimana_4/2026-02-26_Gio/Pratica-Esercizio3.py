import pandas as pd
import numpy as np

# Creazione del DataFrame di esempio
data = {
    'altezza': [175, 168, 182, 160, 170, 185, 158, 172],
    'peso': [70, 65, 80, 55, 68, 85, 50, 72],
    'età': [25, 32, 28, 45, 23, 35, 41, 29]
}

df = pd.DataFrame(data)

# Funzione per la normalizzazione min-max
def min_max_normalization(series):
    min_val = series.min()
    max_val = series.max()
    return (series - min_val) / (max_val - min_val)

# Creazione di una copia del DataFrame per la normalizzazione
df_normalizzato = df.copy()

# Applicazione della normalizzazione min-max alle colonne 'altezza' e 'peso'
df_normalizzato['altezza'] = min_max_normalization(df_normalizzato['altezza'])
df_normalizzato['peso'] = min_max_normalization(df_normalizzato['peso'])


print("DataFratm Base:", df)
print("DataFratm Normalizzato:", df_normalizzato)
print("Confronto Statistiche:", df_normalizzato)
