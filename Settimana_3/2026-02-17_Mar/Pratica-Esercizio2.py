'''
Scrivere un programma che utilizza il cifrario di Cesare per criptare una parola o decriptarla.
Il Cifrario di Cesare è un algoritmo di crittografia che consiste nello spostare ciascuna lettera di una certa quantità di posti nell'alfabeto.
Per utilizzarlo, si sceglie una chiave (scelta dall'utente) che rappresenta il numero di posti di cui ogni lettera dell'alfabeto verrà spostata. Esempio: Se si sceglie una chiave di 3, la lettera A diventerà D, la lettera B diventerà E e così via.
Per decifrare un messaggio cifrato con il cifrario di Cesare bisognaconoscere la chiave utilizzata e spostare ogni lettera indietro di un numero di posti corrispondente alla chiave.

# In collaborazione con Fabio D'Alessandri e Elisabetta Carella
'''

def criptaStringa(testo, chiave):
    stringa_criptata = ""
    for c in testo.lower():
        if c.isalpha(): # Controllo se è lettera
            nuovo = (ord(c) - ord('a') + chiave) % 26 + ord('a')    # Calcolo il nuovo carattere spostato
                                                                        # ord('a') è usato per mantenere il ciclo all'interno dell'alfabeto
                                                                        # ord(c)-ord('a') calcola la posizione della lettera nell'alfabeto (0-25)
                                                                        # %26 assicura che si torni all'inizio dell'alfabeto dopo 'z'
            stringa_criptata += chr(nuovo)
        else:
            stringa_criptata += c # rimane invariato
    return stringa_criptata

def decriptaStringa(stringa_criptata, spostamento):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    stringa_decriptata = ''
    for c in stringa_criptata:
        if c.isalpha():
            stringa_decriptata += alfabeto[(alfabeto.index(c) - spostamento) % 26]
        else:
            stringa_decriptata += c
    return stringa_decriptata


while True:
    print("Premi 0 per uscire.")
    scelta = input("Vuoi criptare o decriptare? [C]/[D]): ")   
    if scelta == '0':
        print("Uscita dal programma.")
        break
    if scelta == 'c':
        testo = input("Inserisci il testo da criptare: ")
        chiave = int(input("Inserisci la chiave (numero di posti): "))
        print("Testo criptato:", criptaStringa(testo, chiave))
    elif scelta == 'd':
        testo_criptato = input("Inserisci il testo da decriptare: ")
        chiave = int(input("Inserisci la chiave (numero di posti): "))
        print("Testo decriptato:", decriptaStringa(testo_criptato, chiave))
    else:
        print("Scelta non valida. Riprova.")





def criptaStringa(alfabeto, stringa, spostamento):
    stringa_criptata = ''
    for c in stringa:
        if c in alfabeto:
            indice = (alfabeto.index(c) + spostamento) % 26
            stringa_criptata += alfabeto[indice]
        else:
            stringa_criptata += c
    return stringa_criptata

def decriptaStringa(alfabeto, stringa_criptata, spostamento):
    stringa_decriptata = ''
    for c in stringa_criptata:
        if c in alfabeto:
            stringa_decriptata += alfabeto[(alfabeto.index(c) - spostamento) % 26]
        else:
            stringa_decriptata += c
    return stringa_decriptata


stringa = "Prova".upper()
stringa_criptata = criptaStringa(stringa, 4)
print(stringa_criptata)
stringa_decriptata = decriptaStringa(stringa_criptata, 4)
print(stringa_decriptata)

alfabeto_completo = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
alfabeto_maiuscolo = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfabeto_minuscolo = 'abcdefghijklmnopqrstuvwxyz'

abc = ["A", "B","C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",  "T", "U", "V", "W", "X", "Y", "Z"]
cba = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
strng = 'CiaoSonoGab'
gnrts = 'CIAO SONO Gab'

#newstring = decriptaStringa(abc, strng, 3)
#newstring = decriptaStringa(abc, gnrts, 3)
#newstring = decriptaStringa(cba, strng, 3)
#newstring = decriptaStringa(cba, gnrts, 3)