'''
Esercizio 1: Indovina il numero
Scrivi un programma che generi un numero casuale compreso tra 1 e 100 (inclusi).
L'utente deve provare a indovinare il numero generato inserendo dei tentativi.
Dopo ogni tentativo, il programma deve indicare se il numero segreto è:
- più alto rispetto al numero inserito, oppure
- più basso rispetto al numero inserito.
Il gioco termina quando l'utente indovina il numero oppure sceglie di uscire dal programma.
'''

# Soluzione con l'invenzione di una funzione di numeri pseudo randomici
def generaNumeroPseudoCasuale(x:int, y:int):
    base = int(input("Inserisci un seed: "))
    
    if base % 2 == 0:
        return ((base * 42 + 12) * limite_hi - limite_lo) % 100 + 1 #Operazione inventata senza senso logico eccetto "% 100 + 1"
    else:
        return ((base * 21 + 24) * limite_hi - limite_lo) % 100 + 1 #Operazione inventata senza senso logico eccetto "% 100 + 1"
    

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

#MAIN
#VARIABILI
limite_lo = 1
limite_hi = 100

numero_segreto = generaNumeroPseudoCasuale(limite_lo, limite_hi)

print(f"Ho scelto un numero tra {limite_lo} e {limite_hi}. Prova a indovinarlo!") # Uguale a scrivere print("Ho scelto un numero tra", limite_lo, "e", limite_hi, ". Prova a indovinarlo!")
print("Scrivi 0 se vuoi uscire.")
while True:
    tentativo = input("Inserisci il tuo tentativo: ")

    if tentativo == 0:
        print("Hai scelto di uscire dal gioco.")
        break
    elif tentativo < 0 or tentativo > 100:
        print("Sei fuori range")
    else:     
        indovinato = checkTentativo(tentativo, numero_segreto)

        if indovinato == True:
            break
    print("Riprova!")

#####################################################################################################################################################################################

print("")
'''
Esercizio 2: Sequenza di Fibonacci fino a N
Chiedi all'utente di inserire un numero N.
Il programma deve stampare tutti i numeri della sequenza di Fibonacci minori o uguali a N.
Esempio:
Se l'utente inserisce 100, il programma deve stampare tutti i numeri della sequenza di Fibonacci che non superano 100.
'''

# Soluzione con iterazioni su funzioni (probabilmente inutili)

def fibonacci(l:list):
    return l[len(l)-1] + l[len(l)-2] # l[len(l)-1] + l[len(l)-2] uguale a scrivere l[-1] + l[-2])
    
def checkProssimo(p:int, n:int):
    if p < n:
        return True
    else:
        return False

#MAIN
#VARIABILI
num = int(input("Inserisci un numero intero: "))
a = 0
b = 1
sequenza = [a, b]

while sequenza[len(sequenza)-1] < num: # sequenza[len(sequenza)-1] uguale a scrivere sequenza[-1]
    prossimo = fibonacci(sequenza)
    if checkProssimo(num) == True:
        sequenza.append(prossimo)
    else:
        break

print(f"I numeri di Fibonacci fino a {num} sono {sequenza}")