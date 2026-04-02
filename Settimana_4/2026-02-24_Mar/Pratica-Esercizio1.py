'''
Realizzare uno script Python utilizzando la libreria NumPy che dimostri la capacità di creare, modificare e manipolare array tramite slicing e fancy indexing.
    1.  Creazione dell'array:
        - Generare un array con valori da 0 a 49 tramite np.arange.
        - Generare ulteriori 50 valori interi casuali compresi tra 49 e 101.
        - Unire i due insiemi in un unico array NumPy.
    2.  Verifica iniziale
        - Stampare:
            . l'array completo
            . il dtype
            . la shape
    3.  Conversione del tipo di dato:
        - Convertire l'array in float64.
        - Stampare nuovamente dtype e shape.
    4. Slicing
        - Utilizzando lo slicing, estrarre:
            . i primi 10 elementi
            . gli ultimi 7 elementi
            . gli elementi dall'indice 5 all'indice 20 (escluso)
            . ogni quarto elemento
        - Modificare successivamente tramite slicing gli elementi dall'indice 10 al 15 (15 escluso), assegnando loro il valore 999.
    5. Fancy Indexing
        - Selezionare:
            . gli elementi nelle posizioni [0, 3, 7, 12, 25, 33, 48]
            . tutti gli elementi pari tramite maschera booleana
            . tutti gli elementi maggiori della media dell'array
    6. Output finale
        - Stampare:
            . l'array finale dopo le modifiche
            . tutti i sotto-array ottenuti con slicing
            . tutti i risultati ottenuti con fancy indexing
'''

import numpy as np

arrei_parte1 = np.arange(0, 50)
print("Array 1° Parte:", arrei_parte1)
arrei_parte2 = np.random.randint(49, 102, 50)
print("Array 2° Parte:", arrei_parte1)
arrei_unito = np.concatenate((arrei_parte1, arrei_parte2))

print("Array Unito Normale:", arrei_unito)
print("dtype:", arrei_unito.dtype)
print("shape:", arrei_unito.shape)

arrei_unito = arrei_unito.astype(np.float64)

print("Array Unito Convertito a float64:", arrei_unito)
print("dtype:", arrei_unito.dtype)
print("shape:", arrei_unito.shape)

arrei_unito_primi_10 = arrei_unito[:10]
print("Array Unito Convertito a float64 Primi 10:", arrei_unito_primi_10)
arrei_unito_ultimi_7 = arrei_unito[-7:]
print("Array Unito Convertito a float64 Ultimi 7", arrei_unito_ultimi_7)
arrei_unito_tra_5_e_20 = arrei_unito[5:20]
print("Array Unito Convertito a float64 Tra Oosizione 5 e 20:", arrei_unito_tra_5_e_20)
arrei_unito_int_ogni_4th = arrei_unito[::4]
print("Array Unito Convertito a float64 Ogni 4 Posizioni", arrei_unito_int_ogni_4th)

arrei_unito[10:15] = 999
print("Array Unito Convertito a float64 Modificato", arrei_unito)

lista_indici = [0, 3, 7, 12, 25, 33, 48]
print("Indici Scelti", lista_indici)
arrei_unito_elementi_specifici = arrei_unito[lista_indici]
print("Array Unito Convertito a float64 Elementi Specifici", arrei_unito_elementi_specifici)
arrei_unito_elementi_pari = arrei_unito[arrei_unito % 2 == 0]
print("Array Unito Convertito a float64 Elementi Pari", arrei_unito_elementi_pari)
arrei_unito_media = np.mean(arrei_unito)
print("Array Unito Convertito a float64 Media Valori", arrei_unito_media)
arrei_unito_elementi_maggiori_media = arrei_unito[arrei_unito > arrei_unito_media]
print("Array Unito Convertito a float64 Elementi Maggiori della Media", arrei_unito_elementi_maggiori_media)