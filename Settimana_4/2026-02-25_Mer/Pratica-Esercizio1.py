'''
Creare un dataset di esempio contenente informazioni relative a un gruppo di persone.
Il dataset dovrà includere le seguenti colonne:

Nome

Età

Città

Salario

I dati devono essere generati casualmente all’interno del programma.








Generazione e caricamento dei dati

Creare il dataset con valori generati casualmente.

Caricare i dati in un DataFrame pandas.

Esplorazione iniziale

Visualizzare le prime cinque righe del DataFrame.

Visualizzare le ultime cinque righe.

Mostrare il tipo di dato di ciascuna colonna.

Analisi statistica

Calcolare le principali statistiche descrittive per le colonne numeriche:

Media

Mediana

Deviazione standard

Pulizia dei dati

Identificare eventuali righe duplicate e rimuoverle.

Individuare eventuali valori mancanti.

Sostituire i valori mancanti con la mediana della rispettiva colonna numerica.

Creazione di una nuova variabile

Aggiungere una nuova colonna chiamata "Categoria Età", classificando le persone secondo le seguenti fasce:

0–18 anni → Giovane

19–65 anni → Adulto

Oltre 65 anni → Senior

Esportazione dei dati

Salvare il DataFrame pulito in un nuovo file CSV.
'''

import numpy as np
import pandas as pd

# ----------------------------
# 1️⃣ Generazione Dataset
# ----------------------------

np.random.seed(42)  # rendere ripetibile

nomi = ["Luca", "Marco", "Anna", "Giulia", "Paolo", "Sara", "Francesco", "Elena"]
citta = ["Roma", "Milano", "Torino", "Napoli", "Bologna"]

n = 30  # numero persone

data = {
    "Nome": np.random.choice(nomi, n),
    "Età": np.random.randint(15, 80, n),
    "Città": np.random.choice(citta, n),
    "Salario": np.random.randint(20000, 80000, n)
}

df = pd.DataFrame(data)

# Inseriamo volutamente:
df.loc[5, "Salario"] = np.nan   # valore mancante
df = pd.concat([df, df.iloc[[2]]])  # duplicato