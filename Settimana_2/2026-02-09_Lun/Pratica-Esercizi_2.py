'''
Obiettivo: Creare una classe Ristorante che permetta di gestire alcune funzionalità di base .
Requisiti:
1. Definizione della Classe:
    - Creare una classe chiamata Ristorante con un costruttore __init__ che accetta i parametri:
        . nome (nome del ristorante)
        . tipo_cucina (tipo di cucina offerta)
    - Definire un attributo "aperto" che indica se il ristorante è aperto o chiuso impostato su False di default (cioè, il ristorante è chiuso).
    - Un "Lista o +" menu dove dentro ci sono i piatti e prezzi che ha il ristorante
2. Metodi della Classe:
    - descrivi_ristorante(): Un metodo che stampa una frase descrivendo il ristorante, includendo il nome e il tipo di cucina.
    - stato_apertura(): Un metodo che stampa se il ristorante è aperto o chiuso.
    - apri_ristorante(): Un metodo che imposta l'attributo aperto su True e stampa un messaggio che indica che il ristorante è ora aperto.
    - chiudi_ristorante(): Un metodo che imposta l'attributo aperto su False e stampa un messaggio che indica che il ristorante è ora chiuso.
    - aggiungi_al_menu(): Un metodo per aggiungere piatti al menu
    - togli_dal_menu(): Un metodo per togliere piatti al menu
    - stampa_menu(): Un metodo per stampare il menu
3. Testare la Classe:
    - Creare un'istanza della classe Ristorante, passando i valori appropriati al costruttore.
    - Testare tutti i metodi creati per assicurarsi che funzionino come previsto.
'''
print("")
print("START")

#-CLASSI-#
class Ristorante:
    aperto = False
    menu = [("Carbonara", 10), ("Amatriciana", 15), ("Gricia", 20)]
    
    def __init__(self, nome, tipo_cucina):
        self.nome = nome
        self.tipo_cucina = tipo_cucina

    def descriviRistorante(self):
        print(f"Il ristorante '{self.nome}' offre cucina {self.tipo_cucina}.")
        
    def eApertoRistorante(self):
        if self.aperto == True:
            print("Il ristorante è aperto.")
        else:
            print("Il ristorante è chiuso.")
            
    def apriRistorante(self):
        self.aperto = True
        print("Il ristorante è ora aperto.")
        
    def chiudiRistorante(self):
        self.aperto = False
        print("Il ristorante è ora chiuso.")
        
    def aggiungiNelMenu(self, piatto, prezzo):
        presente = True
        for t in self.menu:
            if t[0] == piatto:
                print(f"Il piatto '{piatto}' è già presente nel menu.")
                presente = False
                break
        if presente == True:
            self.menu.append((piatto, prezzo))
            print(f"Piatto '{piatto}' aggiunto al menu a {prezzo}€.")

    def togliDalMenu(self, piatto):
        presente = False
        for t in self.menu:
            if t[0] == piatto:
                self.menu.remove(t)
                print(f"Piatto '{piatto}' rimosso dal menu.")
                presente ==  True
                break
        if presente == False:
            print(f"Il piatto '{piatto}' non è presente nel menu.")

    def stampaMenu(self):
        if len(self.menu) == 0:
            print("Il menu è vuoto.")
        else:
            print("Menu del ristorante:")
            for piatto, prezzo in self.menu.items():
                print(f"- {piatto}: {prezzo}€")
                
####-MAIN-####
#Variabili
lista_ristoranti = []
ristorante1 = Ristorante("La Bella Italia", "italiana")
ristorante2 = Ristorante("Ch' Pizz!", "napoletana")
ristorante3 = Ristorante("Meat Sharks!", "norvegese")

ristorante1.descriviRistorante()
ristorante1.eApertoRistorante()

ristorante1.aggiungiNelMenu("Carbonara", 45)
ristorante2.aggiungiNelMenu("Margherita", 5)

ristorante1.stampaMenu()
ristorante2.stampaMenu()

ristorante1.togliDalMenu("Amatriciana")
ristorante2.togliDalMenu("Margherita")

ristorante1.stampaMenu()
ristorante2.stampaMenu()

ristorante1.chiudiRistorante()
ristorante2.chiudiRistorante()

lista_ristoranti.append(ristorante1)
lista_ristoranti.append(ristorante2)
lista_ristoranti.append(ristorante3)


while True:
    print("Seleziona un ristorante:")
    i = 0
    while i < len(lista_ristoranti):
        print(str(i+1) + ". " + lista_ristoranti[i].nome + " (" + lista_ristoranti[i].tipo_cucina + ")")
        i += 1
    print("0. Esci")

    scelta = input("Seleziona un ristorante: ")

    if scelta == "0":
        print("Torna a trovarci e lascia una recensione su TripAdvisor.")
        break

    if not scelta.isdigit() or int(scelta) < 1 or int(scelta) > len(lista_ristoranti):
        print("Scelta non valida, riprova.")
        continue

    ristoranteX = lista_ristoranti[int(scelta)-1]

    while True:
        print(f"{ristoranteX.nome}")
        print("1. Descrivi ristorante")
        print("2. Stato apertura")
        print("3. Apri ristorante")
        print("4. Chiudi ristorante")
        print("5. Aggiungi piatto al menu")
        print("6. Togli piatto dal menu")
        print("7. Stampa menu")
        print("0. Esci")
        
        opzione = input("Seleziona un'opzione: ")

        match opzione:
            case "1":
                ristoranteX.descriviRistorante()
            case "2":
                ristoranteX.statoApertura()
            case "3":
                ristoranteX.apriRistorante()
            case "4":
                ristoranteX.chiudiRistorante()
            case "5":
                piatto = input("Nome piatto: ")
                prezzo = int(input("Prezzo: "))
                ristoranteX.aggiungiNelMenu(piatto, prezzo)
            case "6":
                piatto = input("Nome piatto da togliere: ")
                ristoranteX.togliDalMenu(piatto)
            case "7":
                ristoranteX.stampaMenu()
            case "0":
                break
            case _:
                print("Opzione non valida, riprova.")

print("STOP")
print("")