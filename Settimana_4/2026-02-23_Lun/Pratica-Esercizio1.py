'''
Creare un array NumPy utilizzando arange e verificare il tipo di dato utilizzando dtype e la forma dell'array utilizzando shape.
    1. Utilizza la funzione np.arange per creare un array di numeri interi da 10 a 49.
    2. Verifica il tipo di dato dell'array e Stampa il risultato.
    3. Cambia il tipo di dato dell'array in float64.
    4. Verifica di nuovo il tipo di dato.
    5. Stampa la forma dell'array.
'''

import numpy as np

arrei_int = np.arange(10, 50)                           # np.arange(x, y) crea un array di numeri interi da x a y
print("Tipo di dato originale:", arrei_int.dtype)       # dtype verifica il tipo di dato
arrei_float = arrei_int.astype(np.float64)              # astype cambia il tipo di dato in float64, con np.float64
print("Tipo di dato cambiato:", arrei_float.dtype)      # dtype verifica il tipo di dato
print("Forma dell'array:", arrei_int.shape)             # shape stampa la forma dell'array
