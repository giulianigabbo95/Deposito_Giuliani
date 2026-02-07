'''
Esercizio 1
Scrivi un programma che:
1. Chiede all'utente se vuole inserire un numero o una stringa.
2. Se viene inserito un numero, il programma determina se è pari o dispari e stampa il risultato.
3. Al termine, chiede all'utente se desidera ripetere l'operazione
'''

while True:
#1 - Chiede all'utente se vuole inserire un numero o una stringa.
    #Variabili
    scelta = input("Vuoi inserire un numero o una stringa? [NUM] o [STR]: ").upper()
    
    print("")
#2 - Se viene inserito un numero, il programma determina se è pari o dispari e stampa il risultato.
    match scelta:
        case "NUM":
            num = int(input("Inserisci un numero: "))
            if num % 2 == 0:
                print("Il numero è pari")
            else:
                print("Il numero è dispari")
        case "STR":
            str = input("Inserisci una stringa: ")
            print("Stringa inserita:", str)
            '''
            #Non esplicitamente richiesta
            lung = len(str)
            if lung % 2 == 0:
                print("La stringa ha lunghezza pari")
            else:
                print("La stringa ha lunghezza dispari")
            '''
        case _:
            print("Hai sbagliato a inserire!")

#3 - Al termine, chiede all'utente se desidera ripetere l'operazione
    selezione = input("Vuoi ricominciare? [S] o [N]: ").upper()
    if selezione == "N":
        break
    elif selezione == "S":
        pass
    else:
        print("Hai sbagliato a inserire! Ricomincio")
    
    print("")