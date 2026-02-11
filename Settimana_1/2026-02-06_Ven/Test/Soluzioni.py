'''
1.  Inserisci Cognome nome ed email:
        Gabriele Giuliani giulianigabbo95@gmail.com

2.  Quale di queste è una delle regole fondamentali dell'OOP: (1 punto)
    Selezionare 3 opzioni.
        [X] - Astrazione
            - Proprietarietà
            - Modularità
        [X] - Polimorfismo
            - Ciclicità
        [X] - Incapsulamento
            - Riusabilità
        [X] - Ereditarietà

3.  Cos'è una collezione? Quali conosci e quali caratteristiche hanno? (1 punto)
        Una collezione è un costrutto base di molti linguaggi di programmazione tra cui appunto Python, nel quale abbiamo:
            - Liste: ordinate, modificabili, con possibili duplicati (Es: tsil = [2, 1, 3])
            - Tuple: ordinate, NON modificabile (Es: alput = (1, 4, 2), a volte senza parentesi)
            - Insiemi: non ordinate, senza duplicati (Es: Ates = set([1, 2, 3]) / Btes = {3, 4, 5})
        Servono per immagazzinare, organizzare e gestire dati in un'unica variabile.
        NB: Ordinata significa che mantiene l'ordine degli elementi in base alla loro posizione di inserimento.

4.  Quale tipo è "speciale" in Python? (1 punto)
        [X] - Strighe
            - Bool
            - Char
            - Float

5.  Cos'è Python? quali caratteristiche ha? (1 punto)
        Python è n linguaggio di programmazione con le seguenti caratteristiche:
            - interpretato perchè il codice viene eseguito riga per riga da un interprete senza bisogno di una fase di compilazione precedente, rendendo così più sicuro che il codice stesso venga eseguito
            - OOP / orientato agli oggetti perchè supporta classi, astrazione, ..., che permettono di rappresentare meglio il mondo reale
            - fortemente dinamico perchè il tipo delle variabili viene assegnato automaticamente e può cambiare durante l'esecuzione del programma
            - ad alto livello perchè è simile al linguaggio umano 

6.  Cos'è una funzione incorporata? (1 punto)
            - Una funzione che richiede richiami
            - Un gruppo di funzioni delle collezioni
            - Una funzione delle stringhe
        [X] - Una funzione che non ha richiami

7.  Cos'è una variabile e da quali parti è definita? Quali categorie e tipi esistono di variabile? (1 punto)
        Una variabile è uno spazio di memoria per immagazzinare dei dati, ed è definita da tre punti:
            - nome (pippo)
            - valore (23)
            - tipo (int, float, double, string, bool, list, ...) [implicito]
        Non può contenere spazi ma deve contenere lettere.
        Non può iniziare con i numeri ma può contenerli.
        Può contenere "underscores" (_) e anche iniziare, ma si usa solo in casi particolari. 
        Es: [string] nome_Paapero1 = "paperinik"

8.  Come si chiama una funzione che non può valorizzare una variabile? (1 punto)
            - Una funzione senza parametri
            - Non esiste in Python
        [X] - Una funzione senza return
            - Una funzione con return

9.  Cos'è una funzione? cosa dimostra implicitamente? Quali tipi ne esistono? cosa sono i parametri? e gli argomenti? (1 punto)
        Una funzione è un blocco di codice riutilizzabile che esegue un'operazione.
        Necessita della sintassi "def" e di un nome.
        Può restituire un valore, numerico, testuale, booleano, ..., o eseguire una procedura senza restituire nulla.
        Può avere degli argomenti, cioè dei valori passati quando viene richiamata, e dei parametri, cioè dei valori definiti e usati solo all'interno della funzione stessa.
        Es: def aggiungi_numero(x:int, y:int)

10. Cos'è github? (1 punto)
            - Un prodotto per i DB
        [X] - Un sistema di versionamento e un prodotto
            - Una tecnologia di versionamento
            - Un insieme di funzioni di Python 

11. Cos'è SQL e a cosa serve? (1 punto)
        SQL sta per Structured Query Language ed è un linguaggio di interrogazione (non di programmazione) per interrogare e modificare database relazionali.
        Es: SELECT first_name AS Nome, last_name AS Cognome FROM studenti_corso

12. Cos'è un query? (1 punto)
            - Una funzione di sql
            - Una chiamata al backend
        [X] - Un interrogazione al DB
            - Nessuna delle precedenti

13. Cos'è un operatore? Cosa cambia tra logico e aritmetico? Spiegami quelli che conosci. (1 punto)
        Un operatore è un simbolo che permette di eseguire operazioni.
            - Aritmetici: +, -, *, /, %
            - Logici: and (&&), or (||), not (!=), equal (==)

14. Quale di questi elementi può cambiare un ciclo per UN solo giro (1 punto)
            - Break
        [X] - Continue 
            - Pass
            - Splat

15. Cos'è il controllo di flusso? Quali famiglie abbiamo in questo capo e quali comandi appartengono a queste famiglie? (1 punto)
        Il controllo di flusso stabilisce l'ordine di esecuzione delle istruzioni nel codice.
            - Condizionali: if, elif, else, match
            - Cicli: for, while
            - Interruzione: break, continue, pass

16. Quale di questi elementi non è un controllore del flusso? (1 punto)
            - For
        [X] - List[]
            - If
            - Match

17. Esercizio 1: Condizioni e cicli (1 punto)
    Chiedi all'utente di inserire un numero intero positivo. 
    Usa un ciclo for per stampare tutti i numeri da 1 fino al numero inserito. 
    Per ogni numero: 
        stampa "pari" se il numero è pari 
        stampa "dispari" se il numero è dispari 
    Se l'utente inserisce un numero minore o uguale a zero, stampa un messaggio di errore.

18. Esercizio 2: Funzioni e Liste (1 punto)
    Definisci una funzione chiamata conta_vocali. 
    La funzione deve: 
        ricevere una stringa come parametro 
        contare quante vocali contiene (a, e, i, o, u) 
        restituire il numero totale di vocali 
    Nel programma principale: 
        chiedi all'utente di inserire una parola 
        chiama la funzione 
        stampa il numero di vocali trovate

19. Com'è andata?
    9/10
    
20. EXTRA: Fai un meme sul corso
    Base: The Most Interesting Man in the World
    I don't always program well in Python
    But when I do, a handless Python writes on the keyboard better than I do


Dubbi:
    2. Quale di queste è una delle regole fondamentali dell'OOP - non ho potuto selezionare anche Astrazione sul form
    
'''

# 17
#Variabili
numero = int(input("Inserisci un numero intero positivo: "))

if numero <= 0:
    print("il numero deve essere positivo")
else:
    for num in range(1, numero + 1, 1):
        if num % 2 == 0:
            print("Il numero è pari:", num)
        else:
            print("Il numero è dispari:", num)


#18
def contaVocali(p):
    vocali = ["a", "e", "i", "o", "u"]
    count = 0

    for lettera in p:
        if lettera in vocali:
            count += 1

    return count

####-MAIN-####
#Variabili
parola = input("Inserisci una parola: ").lower()
risultato = contaVocali(parola)

print("Numero di vocali:", risultato)