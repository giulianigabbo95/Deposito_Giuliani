'''
Scrivere un programma che utilizza una funzione che accetta come parametro una stringa passata dall'utente e restituisce in risposta se è palindroma o no.
Esempio:
'I topi non avevano nipoti' è palindroma
'Ciao' non è palindroma
'''

def ePalindroma(frase):
    frase_nospazi = ""
    for c in frase:
        if c.isalnum():
            frase_nospazi += c.lower()

    # Confronta la stringa con la sua versione invertita
    return frase_nospazi == frase_nospazi[::-1] # non specifico inizio, non specifico fine, passo = -1 (va all’indietro)


stringa = input("Inserisci una frase: ")

if ePalindroma(stringa):
    print("La frase è palindroma")
else:
    print("La frase non è palindroma")