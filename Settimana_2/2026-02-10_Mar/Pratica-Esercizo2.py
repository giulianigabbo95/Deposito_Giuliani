'''
Realizzare un programma per la gestione di una fabbrica che produce e vende diversi tipi di prodotti.
Il sistema deve permettere di gestire i prodotti, l'inventario e le vendite.

Il sistema deve essere composto da più classi:
a. Classe Prodotto
    Ogni prodotto deve avere:
        - nome, una stringa che descrive il nome del prodotto
        - costo_produzione, un numero che rappresenta il costo per produrre il prodotto
        - prezzo_vendita, un numero che rappresenta il prezzo di vendita al pubblico
b. Classi parallele a Prodotto
    Creare almeno due classi parallele alla classe `Prodotto`, ad esempio:
        - Elettronica
        - Abbigliamento
    Ogni classe deve:
        - ereditare dalla classe Prodotto
        - avere almeno un attributo specifico:
        - garanzia per i prodotti di tipo Elettronica
        - materiale per i prodotti di tipo Abbigliamento
    La classe deve fornire:
        - un metodo calcola_profitto che restituisce la differenza tra prezzo di vendita e costo di produzione
c. Classe Fabbrica
    La fabbrica deve gestire l'inventario e le vendite dei prodotti.
    La classe deve avere:
        - inventario, un dizionario che tiene traccia della quantità disponibile di ogni prodotto
    La classe deve fornire:
        - un metodo aggiungi_prodotto per aggiungere prodotti all'inventario
        - un metodo vendi_prodotto che diminuisce la quantità di un prodotto in inventario e stampa il profitto realizzato
        - un metodo resi_prodotto che aumenta la quantità di un prodotto restituito in inventario
    
Nel programma principale:
    - creare almeno due prodotti di tipo diverso
    - aggiungerli all'inventario della fabbrica
    - simulare alcune vendite
    - simulare almeno un reso
    - stampare i profitti delle vendite effettuate
'''

#CLASSI
class Prodotto:
    def __init__(self, nome, costo_produzione, prezzo_vendita):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita

    def calcolaProfitto(self):
        margine = self.prezzo_vendita - self.costo_produzione
        return margine
    
class Elettronica(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita, garanzia):
        super().__init__(nome, costo_produzione, prezzo_vendita)
        self.garanzia = garanzia

class Abbigliamento(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita, materiale):
        super().__init__(nome, costo_produzione, prezzo_vendita)
        self.materiale = materiale

class Fabbrica:
    def __init__(self):
        self.inventario = {}
    
    def aggiungiProdotto(self, prodotto, quantita):
        if prodotto.nome in self.inventario:
            self.inventario[prodotto.nome]["quantita"] += quantita
        else:
            self.inventario[prodotto.nome] = {
                "prodotto": prodotto,
                "quantita": quantita
            }

    def vendiProdotto(self, nome_prodotto, quantita):
        if nome_prodotto in self.inventario:
            if self.inventario[nome_prodotto]["quantita"] >= quantita:
                self.inventario[nome_prodotto]["quantita"] -= quantita
                profitto = self.inventario[nome_prodotto]["prodotto"].calcolaProfitto() * quantita
                print("Vendita effettuata. Profitto:", profitto)
            else:
                print("Quantità non disponibile.")
        else:
            print("Prodotto non presente.")

    def rendiProdotto(self, nome_prodotto, quantita):
        if nome_prodotto in self.inventario:
            self.inventario[nome_prodotto]["quantita"] += quantita
            print("Reso registrato.")
            
    def mostraInventario(self):
        print("Inventario:")
        for nome in self.inventario:
            quantita = self.inventario[nome]["quantita"]
            print("-", nome, "| Quantità:", quantita)

            

###-MAIN-###
fabbrica1 = Fabbrica()

telefono1 = Elettronica("Telefono", 200, 350, "2 anni")
maglietta1 = Abbigliamento("Maglietta", 10, 25, "Cotone")

fabbrica1.aggiungiProdotto(telefono1, 10)
fabbrica1.aggiungiProdotto(maglietta1, 20)

fabbrica1.vendiProdotto("Telefono", 2)
fabbrica1.vendiProdotto("Maglietta", 5)

fabbrica1.rendiProdotto("Maglietta", 1)

while True:
    print("Menu:")
    print("1. Aggiungi prodotto")
    print("2. Vendi prodotto")
    print("3. Registra reso")
    print("4. Mostra inventario")
    print("0. Esci")

    scelta = input("Scelta: ")

    if scelta == "0":
        print("Passo e Chiudo!")
        break

    if scelta.isdigit() == False or int(scelta) < 1 or int(scelta) > 4:
        print("Scelta non valida.")
        continue

    match scelta:
        case "1":
            print("Tipo:")
            print("1. Elettronica")
            print("2. Abbigliamento")
            selezione = input("Selezione: ")

            nome = input("Nome prodotto: ")
            costo = float(input("Costo produzione: "))
            prezzo = float(input("Prezzo vendita: "))
            quantita = int(input("Quantità: "))

            if selezione == "1":
                garanzia = input("Garanzia: ")
                prodotto = Elettronica(nome, costo, prezzo, garanzia)
            elif selezione == "2":
                materiale = input("Materiale: ")
                prodotto = Abbigliamento(nome, costo, prezzo, materiale)
            else:
                print("Tipo non valido.")
                continue

            fabbrica1.aggiungiProdotto(prodotto, quantita)
            print("Prodotto aggiunto.")
        
        case "2":
            nome = input("Nome prodotto da vendere: ")
            quantita = int(input("Quantità da vendere: "))
            fabbrica1.vendiProdotto(nome, quantita)
            
        case "3":
            nome = input("Nome prodotto restituito: ")
            quantita = int(input("Quantità restituita: "))
            fabbrica1.rendiProdotto(nome, quantita)

        case "4":
            fabbrica1.mostraInventario()
            
        case _:
            print("Tasto attualmente non disponibile.")