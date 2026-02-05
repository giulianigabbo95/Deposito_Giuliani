'''
Esercizio 1
Scrivi un programma che chieda all'utente di inserire un numero intero e stampi:
- "Pari" se il numero è pari,
- "Dispari" se il numero è dispari.
'''

#Variabili
num = int(input("Inserisci un numero: "))

if num % 2 == 0:
    print("Il numero è pari")
else:
    print("Il numero è dispari")
    
#####################################################################################################################################################################################

print("")
'''
Esercizio 2
Scrivi un programma che chieda all'utente di inserire un numero intero positivo n e stampi tutti i numeri da n a 0 (compreso), decrementando di 1.
Al termine, il programma deve chiedere se l'utente desidera ripetere l'operazione, permettendo di eseguirla più volte.
'''

while True:
    #Variabili
    numero = int(input("Inserisci un numero intero positivo: "))

    if numero <= 0:
        print("Errore: inserisci un numero positivo.")
    else:
        for i in range(numero, -1, -1):
            print(i)

    risposta = input("Vuoi ripetere l'operazione? [S] o [N]: ").upper()  # In teoria dovrebbe ripetersi all'infinito
    if risposta != "S":
        print("Va bene, alla prossima!")
        break

#####################################################################################################################################################################################

print("")
'''
Esercizio 3
Scrivi un programma che chieda all'utente di inserire una lista di numeri e stampi il quadrato di ciascun numero presente nella lista.
'''

#Variabili
numeri = []

while True:
    numero = int(input("Inserisci un numero: "))
    
    numeri.append(numero)

    scelta = input("Vuoi inserire un altro numero? [S] o [N]: ").upper()
    if scelta != "S":
        break

for num in numeri:
    print(num, "al quadrato è:", num * num)

#####################################################################################################################################################################################

print("")
'''
Esercizio 4
Scrivi un programma che prenda in input una lista di numeri interi inserita dall'utente.
Il programma deve:
- Utilizzare un ciclo for per individuare il numero massimo presente nella lista.
- Utilizzare un ciclo while per contare il numero totale di elementi della lista.
- Utilizzare una condizione if per stampare "Lista vuota" se la lista non contiene elementi.
    Altrimenti, stampare il numero massimo e il numero totale di elementi presenti.
'''    

#Variabili
numeri = []
massimo = 0
indice = 0

while True:
    scelta = input("Vuoi inserire un numero? [S] o [N]: ").upper()
    
    if scelta != "S":
        break

    num = int(input("Inserisci un numero intero: "))
    
    numeri.append(num)

for num in numeri: #Se la lista è vuota da errore
    if num > massimo:
        massimo = num

while (indice <= len(numeri)):
    indice += 1

if indice > 0: 
    print("Numero massimo:", massimo)
    print("Numero totale di elementi:", indice)
else:
    print("Lista vuota")

  

    