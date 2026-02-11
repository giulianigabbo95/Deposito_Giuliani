'''
Decoratori
Funzione che modifica il comportamento di un'altra funzione o metodo senza modificarne direttamente il codice. 
Utilizzate per aggiungere funzionalità extra come logging, controllo degli accessi, caching, etc... 
Si applicano anteponendo il simbolo @ al nome del decoratore sopra la funzione da decorare.
'''

#-FUNZIONI-#
def decoratore(funzione):
    def wrapper():
        print("Prima dell'esecuzione della funzione")
        funzione()
        print("Prima dell'esecuzione della funzione")
    return wrapper

@decoratore
def saluta():
    print("Ciao!")
    
@decoratore
def contatore():
    print(100)

def decoratore_con_argomenti(funzione):
    def wrapper(*args, **kwargs):
        print("Prima")
        risultato = funzione(*args, **kwargs)
        print("Dopo")
        return risultato
    return wrapper

@decoratore_con_argomenti
def somma(a, b):
    print(a+b)
    return a + b

# DECORATORI + GENERATORI
# - Generatori: yield, yield from, generator expression
# - Decoratori: base, con parametri, con argomenti, stacking (applicato a funzioni che consumano generatori)

####-MAIN-####
print("Il risultato è ", somma(3, 4))
saluta()

def logger(funzione):
    def wrapper(*args, **kwargs):
        print(f"Chiamata a {funzione.__name__} con argomenti: {args} e {kwargs}")
        risultato = funzione(*args, **kwargs)
        print(f"Risultato di {funzione.__name__}: {risultato}")
        return risultato
    return wrapper
    
#LOGGER
@logger
def moltiplica(a, b):
    return a * b

# Chiamata alla funzione decorata
print("La moltiplicazione è:", moltiplica(3, 4))