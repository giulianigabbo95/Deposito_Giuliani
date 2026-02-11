'''
Esercizio 1
Scrivi un programma che chieda all'utente la sua età.
Se l'età è inferiore a 18 anni, il programma dovrebbe stampare "Mi dispiace, non puoi vedere questo film". 
Altrimenti, dovrebbe stampare "Puoi vedere questo film".
'''

#Variabili
eta = int(input("Dimmi quanti anni hai: "))
maggiorenne = False

if eta >=18:
    maggiorenne = True
elif eta < 18:
    maggiorenne = False
else:
    print("Impossibile tu non abbia età!")

match maggiorenne:
    case False:
        print("Mi dispiace, non puoi vedere questo film")
    case True:
        print("Puoi vedere questo film")

#####################################################################################################################################################################################

print("")
'''
Esercizio 2
Scrivi un programma che chieda all'utente di inserire due numeri e un'operazione da eseguire tra addizione (+), sottrazione (-), moltiplicazione (*) e divisione (/).
Il programma dovrebbe poi eseguire l'operazione e stampare il risultato. Tuttavia, se l'utente tenta di dividere per zero, il programma dovrebbe stampare "Errore: Divisione per zero". 
Se l'operazione inserita non è riconosciuta, dovrebbe stampare "Operazione non valida".
'''

#Variabili
x = int(input("Dimmi il 1° numero: "))
y = int(input("Dimmi il 2° Numero: "))
scelta = input("Inserisci Operatore: ")

match scelta:
    case "+":
        print(x + y)
    case "-":
        print(x - y)
    case "*":
        print(x * y)
    case "/":
        if y == 0 :
            print("Errore: Divisione per Zero")
        else:
            print(x / y)
    case _:
        print("Operazione non esistente!")

#####################################################################################################################################################################################

print("")
'''
Esercizio 3 (Verde)
Scenario:
    Realizzare un programma in Python che simuli un semplice sistema di login.
    Il programma deve permettere all'utente di inserire username e password, verificarne la correttezza e, in caso di successo, consentire la modifica di un dato personale tramite una domanda segreta.

Requisiti:
    1. Inserimento dati utente
        Il programma richiede all'utente di inserire:
        - nome utente
        - password
    2. Verifica delle credenziali
        Il programma confronta i dati inseriti con una coppia di credenziali predefinite (hardcoded).
        Esempio:
            username = admin
            password = 12345
    3. Gestione dell'output
        Se le credenziali sono corrette, visualizzare un messaggio di benvenuto.
        In caso contrario, mostrare un messaggio di errore.
    4. Modifica dati tramite domanda segreta
        Dopo il login, permettere all'utente di scegliere una tra due domande segrete:
        Qual è il tuo colore preferito?
        Qual è il tuo animale preferito?
        L'utente dovrà fornire una risposta, che verrà salvata o modificata tramite una condizione interna.
'''

#Variabili

username_corretto = "admin"
password_corretta = "12345"
#1 - Inserimento dati utente
username = input("Inserisci username: ")
password = input("Inserisci password: ")

#2 - Verifica delle credenziali
if username == username_corretto and password == password_corretta:

#3 - Gestione dell'output
    print("Login effettuato con successo", username)
    
#4 - Modifica dati tramite domanda segreta
    print("Scegli una domanda segreta!")
    print("[1] Qual è il tuo colore preferito?")
    print("[2] Qual è il tuo animale preferito?")

    scelta = int(input("Inserisci 1 o 2: "))

    if scelta == 1:
        risposta = input("Qual è il tuo colore preferito? ")
        print("Risposta salvata:", risposta)
    elif scelta == 2:
        risposta = input("Qual è il tuo animale preferito? ")
        print("Risposta salvata:", risposta)
    else:
        print("Scelta non valida")
        
    # Si potrebbe fare altrettanto con username e password
else:
    print("Errore: username o password non corretti")