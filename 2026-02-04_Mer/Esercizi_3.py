'''
Esercizio 1
Chiedere all'utente di inserire un numero intero.
Il programma deve eseguire un conto alla rovescia a partire dal numero inserito fino ad arrivare a zero, stampando ogni valore.
Al termine del conteggio, il programma deve chiedere all'utente se desidera ripetere l'operazione oppure terminare l'esecuzione.
'''

while(True):
    #Variabili
    numero = int(input("Inserisci un numero: "))
    
    for n in range(numero, -1, -1):
        print(n)
    risposta = input("Vuoi giocare ancora? [S] o [N]: ").upper()
    if risposta != "S":
        print("Va bene, alla prossima!")
        break
    
#####################################################################################################################################################################################

print("")
'''
Esercizio 2
Chiedere ripetutamente all'utente di inserire un numero intero.
Per ogni numero inserito, il programma deve verificare se il numero è primo oppure no.
Se il numero è primo deve salvarlo in una struttura dati e stampare il messaggio: "Il numero è primo";
Altrimenti deve stampare il messaggio: "Il numero non è primo".
Il programma deve terminare automaticamente quando sono stati individuati 5 numeri primi.
'''
import math #Forse sto barando

#Variabili
lista = []
primo = False

while len(lista) < 5:
    #Variabili
    num = int(input("Inserisci un numero: "))
    
    if num <= 0:
            print("Funziono solo con numeri positivi!")
    elif num == 1:
        primo = False
        print("Con 1 è troppo facile!")
    elif num == 2:
        primo = True
    elif num % 2 == 0:
        primo = False
    else:
        primo = True
        for numero in range(3, int(math.sqrt(num))+1, 2): # Controlla solo i divisori dispari fino alla radice quadrata
            if num % numero == 0:
                primo = False
                break                
    if primo:
        if num not in lista:
            lista.append(num)
            print("Il nostro numero:", num, "è un numero primo!")
        else:
            print("Numero primo già in lista!")
    else:
        print("Il nostro numero:", num, "NON è un numero primo!")        
print("Numeri primi trovati:", lista)

