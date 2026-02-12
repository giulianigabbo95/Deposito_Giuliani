'''
Realizzare una classe `ContoBancario` che incapsula le informazioni di un conto corrente e permette di gestire il saldo in modo sicuro.
L0obiettivo è utilizzare l0incapsulamento per impedire accessi o modifiche dirette non autorizzate al saldo.

Classe ContoBancario
    Attributi privati:
        - __titolare, stringa che rappresenta il nome del titolare
        - __saldo, numero decimale che rappresenta il saldo del conto

    Metodi pubblici:
        - deposita(importo), aggiunge un importo al saldo solo se l'importo è positivo
        - preleva(importo), sottrae un importo dal saldo solo se l'importo è positivo e se il saldo è sufficiente
        - visualizza_saldo(), restituisce il saldo attuale e non permette la modifica diretta

    Sicurezza
        - Validare che gli importi non siano negativi
        - Creare getter e setter per il titolare
        - Il titolare non può essere stringa vuota
'''

class ContoBancario:

    def __init__(self, titolare, saldo_iniziale):
        self.set_titolare(titolare)
        self.__saldo = 0

        if saldo_iniziale >= 0:
            self.__saldo = saldo_iniziale
        else:
            print("Saldo iniziale non valido. Impostato a 0.")
        
    def depositaCash(self, importo):
        if importo > 0:
            self.__saldo += importo
            print("Deposito effettuato.")
        else:
            print("Importo non valido.")

    def prelevaCash(self, importo):
        if importo <= 0:
            print("Importo non valido.")
            return
        if importo > self.__saldo:
            print("Fondi insufficienti.")
            return
        self.__saldo -= importo
        print("Prelievo effettuato.")
     
    def visualizzaSaldo(self):
        return self.__saldo 
     
    # Getter titolare
    def get_titolare(self):
        return self.__titolare

    # Setter titolare
    def set_titolare(self, nuovo_titolare):
        if isinstance(nuovo_titolare, str) and nuovo_titolare.strip() != "":
            self.__titolare = nuovo_titolare
        else:
            print("Nome titolare non valido.")

conto1 = ContoBancario("")

conto2 = ContoBancario("Mario Rossi", 1000)

print("Titolare:", conto2.get_titolare())
print("Saldo iniziale:", conto2.visualizzaSaldo())

deposito = int(input("Quando vuoi depositare?"))
conto2.depositaCash(deposito)
print("Dopo il deposito di", deposito, "il saldo è:", conto2.visualizzaSaldo())

prelievo = int(input("Quando vuoi prelevare?"))
conto2.prelevaCash(prelievo)
print("Dopo il prelievo di", prelievo, "il saldo è:", conto2.visualizzaSaldo())

conto2.prelevaCash(2000)  # fondi insufficienti
conto2.depositaCash(-50)  # importo non valido
