'''
Esercizio generato con chatGPT:
    Simulare e analizzare i dati di vendita mensili di un'azienda per un anno, utilizzando NumPy per la generazione dei dati, Pandas per l'analisi e Matplotlib/Seaborn per la visualizzazione.

    Un'azienda vende 3 prodotti:
        - Prodotto A
        - Prodotto B
        - Prodotto C
    Si vuole simulare l'andamento delle vendite per 12 mesi.
        - Generazione dati con NumPy
            1. Usa NumPy per generare:
                . Valori casuali per ciascun prodotto (vendite mensili).
                . Le vendite devono seguire distribuzioni diverse:
                    a) Prodotto A → distribuzione normale (media 200, deviazione standard 20)
                    b) Prodotto B → distribuzione normale (media 150, deviazione standard 30)
                    c) Prodotto C → distribuzione normale (media 100, deviazione standard 15)
            2. Arrotonda i valori a numeri interi positivi.
        - Creazione DataFrame con Pandas
            1. Crea un DataFrame Pandas con:
                . Indice: mesi ("Gen", "Feb", ..., "Dic")
                . Colonne: "Prodotto A", "Prodotto B", "Prodotto C"
            2. Aggiungi:
                . Una colonna "Totale Mensile"
                . Una riga finale "Totale Annuale"
        - Analisi dei dati
            1. Calcola:
                . Il mese con vendite totali più alte
                . Il prodotto con vendite annuali maggiori
                . La media mensile di ciascun prodotto
                . La deviazione standard delle vendite mensili per ciascun prodotto
        - Visualizzazioni
            1. Crea almeno 3 grafici diversi:
                . Grafico a linee con l'andamento mensile dei 3 prodotti
                . Grafico a barre con il totale annuale per prodotto
                . Grafico a torta che mostra la percentuale di contributo di ciascun prodotto al totale annuale
        
        [EXTRA]:
        - Analisi (livello avanzato)
            1. Simula uno scenario:
                . Dal mese di luglio in poi, il Prodotto B aumenta le vendite del 20%.
                . Confronta il totale annuale prima e dopo la modifica.
                . Mostra un grafico comparativo.
            2. Aggiungi un grafico heatmap delle vendite mensili.
            3. Calcola la correlazione tra i prodotti.
            4. Salva il DataFrame in un file CSV.
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#import Prodotto

NOME_FILE = r"C:/Users/Gahab/Documents/GitHub/Corso_PyML_Deposito_Studente_Giuliani/Settimana_4/2026-02-27_Ven/Test/vendite_annuali.csv"


np.random.seed(42) # Ottenuti sempre gli stessi numeri casuali

mesi = ["Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno", "Luglio", "Agosto", "Settembre", "Ottobre", "Novembre", "Dicembre"]


#prodotto_A = Prodotto("A", np.random.normal(200, 20, 12))

prodotto_A = np.random.normal(200, 20, 12) # Generazione vendite
prodotto_B = np.random.normal(150, 30, 12) # Generazione vendite
prodotto_C = np.random.normal(100, 15, 12) # Generazione vendite

prodotto_A = np.abs(np.round(prodotto_A)).astype(int) # Arrotondamento e conversione a interi positivi
prodotto_B = np.abs(np.round(prodotto_B)).astype(int) # Arrotondamento e conversione a interi positivi
prodotto_C = np.abs(np.round(prodotto_C)).astype(int) # Arrotondamento e conversione a interi positivi



print("Prima del Totale")
df = pd.DataFrame({
    "Prodotto A": prodotto_A,
    "Prodotto B": prodotto_B,
    "Prodotto C": prodotto_C
}, index=mesi)
print(df)

print("Dopo del Totale")
totale_mensile = df.sum(axis=1)
df["Totale Mensile"] = totale_mensile
totale_annuale = df.sum()
df.loc["Totale Annuale"] = totale_annuale
print(df)



df_mensile = df.iloc[:-1] # Esclusione riga del totale per le analisi mensili

mese_top = df_mensile["Totale Mensile"].idxmax()            # Mese con vendite più alte
prodotto_top = df.loc["Totale Annuale"].iloc[:3].idxmax()   # Prodotto con vendite annuali maggiori
media_mensile = df_mensile.iloc[:, :3].mean()               # Media mensile
dev_std = df_mensile.iloc[:, :3].std()                      # Deviazione standard

print("")
print("Mese con vendite più alte:", mese_top)
print("Prodotto con vendite annuali maggiori:", prodotto_top)
print("Media mensile:")
print(media_mensile)
print("Deviazione standard:")
print(dev_std)



df_mensile[["Prodotto A", "Prodotto B", "Prodotto C"]].plot(marker='o')
plt.title("Andamento Mensile Vendite")
plt.ylabel("Vendite")
plt.xlabel("Mese")
plt.grid(True)
plt.show()

df.loc["Totale Annuale"].iloc[:3].plot(kind='bar')
plt.title("Totale Annuale per Prodotto")
plt.ylabel("Vendite Totali")
plt.show()



df.to_csv(NOME_FILE)