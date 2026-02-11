'''
Esercizio 1
Realizzare una struttura di condizioni annidate (if dentro altri if) che, sulla base di un input fornito dall'utente, stabilisca se consentire o meno il passaggio.
La struttura deve prevedere 3 livelli di annidamento e utilizzare il confronto tramite l'operatore ==.
'''
print("")
print("START")

#Variabili
a = int(input("Dimmi un numero come limite inferiore di range per indovinare al numero che sto pensando: "))
b = int(input("Dimmi un numero come limite maggiore di range per indovinare al numero che sto pensando: "))
c = 10

if a > 8 :
    if b < 12 :
        if (a == c or b == c):
            print("Sei al Livello 3")
            print("Esatto! Il numero da indovinare era 10.")
        else:
            print("Sei uscito al livello 2")
            print("I numeri non erano uguali! Riprova.")
    else:
        print("Sei uscito al livello 1")
        print("Prova con un limite maggiore di range più basso.")
else:
    print("Sei uscito al livello 0")
    print("Prova con un limite inferiore di range più alto.")

print("")
#####################################################################################################################################################################################
print("------------------------")
print("") # Lascia una riga di spazio tra un esercizio e l'altro
'''
Esercizio 2
Realizzare una struttura condizionale composta da un if, più elif e un else finale, che gestisca un menù per la selezione delle operazioni di un CRUD basilare:
- Aggiunta
- Rimozione
- Eliminazione.
'''

#Variabili
scelta = input("DEV TEST: Vuoi inserire dei numeri in lista? [S] o [N]: ").upper()
numeri = []
if scelta == 'S' :
    x = int(input("Dimmi un numero: "))
    numeri.append(x)
    y = int(input("Dimmene un altro: "))
    numeri.append(y)
    z = int(input("Dinne ancora uno: "))
    numeri.append(z)
    print("La tua lista è:")
    print(numeri)
else:
    print("Numeri non inseriti! Stringa vuota di DEFAULT impostata")

print("Cosa vuoi fare?")
print("Premi C per Create")
print("Premi R per Read")
print("Premi U per Update")
print("Premi D per Delete")
print("Premi T per Terminare")
selezione = input("Inserisci Selezione: ").upper()
if selezione == 'T' :
    print("Alla prossima!")
elif selezione == 'C' :
    numbers = []
    print("Inserisci tre nuovi numeri da mettere in lista:")
    h = int(input("Dimmi un numero: "))
    numbers.append(x)
    k = int(input("Dimmene un altro: "))
    numbers.append(y)
    w = int(input("Dinne ancora uno: "))
    numbers.append(z)
    numeri = numbers
    print("La tua nuova lista di numeri:")
    print(numeri)
elif selezione == 'R' :
    if len(numeri) == 0 :
        print("La lista è vuota! Riprova.")
    else:
        print("La tua lista è:")
        print(numeri)
elif selezione == 'U' :
    if len(numeri) == 0 :
        print("La lista è vuota! Riprova.")
    else :
        i = int(input("Qual è la posizione valore vuoi cambiare?: "))
        if i > len(numeri)-1 :
            print("Posizione non esistente")
        else:
            m = input("Cosa vuoi inserire?: ")
            numeri.insert(i, m)
            # numeri[i] = m #Forse è equivalente a insert()
            print("La tua lista ora è:")
            print(numeri)
elif selezione == 'D':
    if len(numeri) == 0 :
        print("La lista era già vuota!")
    else:
        print("La tua lista è:")
        print(numeri)
        print("Procediamo a svuotarla!")
        numeri.clear()
        #numeri = [] #Forse è equivalente per eliminare tutto il contenuto
        print("La tua lista ora è:")
        print(numeri)
else:
    print("Il tasto premuto non è corretto.")
    print("Riprova la prossima volta!")
print("Ciao")

print("")
#####################################################################################################################################################################################
print("------------------------")
print("")
'''
Esercizio 3
Realizzare una struttura condizionale con if ed else.
All'interno del ramo if, implementare la creazione di un nuovo account, richiedendo:
- nome utente
- password
- ID univoco incrementale generato dal sistema assegnato automaticamente
Nel ramo else, effettuare il controllo automatico dell'esistenza dell'account nel sistema.
Lo script deve terminare correttamente solo nel caso in cui il controllo venga superato, ovvero quando l'utente risulta registrato ed autenticato con successo.
'''

#Variabili
id = 0
users = []
usernames = []
scelta = input("DEV TEST: Vuoi inserire qualche utente il lista? [S] o [N]: ").upper()

if (scelta == "S"):
    nome1 = input("Inserisci il 1° nome in lista: ").lower()
    usernames.append(nome1)
    nome2 = input("Inserisci il 2° nome in lista: ").lower()
    usernames.append(nome2)
    nome3 = input("Inserisci il 3° nome in lista: ").lower()
    usernames.append(nome3)
    print("Gli utenti inserito sono: ")
    print(usernames)
else:
    print("Nomi non inseriti! Lista vuota di DEFAULT impostata")

#Variabili
risposta = input("Vuoi registrarti al sistema? [S] o [N]: ").upper()

if (risposta == "S"):
    nome = input("Inserisci nome: ").lower()
    if nome not in usernames:
        usernames.append(nome)
        utente_id = id + 1
        utente_nome = nome
        utente_password = input("Inserisci password: ")
        utente = (utente_id, utente_nome, utente_password)
        users.append(utente)
        print("Account creato!")
        print(utente)
        id = id + 1 #id++ Non Funziona - Genera Errore! - MA Perchè?
    else:
        print("Nome già utilizzato da un altro utente!")
elif (risposta == "N"):
    print("Allora perchà mi hai avviato?")
else:
    print("Hai sbagliato a scrivere la tua risposta.")
    print("Riprova la prossima volta!")

print("STOP")
print("")
