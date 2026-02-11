'''
Realizzare un programma per la gestione di pacchi in un magazzino.
Il sistema deve essere composto da tre classi:

a. Classe Pacco
Ogni pacco deve avere:
    - codice, una stringa che identifica il pacco
    - peso, un numero
    - stato, una stringa che può assumere valori come:
        . in magazzino
        . in consegna
        . consegnato
La classe deve fornire:
    -un metodo per stampare le informazioni del pacco
    -un metodo per cambiare lo stato del pacco

b. Classe Magazzino
Il magazzino deve contenere una lista di pacchi e permettere di:
    - aggiungere un pacco
    - cercare un pacco dato il suo codice
    - mostrare tutti i pacchi che si trovano in un certo stato

c. Classe GestorePacchi
Questa classe deve utilizzare il magazzino e permettere di:
    - mettere un pacco in consegna
    - segnare un pacco come consegnato
    - calcolare il peso totale dei pacchi non ancora consegnati

Nel programma principale:
    - creare almeno 5 pacchi
    - inserirli nel magazzino
    - cambiare lo stato di alcuni pacchi:
        . almeno uno "in consegna"
        . almeno uno "consegnato"
    - stampare:
        . elenco dei pacchi "in magazzino"
        . elenco dei pacchi "in consegna"
        . peso totale dei pacchi non consegnati
'''

print("")
print("START")

###-CLASSI-###
class Pacco:
    def __init__(self, codice, peso):
        self.codice = codice
        self.peso = peso
        self.stato = "magazzino"        # ENUM ?

    def mostraInfo(self):
        print("Codice:", self.codice, "Peso:", self.peso, "Stato:", self.stato)

    def cambiaStato(self, nuovo_stato):
        self.stato = nuovo_stato

class Magazzino:
    def __init__(self):
        self.pacchi = []

    def aggiungiPacco(self, pacco):
        self.pacchi.append(pacco)

    def cercaPacco(self, codice):
        for p in len(self.pacchi):
            if self.pacchi[p].codice == codice:
                return self.pacchi[p]
        return None

    def mostraPacchiOrdinatiStato(self, stato):
        for p in len(self.pacchi):
            if self.pacchi[p].stato == stato:
                self.pacchi[p].mostraInfo()

class GestorePacchi:
    def __init__(self, magazzino):
        self.magazzino = magazzino

    def avviaConsegna(self, codice):
        pacco = self.magazzino.cercaPacco(codice)
        if pacco != None:                           # if oggetto generico exists() return True ?
            pacco.cambiaStato("consegna")

    def completaConsegna(self, codice):
        pacco = self.magazzino.cercaPacco(codice)
        if pacco != None:
            pacco.cambiaStato("consegnato")

    def pesoPacchiNonConsegnati(self):
        totale = 0
        i = 0
        while i < len(self.magazzino.pacchi):
            pacco = self.magazzino.pacchi[i]
            if pacco.stato != "consegnato":
                totale = totale + pacco.peso
            i += 1
        return totale

###-MAIN-###
magazzino1 = Magazzino()
gestore1 = GestorePacchi(magazzino1)

pacco0101 = Pacco("P_01-01", 10)
pacco0102 = Pacco("P_01-02", 5)
pacco0103 = Pacco("P_01-03", 8)
pacco0104 = Pacco("P_01-04", 12)
pacco0105 = Pacco("P_01-05", 7)

magazzino1.aggiungiPacco(pacco0101)
magazzino1.aggiungiPacco(pacco0102)
magazzino1.aggiungiPacco(pacco0103)
magazzino1.aggiungiPacco(pacco0104)
magazzino1.aggiungiPacco(pacco0105)

gestore1.avviaConsegna("P_01-01")
gestore1.avviaConsegna("P_01-02")
gestore1.completaConsegna("P_01-02")

print("Pacchi in magazzino:", magazzino1.mostraPacchiOrdinatiStato("magazzino"))
print("Pacchi in consegna:", magazzino1.mostraPacchiOrdinatiStato("consegna"))
print("Pacchi in consegna:", magazzino1.mostraPacchiOrdinatiStato("ajeje"))       # Da errore MA con l'ENUM non dovrebbe (credo)

print("\nPeso totale pacchi non consegnati:", gestore1.pesoPacchiNonConsegnati())


print("STOP")
print("")
