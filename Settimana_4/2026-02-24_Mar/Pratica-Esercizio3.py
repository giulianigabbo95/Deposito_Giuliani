'''
Sviluppare uno script Python che esegua le seguenti operazioni:
    - Creare un array di 50 numeri equidistanti tra 0 e 10 utilizzando np.linspace.
    - Creare un array di 50 numeri casuali compresi tra 0 e 1 utilizzando np.random.random.
    - Sommare i due array elemento per elemento per ottenere un nuovo array.
    - Calcolare:
        . la somma totale degli elementi del nuovo array
        . la somma degli elementi maggiori di 5
    - Stampare:
        . i due array originali
        . il nuovo array risultante
        . le somme calcolate
    - Salvare i risultati in un file TXT:
        . chiedendo all'utente se desidera sovrascrivere il file oppure aggiungere i nuovi dati.
    - Rendere il processo ripetibile, impostando un seed per la generazione casuale.
'''

import os
import numpy as np

NOME_FILE = "risultati.txt"

np.random.seed(42)

arrei_parte1_linspace = np.linspace(0, 10, 50)
print("Array linspace:", arrei_parte1_linspace)

arrei_parte2_random = np.random.random(50)
print("Array random:", arrei_parte2_random)

arrei_unito = arrei_parte1_linspace + arrei_parte2_random
print("Array unito:", arrei_unito)

arrei_somma_totale = np.sum(arrei_unito)
print("Array somma totale:", arrei_somma_totale)
arrei_somma_maggiori_5 = np.sum(arrei_unito[arrei_unito > 5])
print("Somma elementi > 5:", arrei_somma_maggiori_5)


if os.path.exists(NOME_FILE):
    scelta = input("Il file esiste già. Vuoi sovrascriverlo? [S] o [N]: ").lower()
    if scelta == "s":
        modalita = "w"
    else:
        modalita = "a"
else:
    modalita = "w"

with open(NOME_FILE, modalita) as file:
    file.write("Array linspace:" + str(arrei_parte1_linspace) + "\n\n")
    
    file.write("Array random:" + str(arrei_parte2_random) + "\n\n")
    
    file.write("Array unito:" + str(arrei_unito) + "\n\n")
    
    file.write("Somma totale:", arrei_somma_totale, "\n")
    file.write("Somma elementi > 5:", arrei_somma_maggiori_5, "\n")

print("Dati salvati nel file:", NOME_FILE)