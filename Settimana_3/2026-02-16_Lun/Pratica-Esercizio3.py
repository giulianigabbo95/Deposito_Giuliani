'''
Scrivete un programma che chiede una stringa all'utente e restituisce un dizionario rappresentante la "frequenza di comparsa" di ciascun carattere componente la stringa.
Esempio: Stringa "ababcc",
Risultato: {"a": 2, "b": 2, "c": 2}
'''

while True:
    numero_lettere = {}
    
    p = input('Inserisci un testo: ').lower()
    if p == "stop":
        break
    
    for c in p:
        if c not in numero_lettere: # Uguale a dire numero_lettere.keys() perché sottointeso
            numero_lettere[c] = 1
        else:
            numero_lettere[c] += 1
    
    print(numero_lettere)