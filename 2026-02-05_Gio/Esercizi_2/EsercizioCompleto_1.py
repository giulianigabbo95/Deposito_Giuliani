'''
Esercizio 1
Scrivi un programma che chieda all'utente di inserire un numero intero positivo n.
Il programma deve poi eseguire le seguenti operazioni:
1. Controllo dell'input:
    Utilizzare un ciclo while per garantire che l'utente inserisca un numero positivo.
    Se l'utente inserisce un numero negativo o uguale a zero, il programma deve continuare a chiedere un numero finché non viene inserito un valore valido.
2. Somma dei numeri pari
    Utilizzare un ciclo for con range() per calcolare e stampare la somma di tutti i numeri pari compresi tra 1 e n.
3. Stampa dei numeri dispari
    Utilizzare un ciclo for per stampare tutti i numeri dispari compresi tra 1 e n.
4. Verifica numero primo
    Utilizzare una struttura if per determinare se n è un numero primo.
    Un numero si dice primo se è divisibile solo per 1 e per se stesso.
    Il programma deve stampare se n è primo oppure no.
EXTRA: Crea una lista che salva tutti i tentativi e un'ultima sezione del programma che permetta di visionare o modificare la lsita
'''

#Variabili
numero = 0
somma_p = 0
somma_d = 0
pari = []
dispari = []
tentativi = []
primo = False

#1 - Controllo dell'input:
while numero <= 0:
    numero = int(input("Inserisci un numero: "))
    tentativi.append(numero)
    if numero <= 0:
        print("Sbagliato! Riprova.")

#2 - Somma dei numeri pari
if numero == 1:
    pass
else:  
    for num in range(2, numero, 2):
        pari.append(num)
        somma_p = somma_p + num
print("La somma dei numeri pari", pari, "è:", somma_p)

#3 - Stampa dei numeri dispari
if numero == 1:
    somma_d += 1
    dispari.append(numero) 
else:
    for num in range(1, numero, 2):
        dispari.append(num)
        somma_d = somma_d + num
print("La somma dei numeri dispari", dispari, "è;", somma_d)

#4 - Verifica numero primo
if numero < 2:
    print(numero, "Primo")
else:
    primo = True
    for num in range(2, numero, 1):
        if numero % num == 0:
            primo = False
            break

#Extra
uscita = True

while uscita == True:
    scelta = input("Vuoi vedere o modificare la lista? [V] o [M]: ").upper()

    match scelta:
        case "V":
            print("La cronologia degli inserimenti è stata:", tentativi)
        case "M":
            modifica = True 
            while modifica == True:
                selezione = int(input("Che elemento vuoi rimuovere? "))
                if selezione < len(tentativi):
                    tentativi.remove(selezione)
                else:
                    print("Selezione non valida!")
                decisione = input("Vuoi continaure? [S] o [N]: ").upper()
                if decisione == "S":
                    pass
                elif decisione == "N":
                    modifica == False
                else:
                    print("Non ho capito!")
        case _:
            print("Scelta non contemplata! Chiudo...")