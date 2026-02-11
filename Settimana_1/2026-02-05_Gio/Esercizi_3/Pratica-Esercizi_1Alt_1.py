'''
Esercizio 1: Indovina il numero
Scrivi un programma che generi un numero casuale compreso tra 1 e 100 (inclusi).
L'utente deve provare a indovinare il numero generato inserendo dei tentativi.
Dopo ogni tentativo, il programma deve indicare se il numero segreto è:
- più alto rispetto al numero inserito, oppure
- più basso rispetto al numero inserito.
Il gioco termina quando l'utente indovina il numero oppure sceglie di uscire dal programma.
'''

# Soluzione con l'uso di random

import random

#-FUNZIONI-#
def generaNumero(min:int, max:int):
    return random.randint(min, max)

def checkTentativo(x:int, y:int):
    if x < y:
        print("Il numero segreto è PIÙ ALTO.")
        return False
    elif x > y:
        print("Il numero segreto è PIÙ BASSO.")
        return False
    else:
        print("Complimenti! Hai indovinato il numero!")
        return True


####-MAIN-####
#Variabili
limit_lo = 101
limit_hi = 0

while limit_hi < limit_lo or limit_hi > 100 or limit_lo < 1:
    limit_lo = int(input("Inserisci un limite inferiore (minimo 1): "))
    limit_hi = int(input("Inserisci un limite superiore (massimo 100): "))
    if limit_hi < limit_lo or limit_hi > 100 or limit_lo < 1:
        if limit_hi < limit_lo:
            print("Limite superiore minore di limire minore! Riprova.")
        if limit_lo < 1:
            print("Il mimite inferiore è fuori range richiesto! Riprova.")
        if limit_hi > 100:
            print("Il mimite superiore è fuori range richiesto! Riprova.")
        print("")

numero_casuale = generaNumero(limit_lo, limit_hi)

print("Ho scelto numero tra", limit_lo, "e", limit_hi)
while True:
    tentativo = int(input("Indovina inserendo un numero intero positivo (tra 1 e 100), oppure scrivi 0 se vuoi uscire: "))

    if tentativo == 0:
        print("Alla prossima!")
        break
    if tentativo > 100 or tentativo < 1:
        if tentativo < 1:
            print("Il tentativo è troppo basso! Riprova.")
        if tentativo > 100:
            print("Il tentativo è troppo alto! Riprova.")
        print("")
    else:
        if checkTentativo(tentativo, numero_casuale) != False:
            break
        print("Ritenta, sarai più fortunato!")
        print("")


#####################################################################################################################################################################################

print("")
'''
Esercizio 2: Sequenza di Fibonacci fino a N
Chiedi all'utente di inserire un numero N.
Il programma deve stampare tutti i numeri della sequenza di Fibonacci minori o uguali a N.
Esempio: Se l'utente inserisce 100, il programma deve stampare tutti i numeri della sequenza di Fibonacci che non superano 100.
EXTRA: creare una funzione che converte da input a lista e una per convertire da lista a tupla e viceversa
'''

# Soluzione con ciclo

#-FUNZIONI-#
def trovaFibonacciFinoA(n:int):
    a = 0
    b = 1
    lista = []
    
    lista.append(a)
    lista.append(b)
    while b < n:
        c = a + b
        if c > n:
            break
        else:
            sequenza.append(c)
            a = b
            b = c
            # ATTENZIONE: Scrivere prima b = c e poi a = b non avrebbe funzionato!
    return lista

####-MAIN-####
#Variabili
sequenza = []
numero = 0

while numero <= 0:
    numero = int(input("Inserisci un numero intero: "))

    if numero <= 0:
        print("Numero non valido!")
    else:
        sequenza = trovaFibonacciFinoA(numero)

print("I numeri di Fibonacci fino a", numero, "sono", sequenza)
