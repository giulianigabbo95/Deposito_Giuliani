'''
Creare una matrice NumPy per estrarre, modificare e manipolare sotto-matrici e array, applicando operazioni avanzate come l'inversione delle righe e la sostituzione condizionale degli elementi.
    1. Crea una matrice NumPy 2D 6x6 contenente numeri interi casuali compresi tra 1 e 100.
    2. Estrai la sotto-matrice centrale 4x4 dalla matrice originale.
    3. Inverti le righe della matrice estratta (cioè, la prima riga diventa l'ultima, la seconda diventa la penultima, e così via).
    4. Estrai la diagonale principale della matrice invertita e crea un array 1D contenente questi elementi.
    5. Sostituisci tutti gli elementi della matrice invertita che sono multipli di 3 con il valore -1.
    6. Stampa la matrice originale, la sotto-matrice centrale estratta, la matrice invertita, la diagonale principale e la matrice invertita modificata.
'''

import numpy as np

the_metrix = np.random.randint(1, 101, (6, 6))              # np.random.randint(x, y, (b, h)) crea una matrice bxh con numeri interi casuali tra x e y
sottomatrice = the_metrix[1:5, 1:5]                         # [a:b, c:d] estrae la sotto-matrice centrale (b-a)x(d-c), righe a:b e colonne d:c
the_metrix_invertita = sottomatrice[::-1, :]                # [::-1, :] inverte le righe della sottomatrice
diagonale = np.diag(the_metrix_invertita)                   # np.diag() estrae la diagonale principale della matrice invertita
the_metrix_invertita[the_metrix_invertita % 3 == 0] = -1    # [the_metrix_invertita % z == 0] = c sostituisce i multipli di z ponendoli uguali a c

print("Matrice originale:", the_metrix)
print("Sotto-matrice centrale 4x4:", sottomatrice)
print("Matrice con righe invertite:", the_metrix_invertita)
print("Diagonale principale della matrice invertita:", diagonale)
print("Matrice invertita modificata (multipli di 3 → -1):", the_metrix_invertita)