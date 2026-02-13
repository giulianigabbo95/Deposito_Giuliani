'''
Esercizio:
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
] #Turno(time(22,0), (6,0)) fa casino perchè va al giorno appresso
badge_1 = Badge("B001")
badge_2 = Badge("B002")
badge_3 = Badge("B003")
dipendenti = [
    Dipendente("Mario", "Rossi", "D001", turni[0], badge_1),
    Dipendente("Luigi", "Verdi", "D002", turni[1], badge_2)
]
visitatori = [
    Visitatore("Paolo", "Ferrari", "V001"), 
    Visitatore("Anna", "Esposito", "V002", True)
]

while True:
    print("1. Elenca persone")
    print("2. Verifica accesso")
    print("3. Aggiungi persona")
    print("4. Log accessi")
    print("5. Esci")
    
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