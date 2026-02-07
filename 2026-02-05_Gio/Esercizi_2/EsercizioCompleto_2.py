'''
Esercizio 2
Scrivi un programma che esegua le seguenti operazioni:
1. Inserimento di un numero positivo
    Chiedi all'utente di inserire un numero intero positivo n.
    Se l'utente inserisce un numero negativo o uguale a zero, il programma deve continuare a chiedere un numero finché non viene inserito un valore valido.
2. Generazione di una lista di numeri casuali
    Genera una lista contenente n numeri interi casuali, compresi tra 1 e n (inclusi).
    La lunghezza della lista deve essere esattamente n.
3. Somma dei numeri pari
    Utilizza un ciclo for per calcolare e stampare la somma di tutti i numeri pari presenti nella lista.
4. Stampa dei numeri dispari
    Utilizza un ciclo for per stampare tutti i numeri dispari contenuti nella lista.
5. Verifica numero primo tramite funzione
    Utilizza una funzione per determinare se un numero è primo.
    La funzione deve restituire:
    - True se il numero è primo
    - False altrimenti
6. Stampa dei numeri primi nella lista
    Utilizza un ciclo for per stampare tutti i numeri primi presenti nella lista.
7. Verifica della somma dei numeri primi
    Infine, utilizza una struttura if per verificare se la somma di tutti i numeri primi presenti nella lista è un numero primo e stampa il risultato.
'''

import math

#Variabili
numero = 0
somma_p = 0
somma_d = 0
somma_primi = 0
primo = False
pari = []
dispari = []
primi = []

#1 - Inserimento di un numero positivo
while numero <= 0:
    numero = int(input("Inserisci un numero: "))
    if numero <= 0:
        print("Sbagliato! Riprova.")

#2 - Generazione di una lista di numeri casuali
numeri = [*range(1, numero+1, 1)]
print("il numero inserito:", numero, "è uguale alla lunghezza della lista di numeri:", len(numeri))

#3 - Somma dei numeri pari
if numero == 1:
    print("Non ci sono numeri pari quindi la somma è:", somma_p)
else:  
    for num in range(0, len(numeri), 2):
        pari.append(num)
        somma_p = somma_p + num
print("La somma dei numeri pari", pari, "è:", somma_p)

#4 - Stampa dei numeri dispari
if numero == 1:
    somma_d += 1
    dispari.append(numero) 
else:
    for num in range(1, numero, 2):
        dispari.append(num)
        somma_d = somma_d + num
print("La somma dei numeri dispari", dispari, "è:", somma_d)

#5 - Verifica numero primo tramite funzione
if numero <= 1:
    primo = False
elif numero == 2:
    primo = True
elif numero % 2 == 0:
    primo = False
else:
    primo = True
    for num in range(3, int(math.sqrt(numero))+1, 2): # Controlla solo i divisori dispari fino alla radice quadrata
        if numero % num == 0:
            primo = False
            break
if primo:
    print("Il nostro numero:", numero, "è un numero primo")
else:
    print("Il nostro numero:", numero, "NON è un numero primo")

#6 - Stampa dei numeri primi nella lista
for n in numeri:
    if n <= 1:
        primo = False
    elif n == 2:
        primo = True
    elif n % 2 == 0:
        primo = False
    else:
        primo = True
        for num in range(3, int(math.sqrt(n))+1, 2):
            if n % num == 0:
                primo = False
                break
    if primo:
        primi.append(n)
print("I numeri primi sono:", primi)

#7 - Verifica della somma dei numeri primi
for i in primi:
    somma_primi += i
if somma_primi <= 1:
    primo = False
elif somma_primi == 2:
    primo = True
elif somma_primi % 2 == 0:
    primo = False
else:
    primo = True
    for num in range(3, int(math.sqrt(somma_primi))+1, 2):
        if somma_primi % num == 0:
            primo = False
            break
if primo:
    print("La somma dei primi è un numero primo:", somma_primi)
else:
    print("La somma dei primi è un numero primo:", somma_primi)