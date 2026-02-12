'''
Creare un sistema a oggetti per gestire la prenotazione dei posti di un teatro, utilizzando ereditarietà e polimorfismo.

a. Classe base Posto
    Attributi privati:
        - _numero (intero): numero del posto
        - _fila (stringa): fila in cui si trova il posto
        - _occupato (booleano): True se occupato, False se libero
    Metodi:
        - __init__(self, numero, fila): inizializza numero e fila, imposta _occupato = False
        - prenota(self): prenota il posto se libero, altrimenti stampa un messaggio di errore
        - libera(self): libera il posto se occupato, altrimenti stampa un messaggio di errore
    Getter: metodi per recuperare numero, fila e stato di occupazione

b. Classi derivate:
    - PostoStandard (eredita da Posto)
        Attributi aggiuntivi: _costo: prezzo del posto (es.: per prenotazione online)
        Metodi: prenota(self): sovrascrive il metodo base per visualizzare il costo della prenotazione
    - PostoVIP (eredita da Posto)
        Attributi aggiuntivi: _serviziExtra: lista di servizi (es. ["Accesso lounge", "Servizio al posto", "Omaggio"])
        Metodi: prenota(self): sovrascrive il metodo base per attivare anche i servizi extra
    
c. Classe Teatro
    Attributi: _posti: lista contenente tutti i posti (sia VIP che Standard)
    Metodi:
        - aggiungiPosto(self, posto): aggiunge un nuovo posto alla lista
        - prenotaPosto(self, numero, fila): cerca il posto con numero e fila corrispondenti e chiama il suo metodo prenota()
        - stampaPostiOccupati(self): visualizza tutti i posti attualmente occupati
'''

class PostoBase:
    def __init__(self, numero, fila):
        self._numero = numero
        self._fila = fila
        self._occupato = False
        self.costo_base = 15
    
    def eOccupato(self):
        return self._occupato
    
    def prenotaPosto(self):
        if self._occupato == False:
            self._occupato = True
            print(f"Il posto {self._fila}{self._numero} è stato prenotato! Ti è andata bene!")
        else:
            print(f"Il posto {self._fila}{self._numero} è già occupato! Che sfiga!")
    
    def liberaPosto(self):
        if self._occupato == True:
            self._occupato = False
            print(f"Il posto {self._fila}{self._numero} si è liberato! Che culo!")
        else:
            print(f"Il posto {self._fila}{self._numero} non era occupato scemo!")
    
    def get_numero(self):
        return self._numero
    
    def get_fila(self):
        return self._fila
    
    def get_costo_base(self):
        return self.costo_base
    
class PostoStandard(PostoBase):
    def __init__(self, numero, fila):
        super().__init__(numero, fila)
    
    def prenotaPosto(self):
        if self._occupato == False:
            self._occupato = True
            print(f"Il posto da poveri {self._fila}{self._numero} è stato prenotato!")
            print(f"Sborsa {self._costo}€")
            print(f"Pagah! Devi pagare lezzo!")
        else:
            print(f"il posto da poveri {self._fila}{self._numero} è già occupato da uno più povero di te! Vabbeh dai, non sei il più barbone, una magra consolazione!")

class PostoVIP(PostoBase):
    def __init__(self, numero, fila, servizi_extra, costo_servizi_extra):
        super().__init__(numero, fila)
        self._servizi_extra = servizi_extra
        self._costo += costo_servizi_extra
    
    def prenotaPosto(self):
        if self._occupato == False:
            self._occupato = True
            print(f"Il posto da sceicco {self._fila}{self._numero} è prenotato! Li sordi tua!")
            print(f"Puoi anche: {', '.join(self._servizi_extra)}")
        else:
            print(f"Il posto VIP {self._fila}{self._numero} già occupato da uno più ricco di te, pezzente!")
            
    def get_costo(self):
        return self._costo
            
class Teatro:
    def __init__(self):
        self._posti = []
        
    def aggiungiPosto(self, posto):
        self._posti.append(posto)
        print(f"Posto {posto.getFila()}{posto.getNumero()} aggiunto!")
        
    def cercaPosto(self, numero, fila):
        for posto in self._posti:
            if posto.getNumero() == numero and posto.getFila() == fila:
                return posto
        return None
    
    def liberaPosto(self, numero, fila):
        posto = self.cercaPosto(numero, fila)
        if posto:
            posto.liberaPosto()
        else:
            print(f"Wewe, il posto {fila}{numero} non esiste!")
        
    def stampaTuttiPosti(self):
        if self._posti :
            print("Nessun posto nel teatro.")
            return
        
    def stampaPostiOccupati(self):
        pass     
        
    def stampaPostiLiberi(self):
        pass
        
        
        
teatro = Teatro()

while True:
    print("Teatro Varti Occupazione")
    print("1. Aggiungi Posto")
    print("2. Prenota Posto")
    print("3. Libera Posto")
    print("4. Mostra Posti Occupati")
    print("5. Mostra Posti Liberi")
    print("6. Mostra Tutti i Posti")
    print("7. Esci")
    
    scelta = input("Scegli: ")
    
    match scelta:
        case "1":
            print("Aggiungi Posto")
            print("1. Posto Poveri")
            print("2. Posto Ricchi")
            tipo = input("Scegli tipo: ")
            
            fila = input("Fila: ").upper()
            numero = int(input("Numero: "))
            
            match tipo:
                case "1":
                    costo = float(input("Costo: €"))
                    teatro.aggiungiPosto(PostoStandard(numero, fila, costo))
                case "2":
                    servizi = input("Servizi extra (separati da virgola): ").split(",")
                    servizi = [s.strip() for s in servizi]
                    teatro.aggiungiPosto(PostoVIP(numero, fila, servizi))
                case _:
                    print("Tipo non valido!")
        
        case "2":
            print("Prenota")
            fila = input("Fila: ").upper()
            numero = int(input("Numero: "))
            teatro.prenotaPosto(numero, fila)
        
        case "3":
            print("Libera")
            fila = input("Fila: ").upper()
            numero = int(input("Numero: "))
            teatro.liberaPosto(numero, fila)
        
        case "4":
            teatro.stampaPostiOccupati()
        
        case "5":
            teatro.stampaTuttiPosti()
        
        case "6":
            teatro.stampaPostiLiberi()
        
        case "7":
            print("Non farti più rivedere!")
            break
        
        case _:
            print("Era difficile sbagliare eh!")
            
    print("")