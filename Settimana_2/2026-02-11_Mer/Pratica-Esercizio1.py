'''
Realizzare un programma per la gestione dei membri di una squadra di calcio.
Il sistema deve utilizzare il concetto di ereditarietà.

Il sistema deve essere composto da una classe base e più classi derivate:
a. Classe MembroSquadra
    Ogni membro deve avere:
        - nome, una stringa
        - eta, un numero intero
    La classe deve fornire:
        - un metodo descrivi() che stampa una descrizione generale del membro
b. Classe Giocatore (derivata da MembroSquadra)
    Il giocatore deve avere:
        - ruolo (es. attaccante, difensore, portiere)
        - numero_maglia
    La classe deve fornire:
        - un metodo gioca_partita() che descrive un'azione durante la partita
c. Classe Allenatore (derivata da MembroSquadra)
    L'allenatore deve avere:
        - anni_di_esperienza
    La classe deve fornire:
        - un metodo dirige_allenamento() che descrive come conduce l'allenamento
d. Classe Assistente (derivata da MembroSquadra)
    L'assistente deve avere:
        - specializzazione (es. fisioterapista, analista)
    La classe deve fornire:
        - un metodo supporta_team() che descrive il tipo di supporto fornito alla squadra

Nel programma principale:
    Creare almeno:
        - un giocatore
        - un allenatore
        - un assistente
    Chiamare i metodi specifici di ciascun ruolo
'''

#CLASSI
class Squadra:
    def __init__(self, nome):
        self.nome = nome
        self.giocatori = []
        self.staff = []
        self.allenatore = None
        
    def aggiungiGiocatore(self, giocatore):
        if giocatore.squadra is not None:                   # Controllo se è già in una squadra
            print("Il giocatore è già in una squadra.")
            return
        if len(self.membri_giocanti) >= 25:                 # Controllo limite 25 giocatori 
            print("La squadra ha già 25 giocatori.")
            return
        self.giocatori.append(giocatore)                    # Inserimento giocatore 
        giocatore.squadra = self
        print("Giocatore aggiunto alla squadra", self.nome)
        
    def aggiungiAllenatore(self, membro):
        if membro.squadra is not None:
            print("Il membro è già in una squadra.")
            return
        self.membri_dirigenza.append(membro)
        membro.squadra = self
        print("Membro dirigenza aggiunto alla squadra", self.nome)
        
    def aggiungiAllenatore(self, membro):
        if membro.squadra is not None:
            print("Il membro è già in una squadra.")
            return
        self.membri_dirigenza.append(membro)
        membro.squadra = self
        print("Membro dirigenza aggiunto alla squadra", self.nome)

class MembroSquadra:
    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.squadra = None                 # Non lo assegno a nessuna squadra quando lo creo

    def descriviMembro(self):
        print("Nome:", self.nome, "Età:", self.eta)

class Giocatore(MembroSquadra):
    def __init__(self, nome, eta, squadra, ruolo, numero_maglia):
        super().__init__(nome, eta, squadra)
        self.ruolo = ruolo
        self.numero_maglia = numero_maglia

    def giocaPartita(self):
        print(self.nome, "sta giocando come", self.ruolo, "con il numero", self.numero_maglia)
        
    # Override
    def descriviMembro(self):
        super().descriviMembro()
        print("Nome:", self.nome, "Età:", self.eta, "Ruolo:", self.ruolo, "Numero:", self.numero_maglia)

class Allenatore(MembroSquadra):
    def __init__(self, nome, eta, anni_esperienza):
        super().__init__(nome, eta)
        self.anni_esperienza = anni_esperienza

    def dirigeAllenamento(self):
        print(self.nome, "dirige l'allenamento con", self.anni_esperienza, "anni di esperienza")

class Assistente(MembroSquadra):
    def __init__(self, nome, eta, specializzazione):
        super().__init__(nome, eta)
        self.specializzazione = specializzazione

    def supportaTeam(self):
        print(self.nome, "supporta il team come", self.specializzazione)


###-MAIN-###
squadra = Squadra("ASRoma")

player_asroma_1 = Giocatore("Francesco", "Totti", 47, "Attaccante", 10)
player_asroma_1 = Giocatore("Daniele", "De Rossi", 42, "Attaccante", 15)
trainer_asroma = Allenatore("Spalletti", 50, 20)
steward_arsoma = Assistente("Luca", "Verdini", 35, "Fisioterapista")

player_asroma_1.descriviMembro()
player_asroma_1.giocaPartita()

trainer_asroma.descriviMembro()
trainer_asroma.dirigeAllenamento()

steward_arsoma.descriviMembro()
steward_arsoma.supportaTeam()


while True:
    print("Menù:")
    print("1. Aggiungi Giocatore")
    print("2. Aggiungi Allenatore")
    print("3. Aggiungi Assistente")
    print("4. Mostra Squadra")
    print("5. Gioca Partita")
    print("0. Esci")

    scelta = input("Scelta: ")

    if scelta == "0":
        print("Uscita.")
        break
    elif scelta == "1":
        nome = input("Nome: ")
        cognome = input("Cognome: ")
        eta = int(input("Età: "))
        ruolo = input("Ruolo: ")
        numero = int(input("Numero maglia: "))
        g = Giocatore(nome, cognome, eta, ruolo, numero)
        squadra.aggiungiGiocatore(g)
    elif scelta == "2":
        nome = input("Nome: ")
        cognome = input("Cognome: ")
        eta = int(input("Età: "))
        anni = int(input("Anni esperienza: "))
        t = Allenatore(nome, eta, anni)
        squadra.aggiungiDirigenza(t)
    elif scelta == "3":
        nome = input("Nome: ")
        cognome = input("Cognome: ")
        eta = int(input("Età: "))
        spec = input("Specializzazione: ")
        s = Assistente(nome, cognome, eta, spec)
        squadra.aggiungiDirigenza(s)
    elif scelta == "4":
        player_asroma_1.giocaPartita()
    elif scelta == "5":
        break
    else:
        print("Scelta non valida.")
