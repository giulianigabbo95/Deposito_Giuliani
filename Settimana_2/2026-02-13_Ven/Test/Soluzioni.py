'''
01. Inserisci Cognome nome ed email:
        Gabriele Giuliani giulianigabbo95@gmail.com

02. Quale di queste è una delle regole fondamentali dell'OOP a livello tecnico: (1 punto)
    Selezionare 3 opzioni.
        [X] - Astrazione
            - Proprietarietà
            - Modularità
        [X] - Polimorfismo
            - Ciclicità
        [X] - Incapsulamento
            - Riusabilità
        [X] - Ereditarietà

03. Cos'è Python? Quali sono le sue caratteristiche? Spiegale (1 punto)
    Python è un linguaggio di programmazione nato negli anni '90:
        - OOP: permette di definire classi e creare istanze supportando ereditarietà semplice e multipla, incapsulamento (tipo __ per attributi privati) e polimorfismo, ovvero quando uno stesso metodo si comporta diversamente in classi diverse.
        - Interpretato: permette che il codice venga eseguito riga per riga da un interprete senza una fase di compilazione separata, rendendo quindi più -certa l'esecuzione e più semplice il testing e il debugging a discapito però della velocità.
        - Fortemente dinamico: permette una dichiarazione implicita del tipo delle variabili, che può cambiare durante il codice, e, tramite questa forte e dinamica tipizzazione, operazioni tra tipi incompatibili senza conversione esplicita, previene errori sui tipi stessi.
        - Ad alto livello: permette asstrazione dall'hardware, non lasciando allo sviluppatore la gestione della memoria e dei puntatori, tramite un garbage collector automatico (simil-Java), e usando una sintassi leggibile e vicina al linguaggio umano, integrando tipi di dati complessi (come liste e dizionari).

04. Esamina il seguente codice Indica se l'incapsulamento è implementato correttamente e perché. (1 punto)
        class Account:
            def __init__(self, titolare, saldo_iniziale):
                self.titolare = titolare
                self.__saldo = saldo_iniziale  # Saldo è definito come privato

            def get_saldo(self):
                return self.__saldo

            def set_saldo(self, new_saldo):
                return self.__saldo = new_saldo

            def deposita(self, quantità):
                if quantità > 0:
                    self.__saldo += quantità
                    print(f"Depositati {quantità}€. Saldo : {self.__saldo}€.")
                else:
                    print("Inserisci una quantità valida.")

            def preleva(self, quantità):
                if 0 < quantità <= self.__saldo:
                    self.__saldo -= quantità
                    print(f"Prelevati {quantità}€. Saldo residuo: {self.__saldo}€.")
                else:
                    print("Quantità non valida o saldo insufficiente.")

            - Sì, l'incapsulamento è implementato correttamente perché __saldo è privato e accessibile solo tramite metodi definiti nella classe.
        [X] - No, l'incapsulamento non è implementato correttamente perché i metodi deposita e preleva non utilizzano i metodi getter e setter per accedere e modificare il saldo, bypassando le buone pratiche di incapsulamento.
            - Sì, l'incapsulamento è implementato correttamente perché permette la modifica diretta del saldo tramite i metodi deposita e preleva.

05. Cos'è una collezione? quali abbiamo studiato in Python?
    Spiega le differenze e fai un esempio di codice di istanziazione. (1 punto)
        Le collezioni sono strutture dati che permettono di memorizzare e organizzare più elementi insieme:
            - Liste: Sequenze ordinate, modificabili che possono contenere anche elementi duplicati, di qualsiasi tipo (nomi = ["Gabriele", "Mirko", "Francesco"] oppure numeri = [1, 2, 3, 4, 19, 5] oppure qualcosa = ["pippo", 42, False, 3.14]) 
            - Tuple: Sequenze ordinate, non modificabile che possono contenere duplicati (punto = (10, 20) oppure colori = ("rosso", "giallo", "aroma") oppure qualcosaltro = ("Pippo", 3.14, False))
            - Insiemi = Sequenze non ordinate, modificabili ma senza duplicati (numeri = {1, 2, 3, 4, 5} oppure cifrebelle = set([1, 2, 2, 3, 3, 3])
            - Dizionari: Sequenze di coppie chiave-valore, non ordinate (diz = {"Chiav": "Valor"})

06. Cos'è l'astrazione a livello teorico? (1 punto)
        [X] - Il processo di nascondere i dettagli complessi dietro un'interfaccia semplificata.
            - Il metodo per creare più copie di un oggetto senza esporre i suoi valori reali
            - La pratica di migliorare il rendimento del codice attraverso l'ottimizzazione.
            - Il nascondere i dettagli complessi dei metodi dietro un'interfaccia chiamata da abc.

07. Cos'è una classe, cos'è un oggetto, e cosa possono contenere?
    Cos'è un metodo specialee quali consoci? Descrivili (1 punto)
        Una classe è un modello per creare oggetti che definisce gli attributi e i metodi che gli oggetti di quel tipo avranno mentre un oggetto è un'istanza di una classe con attributi con dei valori specifici.
        I metodi speciali iniziano e finiscono con __ (doppio underscore) tipo __init__, e vengono chiamati automaticamente in determinate situazioni, tipo quando si crea un oggetto o si voglio stampare i suoi attributi (__init__(self), __str__(self)).

08. Esamina il seguente codice Indica se l'ereditarietà è implementata correttamente e perché. (1 punto)
        class Veicolo:
            def __init__(self, anno):
                self.anno = anno

            def mostra_anno(self):
                print(f"L'anno del veicolo è {self.anno}")

        class Automobile(Veicolo):
            def __init__(self, anno, marca):
                __init__(self, anno)  
                self.marca = marca

            def mostra_dettagli(self):
                print(f"Questa auto è del {self.anno} e della marca {self.marca}")
        
            - Sì, l'ereditarietà è implementata correttamente perché Automobile estende Veicolo e ha accesso ai suoi metodi e attributi.
            - Sì, l'ereditarietà è implementata correttamente perché la classe Automobile utilizza il costruttore della classe Veicolo per inizializzare l'attributo anno
        [X] - No, l'ereditarietà non è implementata correttamente perché la classe Automobile dovrebbe utilizzare super() invece di chiamare direttamente il costruttore della classe padre Veicolo.

09. Spiega le tre regole fondamentali dell'OOP, cosa fanno, e fai un ESEMPIO DI CODICE per ognuna. (1 punto)
        La regola fondamentale dell'OOP è l'astrazione, che si ottiene mediante:
            - Incapsulamento che pemette di nascondere i dettagli interni di un oggetto proteggendo i dati (
                    class ContoBancario:
                        def __init__(self, titolare, saldo_iniziale):
                            self.titolare = titolare
                            self.__saldo = saldo_iniziale       # Attributo privato
                        # Getter pubblico
                        def get_saldo(self):
                            return self.__saldo
                ).
            - Ereditarietà che permette di creare nuove classi basate su classi esistenti, usando i suoi attributi e metodi (
                    class Auto:
                        def __init__(self, marca, modello, anno):
                            self.__marca = marca
                            self.__modello = modello
                            self.__anno = anno

                    class FiatPunto(Auto):
                        def __init__(self, marca, modello, anno, numero_porte):
                            # Chiamata al costruttore del padre
                            super().__init__(marca, modello, anno)
                            self.__numero_porte = numero_porte  # Nuovo attributo
                ).
            - Polimorfismo che permette a oggetti di classi diverse di rispondere allo stesso metodo in modi diversi (
                    class Animale:
                        def __init__(self, nome):
                            self.nome = nome
                        def verso(self):
                            pass  # Metodo astratto (da implementare)

                    class Cane(Animale):
                        def verso(self):
                            return "Bau!"
                ).

10. Quale di queste capacità è di Git come tecnologia? (1 punto)
    Selezionare 3 opzioni.
            - Gestione del lavoro di gruppo
        [X] - Branching
            - Condivisone della repository
            - Riusabilità
            - Gestione dei partecipanti
        [X] - Merge
            - Coding assistito
        [X] - Commit
            - Gestione dei conflitti
            - Centralizzamento online condiviso

11. Cos'è il duck typing? (1 punto)
            - Una caratteristica prettamente dell'astrazione
        [X] - Una logica che usa il polimorfismo di Python
            - Un algoritmo di definizione matematica 
            - Un modulo interno a Python
            
    
12. Cos'è Git e cos'è GitHub? Cosa puoi fare con github? (azioni e concetti) (1 punto)
        - Git è una tecnologia, programma, sistema di controllo versione aka versionamento che tiene traccia cronologica dei record di modifiche nel tempo di alcuni file scelti dall'utente/sviluppatore, permettendo quindi anche di toranre indietro nel tempo e di far lavorare più persone in parallelo, anche su progetti diversi derivati dallo stesso (tipo LibreOffice, OpenOffice, OnlyOffice che derivano da una radice unica Microsoft Office), e quindi di scaricare codice altrui sulla propria macchina.
            Funziona in locale ma permette di inserire i cambiamenti su repository online come GitHub
            Permette di fare Commit per creare un nuovo record dei cambiamenti, Branching per creare fork di software, Merge per unire i cambiameti di vari branch e quindi gestire i conflitti di file diversi con stesso path e nome.
        - GitHub è un prodotto lato client che ospita repository Git sul web e si usa col browser, permette di salvare e condividere il codice (come un drive per qualsiasi file), ma soprattutto ad altri di modificarlo.*
            Senza Git non esisterebbe ma non è vero il contrario.
            Versioni alternative a GitHub: GitLab, BitBucket
        - Bonus: GitHub Desktop è un software lato client che tramite GUI permette di usare le operazioni di Git connettendosi alle repository remote online,
            Versioni alternative a GitHub Desktop: GitLab, GitKraken, BitBucket

13. Cosa differenzia un metodo variadico e uno polimorfico? (1 punto)
        - Il numero di parametri accettati e il numero di richiami possibili
        - Il variadico lavora sui tipi, il polimorfico sui parametri
        - Il variadico lavora sui parametri, il polimorfico sui tipi
        - Niente solo il numero di return

14. Cos'è l'astrazione? Spiegala sia pratica che teorica (1 punto)
        L'astrazione per i linguaggi OOP è un principio che aiuta a separare le specifiche di alto livello dalle implementazioni di basso livello.
        In pratica è il processo di nascondere i dettagli complessi dietro un'interfaccia semplificata.
        L'astrazione viene realizzata attraverso classi astratte, che non può essere istanziata da sola, ma che serve come modello per altre classi. e metodi astratti, che sono implementati nelle classi derivate che ereditano dalla classe astratta.
        Si può implementare in Python con la libreria ABC e l'uso del decoratore @abstractmethod, che impongono rispettivamente un'interfaccia comune (diversa da quella che si intende in Java) tra classi diverse, e l'implementazione di determinati metodi.

            from abc import ABC, abstractmethod

            class Persona(ABC):
                @abstractmethod
                def stampaNome(self):
                    pass
                @abstractmethod
                def stampaTitoloStudio(self):
                    pass

            class Studente(Persona):
                def __init__(self, nome, cognome, istruzione):
                    self.nome = nome
                    self.cognome = cognome
                    self.__istruzione = istruzione
                def stampaNome(self):
                    print(f"Sono {self.nome} {self.cognome}")
                def stampaTitoloStudio(self):
                    print(f"Ho un/una {self.__istruzione}")

            s = Studente("Giuliani", "Giuliani", "Laurea Magistrale in CyberSecurity")
            s.stampaNome()
            s.stampaTitoloStudio()
            
15. Com'è andata?
        8/10

16. EXTRA: fai un meme sul corso (vale mille mila punti)
        BASE: Drake Hotline Bling
        Not all HUBs are built to stand the test of time.

17. Esercizio:
    Realizzare, all'interno di una cartella specifica della repository (ad esempio: /progetti/OOP_GestionaleIngressoLavoro), un piccolo sistema software per la gestione dell'ingresso in azienda, utilizzando la programmazione orientata agli oggetti (OOP).

    Il sistema dovrà simulare la gestione di:
        - persone (dipendenti, visitatori, ecc.)
        - ruoli
        - badge
        - turni di lavoro
        - controlli di accesso
        - log delle entrate e uscite

    Progettare e implementare un software che gestisca la logica di accesso a un'azienda, dimostrando in modo chiaro e strutturato l'applicazione delle quattro regole fondamentali della programmazione orientata agli oggetti:
        - Astrazione
        - Ereditarietà
        - Incapsulamento
        - Polimorfismo
        
    Il progetto dovrà:
        - Essere organizzato nella cartella indicata all'interno della repository.
        - Contenere più file e/o moduli coerenti con l'idea di “gestionale per l'ingresso a lavoro”.
        - Mostrare chiaramente, nel codice e nella struttura del progetto, dove e come vengono applicate le quattro regole OOP.
    
    Non sono fornite ulteriori specifiche obbligatorie ma lo studente dovrà:
        - Definire autonomamente quali oggetti esistono nel sistema.
        - Stabilire come interagiscono tra loro.
        - Decidere le responsabilità di ciascuna classe.
        - Dimostrare in modo evidente l'uso di:
            . Astrazione
            . Ereditarietà
            . Incapsulamento
            . Polimorfismo
'''
from datetime import time

