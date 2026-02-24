import numpy as np

'''
Creare un array NumPy di 15 elementi contenente numeri casuali compresi tra 1 e 100.
Calcolare e stampare:
    - la somma di tutti gli elementi
    - la media di tutti gli elementi
'''

arrei = np.random.randint(1, 101, 15)
print("Array:", arrei)

somma = np.sum(arrei)
print("Somma:", somma)
media = np.mean(arrei)
print("Media:", media)


'''
Creare una matrice 5x5 contenente numeri interi sequenziali da 1 a 25.
Estrarre e stampare:
    - la seconda colonna
    - la terza riga
Calcolare e stampare la somma della diagonale principale.
'''

the_metrix = np.arange(1, 26).reshape(5, 5)
print("Matrice:", the_metrix)

the_metrix_colonna_2 = the_metrix[:, 1]
print("Seconda colonna:", the_metrix_colonna_2)
the_metrix_riga_3 = the_metrix[2, :]
print("Terza riga:", the_metrix_riga_3)
the_metrix_diagonale = np.diag(the_metrix)
print("Diagonale principale:", the_metrix_diagonale)

the_metrix_somma_diagonale = np.sum(the_metrix_diagonale)
print("Somma diagonale principale:", the_metrix_somma_diagonale)