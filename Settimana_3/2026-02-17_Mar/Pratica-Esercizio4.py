'''
Scrivere un programma che genera 5 numeri casuali e li salva su un file.
L'utente dovrà cercare di indovinarne almeno 2 oppure avrà perso.

# In collaborazione con Fabio D'Alessandri e Elisabetta Carella
'''
import random

def scriviNumeriFile(nome_file):
    with open("C:\\Users\\Gahab\Documents\\GitHub\\Corso_PyML_Deposito_Studente_Giuliani\\Settimana_3\\2026-02-17_Mar\\nome_file", "w") as file:
        numeri_appoggio = []
        while True:  
            limite_numeri = int(input("Inserisci uanti numeri random vuoi generare (min 1 & max 90): ")) 
            if 90 > limite_numeri > 0:
                while limite_numeri > 0:
                    numero_generato = random.randint(1, 91)
                    if numero_generato not in numeri_appoggio:
                        numeri_appoggio.append(numero_generato)
                        file.write(str(numero_generato) + "\n")
                        limite_numeri -= 1
                break

def leggiNumeriFile(nome_file):
    numeri = []
    with open(nome_file, "r") as file:
        for riga in file:
            numeri.append(int(riga))
    return numeri



numeri_giocati = []
tentativi_rimasti = int(input("Scegli quanti tentativi vuoi fare: "))

scriviNumeriFile("file.txt")
numeri_file = leggiNumeriFile("file.txt")
numeri_indovinati = 0

while tentativi_rimasti > 0:
    try:
        while True:
            tentativo = int(input("Inserici il numero: "))
            if 90 > tentativo > 0:
                break
            else:
                print("Numero fuori range!")
    except:
        print("errore!")
    if tentativo not in numeri_giocati:
        numeri_giocati.append(tentativo)
        tentativi_rimasti -= 1
        print(tentativi_rimasti)
    else:
        print("Numero già inserito!")

print(numeri_file)

for n in numeri_giocati:
    if n in numeri_file:
        numeri_indovinati += 1
        print(n)

if numeri_indovinati >= 2:
    print("Hai vinto!")
else:
    print("Hai perso!")