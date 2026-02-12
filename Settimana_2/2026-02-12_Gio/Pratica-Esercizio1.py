'''
Creare un sistema che dimostri l'uso del polimorfismo attraverso diverse classi che rappresentano metodi di pagamento.

a. Classe base: MetodoPagamento
    Definire un metodo effettuaPagamento(importo) che dovrà essere implementato da tutte le sottoclassi.

b. Classi derivate:
    - CartaDiCredito: Implementa effettua_pagamento(importo) simulando un pagamento con carta di credito.
    - PayPal: Implementa effettuaPagamento(importo) simulando un pagamento tramite PayPal.
    - BonificoBancario: Implementa effettuaPagamento(importo) simulando un pagamento con bonifico bancario.

c. Classe GestorePagamenti
    Deve accettare un'istanza di MetodoPagamento (o di una sua sottoclasse) e utilizzarla per effettuare pagamenti, senza conoscere i dettagli specifici del metodo di pagamento utilizzato.
'''

class MetodoPagamento:
    def effettuaPagamento(self, importo):
        pass

class CartaDiCredito(MetodoPagamento):
    def effettuaPagamento(self, importo):
        print(f"Pagamento di {importo}€ effettuato con Carta di Credito")

class PayPal(MetodoPagamento):
    def effettuaPagamento(self, importo):
        print(f"Pagamento di {importo}€ effettuato con PayPal")

class BonificoBancario(MetodoPagamento):
    def effettuaPagamento(self, importo):
        print(f"Pagamento di {importo}€ effettuato con Bonifico Bancario")

class GestorePagamenti:
    def __init__(self):
        self.metodo = None
        self.totale = 0
    
    def impostaMetodo(self, metodo):
        self.metodo = metodo
    
    def pagaSoldi(self, importo):
        if self.metodo:
            self.metodo.effettuaPagamento(importo)
            self.totale += importo
        else:
            print("Nessun metodo di pagamento selezionato!")

# Programma principale
gestore = GestorePagamenti()
carta = CartaDiCredito()
paypal = PayPal()
bonifico = BonificoBancario()

while True:
    print("Sistema RubaSoldi")
    print("Premi 1 per Scelta Metodo")
    print("Premi 2 per Effettua Pagamento")
    print("Premi 3 per Calcola Totale Pagato")
    print("Premi 4 per Esci")
    
    scelta = input("Scegli che vuoi fare: ")
    
    match scelta:
        
        case "1":
            print("")
            print("Metodo di scam")
            print("Premi 1 per Usa Carta di Credito")
            print("Premi 2 per Usa PayPal")
            print("Premi 3 per Usa Bonifico Bancario")
            
            tipo = input("Scegli il metodo di scam: ")
            
            match tipo:
                case "1":
                    gestore.impostaMetodo(carta)
                    print("Metodo impostato: Carta di Credito")
                case "2":
                    gestore.impostaMetodo(paypal)
                    print("Metodo impostato: PayPal")
                case "3":
                    gestore.impostaMetodo(bonifico)
                    print("Metodo impostato: Bonifico Bancario")
                case _:
                    print("Dillo che non vuoi pagare! Avresti ragione!")
        
        case "2":
            importo = float(input("Inserisci l'importo da donare alla tua sugar mommy: €"))
            gestore.pagaSoldi(importo)
        
        case "3":
            print(f"Totale complessivo scammato: {gestore.totale}€")
        
        case "4":
            print("Grazie per esserti fatto scammare!")
            break
        
        case _:
            print("Ma sei scemo?")
    
    print("")