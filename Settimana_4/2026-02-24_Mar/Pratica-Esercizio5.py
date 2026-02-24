'''

'''

import numpy as np

FILE_NAME = "log_matrice.txt"

def salvaFile(contenuto):
    with open(FILE_NAME, "a") as file:
        file.write(contenuto + "\n")
        file.write("-" * 40 + "\n")

def creaMatrice():
    righe = int(input("Numero righe: "))
    colonne = int(input("Numero colonne: "))
    matrice = np.random.randint(1, 101, (righe, colonne))
    print("Matrice creata:\n", matrice)
    salvaFile("Matrice creata:\n" + matrice)
    return matrice

def estraiSottomatriceCentrale(matrice):
    r, c = matrice.shape
    if r < 3 or c < 3:
        print("Matrice troppo piccola per estrarre una parte centrale.")
        return
    sub = matrice[1:r-1, 1:c-1]
    print("Sottomatrice centrale:\n", sub)
    salvaFile("Sottomatrice centrale:\n", sub)

def trasponiMatrice(matrice):
    t = matrice.T
    print("Matrice trasposta:\n", t)
    salvaFile("Matrice trasposta:\n", t) 

def sommaElementi(matrice):
    s = np.sum(matrice)
    print("Somma elementi:", s)
    salvaFile("Somma elementi:", s)

def mediaElementi(matrice):
    m = np.mean(matrice)
    print("Media elementi:", m)
    salvaFile("Media elementi:", m)

def moltiplicazioneElementWise(matrice):
    seconda = np.random.randint(1, 101, matrice.shape)
    risultato = matrice * seconda
    print("Seconda matrice:\n", seconda)
    print("Risultato moltiplicazione element-wise:\n", risultato)
    salvaFile("Seconda matrice:\n", seconda)
    salvaFile("Moltiplicazione element-wise:\n", risultato)

def determinanteMatrice(matrice):
    if matrice.shape[0] == matrice.shape[1]:
        det = np.linalg.det(matrice)
        print("Determinante:", det)
        salvaFile("Determinante:", det)
    else:
        print("La matrice non è quadrata.")
        salvaFile("Tentativo calcolo determinante: matrice non quadrata")

# MAIN
metrix = None

while True:
    selezione = input("Vuoi creare una nuova matrice casuale? [S] o [N]: ").lower()
    
    if selezione != 's':
        print("Allora questo programma non può essere utilizzato!")
        print("Addio!")
        break
    
    metrix = creaMatrice()
        
    print("Menu")
    print("1. Crea nuova matrice")
    print("2. Estrai sottomatrice centrale")
    print("3. Trasponi matrice")
    print("4. Somma elementi")
    print("5. Media elementi")
    print("6. Moltiplicazione element-wise")
    print("7. Determinante (se quadrata)")
    print("0. Esci")

    if metrix is not None:
        scelta = input("Scelta: ")

        match scelta:
            case "1":
                metrix = creaMatrice()
            case "2":
                estraiSottomatriceCentrale(metrix)
            case "3" :
                trasponiMatrice(metrix)
            case "4":
                sommaElementi(metrix)
            case "5":
                mediaElementi(metrix)
            case "6":
                moltiplicazioneElementWise(metrix)
            case "7":
                determinanteMatrice(metrix)
            case "0":
                print("Ciao!")
                break
            case _:
                print("Scelta non valida.\n")
    else:
        print("Matrice non esistente.\n")
        break