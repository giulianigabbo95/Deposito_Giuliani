'''
Esercizio 1: Indovina il numero
Scrivi un programma che generi un numero casuale compreso tra 1 e 100 (inclusi).
L'utente deve provare a indovinare il numero generato inserendo dei tentativi.
Dopo ogni tentativo, il programma deve indicare se il numero segreto è:
- più alto rispetto al numero inserito, oppure
- più basso rispetto al numero inserito.
Il gioco termina quando l'utente indovina il numero oppure sceglie di uscire dal programma.
'''

# Soluzione con l'uso di random e funzioni di controllo, senza limiti di range

import random

#-FUNZIONI-#
def generaNumero(min:int, max:int):
    return random.randint(min, max)

def checkLimitiCONTROL(lim_do:int, lim_up:int):
    flag = False
    if lim_do == lim_up:
        print("I limiti non possono essere uguali! Riprova.")
        flag = True
    if lim_up < lim_do:
        print("Limite superiore minore di limire minore! Riprova.")
        flag = True
    if lim_do < 1:
        print("Il mimite inferiore è fuori range richiesto! Riprova.")
        flag = True
    if lim_up > 100:
        print("Il mimite superiore è fuori range richiesto! Riprova.")
        flag = True
    print("")
    return flag

def checkTentativoCONTROL(x:int, lim_do:int, lim_up:int):
    if x < lim_do:
        print("Il tentativo è troppo basso! Riprova.")
        return False
    if x > limit_hi:
        print("Il tentativo è troppo alto! Riprova.")
        return False
    print("")
    return True

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

while checkLimitiCONTROL(limit_lo, limit_hi) == True: ## == True è implicito e può essere omesso, ma siccome lo capisco meglio lo metto lo stesso
    limit_lo = int(input("Inserisci un limite inferiore: "))
    limit_hi = int(input("Inserisci un limite superiore: "))

print("Scelgo numero tra", limit_lo, "e", limit_hi)
numero_casuale = generaNumero(limit_lo, limit_hi)

while True:
    tentativo = int(input("Indovina inserendo un numero intero positivo (tra 1 e 100), oppure scrivi 0 se vuoi uscire: "))
    
    if tentativo == 0:
        print("Alla prossima!")
        break
    if checkTentativoCONTROL(tentativo, limit_lo, limit_hi) == True:
        if checkTentativo(tentativo, numero_casuale) == True:
            break
        else:
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

# Soluzione con ricorsione, esosa di tempo e memoria

import math

#-FUNZIONI-#

def fibonacciMod(x:int, l:list):
    if x < 0:
        return l
    elif x == 0:
        l.append(0)
        return l
    elif x == 1:
        l.append(1)
        return l
    else:
        l = fibonacciMod(x-1, l)
        if len(l) < 2:
            l.append(1)
        else:
            p = l[-1] + l[-2]
            l.append(p)
        return l


####-MAIN-####
#Variabili
phi = 1.618
numero = 0
sequenza = []

while numero <= 0:
    numero = int(input("Inserisci un numero intero: "))

    if numero <= 0:
        print("Numero non valido!")
    else:
        indice = math.trunc(math.log(numero*math.sqrt(5))/math.log(phi))
        sequenza = fibonacciMod(indice+1, sequenza)
        
        if sequenza[-1] > numero:
            sequenza.pop() #Uguale a scrivere sequenza.remove(indice+1) IN QUESTO CASO (e forse anche sequenza.remove(-1))

print("I numeri di Fibonacci fino a", numero, "sono", sequenza)

'''
# Fibonacci Ricorsivo in C

/*  Funzione ricorsiva che dato un numero i >= 0 calcola il numero di Fibonacci i-esimo:

    L'i-esimo numero di Fibonacci F(i) e` definito attraverso la seguente definizione induttiva:
    F(i) = 0                 se i = 0
    F(i) = 1                 se i = 1
    F(i) = F(i-1) + F(i-2)   se i >= 2

    Nota: il numero di Fibonacci cresce molto velocemente. Per calcolare il numero di Fibonacci per numeri grandi, modificare la funzione sostituendo int con long
*/


#include <stdio.h>

int fibonacci(int i){
    if (i < 0) 
        return -1; /* F(i) non e' definito per interi i negativi! */

    if (i == 0)
        return 0;
    else if (i == 1) 
        return 1;
    else 
        return fibonacci(i-1) + fibonacci(i-2);
}

int main(void){
    int n;
    printf("Inserire intero >= 0 : ");
    scanf("%d", &n);
    printf("L' %do numero di Fibonacci e' %d.", n, fibonacci(n));
    return 0;
}
'''