from badge import Badge
from turno import Turno
from persona import Persona, Dipendente, Visitatore
from accessi import ControlloAccessi, LogAccesso

controllo = ControlloAccessi()
turni = [
    Turno(time(6,0), time(14,0)), 
    Turno(time(14,0), time(22,0))
] #Turno(time(22,0), (6,0)) fa casino perchè va al giorno appresso e non so come dirglielo
badge_1 = Badge("B001")
badge_2 = Badge("B002")
badge_3 = Badge("B003")
dipendenti = [
    Dipendente("Mario", "Rossi", "D001", turni[0], badge_1),
    Dipendente("Luigi", "Verdi", "D002", turni[1], badge_2)
]
visitatori = [
    Visitatore("Paolo", "Ferrari", "V001", False), 
    Visitatore("Anna", "Esposito", "V002", True)
]

while True:
    print("")
    print("Menù")
    print("1. Elenca Persone")
    print("2. Verifica Accesso")
    print("3. Aggiungi Persona")
    print("4. Log Accessi")
    print("5. Esci")
    print("")
    
    scelta = input("Scegli: ")
    
    match scelta:
        case "1":
            print("Dipendenti:")
            for d in dipendenti:
                print(" ", d)
            print("Visitors:")
            for v in visitatori:
                print(" ", v)
    
        case "2":
            print("1. Dipendente")
            print("2. Visitatore")
            
            tipo = input("Tipo: ")
            
            if tipo == "1":
                for i, d in enumerate(dipendenti):
                    print(f"{i+1} - {d.stampaGeneralita()}")
                idx = int(input("Numero: ")) - 1
                controllo.verificaAccesso(dipendenti[idx])
            else:
                for i, v in enumerate(visitatori):
                    print(f"{i+1} - {v.stampaGeneralita()}")
                idx = int(input("Numero: ")) - 1
                controllo.verificaAccesso(visitatori[idx])
        
        case "3":
            print("1. Dipendente")
            print("2. Visitatore")
            
            tipo = input("Tipo: ")
            nome = input("Nome: ")
            cognome = input("Cognome: ")
            id_persona = input("ID: ")
            
            if tipo == "1":
                nuovo_badge = Badge(f"B{len(dipendenti)+4:03d}") #Grazie Google
                dipendenti.append(Dipendente(nome, cognome, id_persona, turni[0], nuovo_badge))
            else:
                visitatori.append(Visitatore(nome, cognome, id_persona))
            print("Aggiunto!")
    
        case "4":
            controllo.mostraLog()
    
        case "5":
            print("Ciao!")
            break


