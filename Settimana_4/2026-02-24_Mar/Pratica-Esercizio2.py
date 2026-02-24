'''
Sviluppare uno script Python che esegua i seguenti passaggi:
    - Creare un array di 12 numeri equidistanti compresi tra 0 e 1 utilizzando la funzione np.linspace.
    - Modificare la forma dell'array ottenuto trasformandolo in una matrice 3x4 tramite reshape.
    - Generare una matrice 3x4 contenente numeri casuali compresi tra 0 e 1.
    - Calcolare e stampare la somma degli elementi di entrambe le matrici.
'''

import numpy as np

arrei = np.linspace(0, 1, 12)
print("Array:", arrei)

the_metrix_linspace = arrei.reshape(3, 4)
print("Matrice ottenuta con linspace:", the_metrix_linspace)

the_metrix_random = np.random.rand(3, 4)
print("Matrice casuale:", the_metrix_random)

somma_linspace = np.sum(the_metrix_linspace)
print("Somma elementi matrice linspace:", somma_linspace)
somma_random = np.sum(the_metrix_random)
print("Somma elementi matrice casuale:", somma_random)