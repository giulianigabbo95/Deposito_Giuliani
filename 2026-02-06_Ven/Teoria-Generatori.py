'''
Generatori
Speciale classe di funzioni che permettono di iterare su una serie di valori, ma invece di restituirli tutti in una volta, lo fanno uno alla volta.
'''

#-FUNZIONI-#
def fibonacci(n:int):
    a = 0
    b = 1
    #Scrviere a, b = 0, 1 è uguale a dichiarare le variabili separatamente
    
    while a < n:
        # "yield" è la parola chiave che trasforma una funzione in un generatore. 
        # Restituisce un valore e sospende l'esecuzione della funzionemantenendone lo stato locale
        # Quando il generatore viene richiamato, riprende l'esecuzione esattamente dal punto in cui si era interrotto
        yield a
        a, b = b, a + b
        
def contatoreFinoA(n:int):
    # Generatore che produuce 1, 2, 3, ..., n
    i = 1
    while i <= n:
        yield i
        i += 1
         
def catenaGeneratori():
    # Prima prodice 1..3, poi 10..12
    yield from range(1, 4)
    yield from range(10, 13)


####-MAIN-####
for x in list(fibonacci(10)):
    print(x)
    lista = []
    lista.append(x*2)
print(list(catenaGeneratori()))


### Funzioni come oggetti di prima classe: 
# Le funzioni sono oggetti di prima classe, il che significa che possono essere passate come argomenti, restituite da altre funzioni o assegnate a variabili.
# Questo è ciò che consente ai decoratori di funzionare.

### Funzioni annidate:
# I decoratori spesso utilizzano funzioni annidate, cioè funzioni definite all'interno di altre funzioni, per eseguire del codice aggiuntivo prima o dopo la funzione decorata.

### Restituzione di una funzione modificata:
# I decoratori restituiscono una nuova funzione che sostituisce quella originale, permettendo di modificare il comportamento senza toccare il codice della funzione decorata.

### Uso di *args e **kwargs:
# Sintassi usata per garantire che il decoratore possa gestire funzioni di qualsiasi tipo, con qualsiasi numero di parametri.

### Uso di @decoratore:
# Sintassi abbreviata per applicare un decoratore a una funzione. 
# È equivalente a scrivere funzione = decoratore(funzione)