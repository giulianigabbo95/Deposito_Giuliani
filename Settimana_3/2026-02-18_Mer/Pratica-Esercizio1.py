'''
Scrivere un programma che genera 5 numeri casuali e li salva su un file.
L'utente dovrà cercare di indovinarne almeno 2 oppure avrà perso.

# In collaborazione con Fabio D'Alessandro, Elisabetta Carella e Stefano Romanelli
'''

#by Stefano
import random


NOME_FILE = "numeri.txt"


def scriviNumeriFile(nome_file):
    result = ""
    numeri_appoggio = []
    while True:  
        limite_numeri = int(input("Inserisci quanti numeri random vuoi generare (min 1 & max 90): ")) 
        if 90 > limite_numeri > 0:
            while limite_numeri > 0:
                numero_generato = random.randint(1, 91)
                if numero_generato not in numeri_appoggio:
                    numeri_appoggio.append(numeri_appoggio)
                    limite_numeri -= 1
            break
    for i in range(0, len(numeri_appoggio), 1):
        if i != len(numeri_appoggio) - 1:
            result += str(numeri_appoggio[i]) + ','
        else:
            result += str(numeri_appoggio[i])
    with open(f"C:\\Users\\Gahab\Documents\\GitHub\\Corso_PyML_Deposito_Studente_Giuliani\\Settimana_3\\2026-02-18_Mer\\{nome_file}", "w") as file:
        file.write(numeri_appoggio)


def leggiNumeriFile(nome_file):
    righe = []   
    with open(nome_file, "r") as file:
        contenuto = file.read()
    righe = contenuto.split(',')
    return righe

# MAIN
print("SuperEnalotto")
tentativi_rimasti = int(input("Scegli quanti tentativi vuoi fare: "))

scriviNumeriFile(NOME_FILE)
numeri_file = leggiNumeriFile(NOME_FILE)
print("Righe File: ", numeri_file)
print(type(numeri_file[0]).__name__)
print(numeri_file[0])

numeri_indovinati = 0
numeri_inseriti = []

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
    if tentativo not in numeri_inseriti:
        numeri_inseriti.append(str(tentativo))
        tentativi_rimasti -= 1
    else:
        print("Numero già inserito!")

for n in numeri_file:
    if n in numeri_inseriti:
        numeri_indovinati += 1

if numeri_indovinati >= 2:
    print("Hai vinto!")
else:
    print("Hai perso!")
    
    

#by Fabio
import random as r

FILE_NAME = r"Corso_Python_02-26/18-02-26/Mattina/numbers.txt"

# generazione dei numeri
def generate_numbers():
    return [r.randint(1, 100) for _ in range(5)]

# funzioni per scrivere
def write_file(numbers):
    with open(FILE_NAME, "w") as f:
        f.write(numbers)

# funzione per leggere
def read_file():
    with open(FILE_NAME,"r") as file:
        contenuto = file.read()
    return contenuto


# funzione principale del programma che gestisce la logica del gioco
def main():
    numbers =",".join([str(n) for n in generate_numbers()])
    write_file(numbers)


    # utilizzo una list comprehension per leggere e convertire i numeri in interi
    cont = read_file()
    listaR = cont.split(",")
    matrice = [int(num) for num in listaR]
    
    
    print("Indovina almeno 2 dei numeri generati!")
    # l'utente ha 5 tentativi per indovinare i numeri
    x = 0
    while x < 5:
        if x < 0: x = 0
        guess = input(f"tentativo {x+1} - Inserisci un numero: ")
        try:
            guess = int(guess)  # converto l'input in un intero
        except ValueError as e:
            print(f"Per favore, inserisci un numero valido.", e)
            continue  # salta al prossimo tentativo se l'input non è un numero
        if guess in matrice:
            print("Hai indovinato un numero!")
            matrice.remove(guess)  # rimuove il numero indovinato per evitare duplicati
        else: print("Numero sbagliato!")
        x += 1  # incrementa il contatore dopo ogni tentativo

    if len(matrice) <= 3:  # se sono stati indovinati almeno 2 numeri
        print("Hai vinto!")
    else: print("Hai perso! I numeri erano:", matrice)


# MAIN
# esecuzione del programma
main()