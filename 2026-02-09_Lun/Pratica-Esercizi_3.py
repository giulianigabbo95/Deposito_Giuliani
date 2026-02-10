'''
Esercizio: Sistema di Gestione Negozio
Realizza un programma che simuli la gestione di un negozio.
Il sistema deve gestire:
    - Clienti
    - Inventario
    - Amministratori
1. Gestione Clienti
    I clienti possono registrarsi e fare login.
    Dopo il login, i clienti possono:
        - visualizzare gli articoli disponibili
        - acquistare articoli
    Il sistema deve tenere traccia degli acquisti dei clienti.
2. Gestione Inventario
    Ogni articolo è descritto da:
        - nome
        - prezzo
        - quantità disponibile
    È possibile:
        - aggiungere nuovi articoli
        - modificare prezzo o quantità
        - rimuovere articoli
3. Amministrazione
    Gli amministratori sono pre-inseriti nel sistema.
    Gli amministratori possono:
        - visualizzare l'inventario
        - modificare l'inventario
        - visualizzare i guadagni totali del negozio
    Il programma deve simulare un'interazione tramite menu testuali, distinguendo l'accesso cliente e amministratore.

'''
print("")
print("START")
print("CON ERRORI E DA FINIRE")

#-CLASSI-#
class Cliente:
    def __init__(self, nome, password):
        self.nome = nome
        self.password = password
        self.acquisti = []
        
    def aggiungiAcquisto(self, articolo, quantita):
        self.acquisti.append((articolo, quantita))

class Amministratore:
    def __init__(self, nome, password):
        self.nome = nome
        self.password = password 

class Negozio:
    def __init__(self, nome):
        self.nome = nome
        self.inventario = Inventario()
        self.clienti = [Cliente("Giuseppe", "qwerty")]
        self.amministratori = [Amministratore("admin", "12345")]
        self.guadagni = 0

    def registraCliente(self, nome):
        self.clienti.append(Cliente(nome))
        print("Cliente registrato.")
        
    def trovaCliente(self, nome):
        i = 0
        while i < len(self.clienti):
            if self.clienti[i].nome == nome:
                return self.clienti[i]
            i += 1
        return None
    
    def acquistaArticolo(self, cliente, articolo, quantita):
        i = 0
        while i < len(self.inventario.articoli):
            a = self.inventario.articoli[i]
            if a[0] == articolo and a[2] >= quantita:
                self.inventario.articoli[i] = (a[0], a[1], a[2] - quantita)
                costo = a[1] * quantita
                self.guadagni += costo
                cliente.aggiungiAcquisto(articolo, quantita)
                print("Acquisto completato. Spesa:", costo, "€")
                return
            i += 1
        print("Articolo non disponibile.")

class Inventario:
    def __init__(self):
        self.articoli = [
            ("Pane", 2, 50),
            ("Latte", 1.5, 30),
            ("Pasta", 1, 40)
        ]
    
    def mostraArticoli(self):
        print("Inventario:")
        i = 0
        while i < len(self.articoli):
            a = self.articoli[i]
            print("- " + a[0] + " | Prezzo: " + str(a[1]) + "€ | Quantità: " + str(a[2]))
            i += 1
            
    def aggiornaArticolo(self, nome, prezzo, quantita):
        i = 0
        while i < len(self.articoli):
            if self.articoli[i][0] == nome:
                self.articoli[i] = (nome, prezzo, quantita)
                print("Articolo aggiornato.")
                return
            i += 1
        self.articoli.append((nome, prezzo, quantita))
        print("Nuovo articolo aggiunto.")

     
####-MAIN-####
#Variabili

negozio1 = Negozio("Lidl di Afragola")
cliente1 = Cliente("Franco", "parolasegreta")

while True:
    print("Login:")
    print("1. Admin")
    print("2. Users")
    print("0. Esci")

    scelta = input("Seleziona tipo di accesso: ")

    match scelta:
        case "0":
            print("Ciao.")
            break
        case "1":
            pass
        case "2":
            while True:
                print("Menù Cliente")
                print("1. Visualizza articoli")
                print("2. Acquista articolo")
                print("3. Visualizza acquisti")
                print("0. Logout")
                
                selezione = input("Seleziona tipo di accesso: ")

                match selezione:
                    case "0":
                        print("Arrivederci.")
                        break
                    case "1":
                        negozio1.inventario.mostraArticoli()
                    case "2":
                        nome = input("Nome articolo: ")
                        quantita = int(input("Quantità: "))
                        negozio1.acquista(cliente1, nome, quantita)
                    case 3:
                        print("\nAcquisti effettuati:")
                        i = 0
                        while i < len(cliente1.acquisti):
                            a = cliente1.acquisti[i]
                            print("- " + a[0] + " x " + str(a[1]))
                            i += 1
                    case _:
                        print("Scelta non valida, riprova.")
                        continue



print("STOP")
print("")
