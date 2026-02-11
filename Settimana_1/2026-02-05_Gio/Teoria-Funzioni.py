'''
Funzioni
Blocchi di codice autonomi che eseguono una determinata operazione.
Consentono di organizzare il codice in unità modulari, possono essere richiamate e riutilizzate in diverse parti di un programma. 
Aiutano a scrivere codice più leggibile, comprensibile e manutenibile.
'''

#Definizioni di Funzioni
def saluta(nome):
    print("Ciao", nome)
    print("Benvenuto!")
    
def saluta(nome, messaggio = "Ciao"):
    print(f"{messaggio}{nome}!")
    
def somma(a, b):
    risultato = a + b
    print("Lǽsomme è:", risultato)
    
def stampaSingola_lista(listaX:list):
    for i in listaX:
        print(listaX)
    print("Fine")
        
def quadrato(numero):
    return numero*numero

def ricalcoloValore(x:int):
    return x*7


####-MAIN-####
saluta("Alice")

saluta("Luigi", messaggio = "Buongiorno")

res = somma(5, 3)
print(res)

lista1 = [* range(0, 50, 2)]
stampaSingola_lista(lista1)

lista2 = [* range(1, 30, 3)]
stampaSingola_lista(lista2)

print("L'elevazioe alla seconda di quattro è:", quadrato(4))

numero = 10
print("Il numero è:", numero)
numero = ricalcoloValore(numero)
print("Il ricacolo è:", numero)