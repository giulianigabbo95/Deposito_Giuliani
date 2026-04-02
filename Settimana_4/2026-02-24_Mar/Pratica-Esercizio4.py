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
print("Matrice Originale 1:\n", the_metrix)

the_metrix_colonna_2 = the_metrix[:, 1]
print("Seconda colonna:", the_metrix_colonna_2)
the_metrix_riga_3 = the_metrix[2, :]
print("Terza riga:", the_metrix_riga_3)
the_metrix_diagonale = np.diag(the_metrix)
print("Diagonale principale:", the_metrix_diagonale)

the_metrix_somma_diagonale = np.sum(the_metrix_diagonale)
print("Somma diagonale principale:", the_metrix_somma_diagonale)


'''
Creare un array NumPy di forma (4,4) con numeri casuali interi tra 10 e 50.
Utilizzare il fancy indexing per selezionare gli elementi nelle posizioni:
    - (0,1), (1,3), (2,2), (3,0)
Selezionare tutte le righe dispari (numerazione da 0).
Modificare gli elementi selezionati al punto 2 aggiungendo 10 al loro valore.
'''

arrey = np.random.randint(10, 51, (4, 4))
print("Matrice Originale 2:\n", arrey)

indici_righe = [0, 1, 2, 3]
print("Righe della Matrice:\n", indici_righe)
indici_colonne = [1, 3, 2, 0]
print("Colonne della Matrice;", indici_colonne)
arrey_elementi_specifici = arrey[indici_righe, indici_colonne]
print("Elementi Specifici della Matrice;\n", arrey_elementi_specifici)

arrey_righe_dispari = arrey[[1, 3], :]
print("Righe Dispari della Matrice:\n", arrey_righe_dispari)

arrey[indici_righe, indici_colonne] += 10
print("Matrice con Elementi Modificati:", arrey)