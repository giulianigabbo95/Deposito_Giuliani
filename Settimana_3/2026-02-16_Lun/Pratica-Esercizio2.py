''''
Scrivere un programma che chiede all'utente una serie di parole e restituisce solo le vocali e l'indice della vocale all'interno delle parole.
'''
vocali = ["a", "e", "i", "o", "u"]


def eVocale(c:str, v:list):
    return True if c in v else False


parole = []


while True:
    p = input('Inserisci una parola: ')
    if p == "stop":
        break
    else:
        parole.append(p)

for p in parole:
    indice = 0
    indici = []
    vocali_trovate = []
    while indice < len(p):
        if eVocale(p[indice], vocali):
            vocali_trovate.append(p[indice])
            indici.append(indice)
        indice += 1
    print(f"Parola: {p} | Vocali: {vocali_trovate} | Indice : {indici}")