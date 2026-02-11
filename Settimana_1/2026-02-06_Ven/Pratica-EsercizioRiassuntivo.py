'''
Esercizio generato con ChatGPT con prompt: Dammi un esercizio in Python che racchiuda:
    - Collezioni
    - Controllori di flusso
    - Cicli Funzioni 
    - Generatori 
    - Decoratori
    
Scrivi un programma che analizzi le vendite giornaliere di un negozio.
Ogni vendita è rappresentata da una tupla (nome_prodotto, prezzo) e tutte le vendite devono essere salvate in una lista.
Il programma deve permettere all'utente di inserire le vendite tramite un ciclo while, chiedendo il nome del prodotto e il prezzo; l'inserimento termina quando il nome del prodotto è "stop". Se il prezzo inserito non è numerico o è minore o uguale a zero, la vendita deve essere ignorata.
Scrivi una funzione generatore che, data la lista delle vendite, restituisca una alla volta solo le vendite valide (con prezzo maggiore di zero). 
Scrivi poi tre funzioni di analisi che utilizzino il generatore: una per calcolare l'incasso totale, una per calcolare il numero di vendite valide e una per determinare il prodotto più costoso.
Scrivi infine un decoratore che stampi un messaggio prima e dopo l'esecuzione di una funzione e usalo per decorare una funzione principale che richiami le funzioni di analisi e stampi i risultati.
'''

#-FUNZIONI-#
# Generatore: restituisce solo le vendite valide
def venditeValide(vendite):
    for vendita in vendite:
        if vendita[1] > 0:
            yield vendita


def incassoTotale(vendite):
    totale = 0
    for u, prezzo in venditeValide(vendite):
        totale += prezzo
    return totale


def numeroVendite(vendite):
    count = 0
    for u in venditeValide(vendite):
        count += 1
    return count


def prodottoCostoso(vendite):
    max_nome = ""
    max_prezzo = 0

    for nome, prezzo in venditeValide(vendite):
        if prezzo > max_prezzo:
            max_prezzo = prezzo
            max_nome = nome

    return max_nome, max_prezzo


# Decoratore
def logger(funzione):
    def wrapper(vendite):
        print("Inizio analisi")
        funzione(vendite)
        print("Fine analisi")
    return wrapper


@logger
def analizza_vendite(vendite):
    print("Incasso totale:", incassoTotale(vendite))
    print("Numero vendite:", incassoTotale(vendite))

    nome, prezzo = prodottoCostoso(vendite)
    print("Prodotto più costoso:", nome, prezzo)


####-MAIN-####
vendite = []

while True:
    nome = input("Nome prodotto (stop per terminare): ").upper()
    if nome == "STOP":
        break

    prezzo_input = input("Prezzo: ")

    if prezzo_input.replace(".", "", 1).isdigit():
        prezzo = float(prezzo_input)

        if prezzo > 0:
            vendite.append((nome, prezzo))
        else:
            print("Prezzo non valido")
    else:
        print("Prezzo non valido")

analizza_vendite(vendite)