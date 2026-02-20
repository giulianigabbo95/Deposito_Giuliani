'''
Trasformare il programma che abbiamo creato in precedenza per la gestione dei voti degli alunni in un programma per la gestione di una classe che utilizza un file come database:
    All'avvio il programma chiede se si vuole leggere l'elenco degli alunni e i loro voti e medie, se si vuole aggiungere un alunno o un voto.

# In collaborazione con Giovanni Iadelise, Elisabetta Carella e Mariagrazia Nuzzolese
'''

NOME_FILE = r"C:/Users/Gahab/Documents/GitHub/Corso_PyML_Deposito_Studente_Giuliani/Settimana_3/2026-02-18_Mer/voti.csv"


def scriviFile(nome_file, diz_studenti):
    stringa_totale = convertiDictToStr(diz_studenti)
    with open(nome_file, "w") as file:
        file.write(stringa_totale)


def leggFile(nome_file):
    with open(nome_file, "r") as file:
        contenuto = file.read()
    dizionario_totale = convertiStrToDict(contenuto)
    return dizionario_totale


def convertiDictToStr(dizionario):
    strg = ""                                   #Stringa
    for chiave, valore in dizionario.items():
        voti_stringa = "-".join(map(str, valore))
        strg += f"{chiave},{voti_stringa}\n"
    #print(strg.strip("\n"))
    return strg.strip("\n")


def convertiStrToDict(stringa):
    diz = {}
    lista_strg = stringa.split("\n")            #Stringa
    for riga in lista_strg:
        if riga.strip() == "":
            continue
        parti = riga.split(",")                     #Stringa
        chiave = parti[0]                           #Stringa
        valore = parti[1]                           #Stringa
        if valore == "":
            diz[chiave] = []
        else:
            elementi = valore.split("-")                #Lista di Stringhe Numeriche
            numeri = list(map(int, elementi))           #Lista di Interi
            diz[chiave] = numeri
    #print(diz)
    return diz


# MAIN
studenti = {}


try:
    studenti = leggFile(NOME_FILE)
except FileNotFoundError:
    studenti = {}

while True:
    print("-Menu-")
    print("Premi 1 - Aggiungi Alunno")
    print("Premi 2 - Aggiungi Voto")
    print("Premi 3 - Stampa Studenti e Medie")
    print("Premi 4 - Aggiorna")
    print("Premi 0 - Esci")
    scelta = input("Cosa vuoi fare? ")

    match scelta:
        case "1":
            #if type(studenti) == str:
            #    print(f"Studenti era una stringa: {type(studenti)}\n{studenti}")
            #    studenti_a = convertiStrToDict(studenti)
            #    studenti = studenti_a
            #    print(f"Studenti ora è un dizionario: {type(studenti)} - {studenti}")
            while True:
                nome = str(input("Inserisci studente: ")).lower()
                if nome not in studenti.keys():
                    print("Studente Inserito!")
                    break
                print("Studente già presente!")
            studenti[nome] = []
            scriviFile(NOME_FILE, studenti)
        case "2":
            #if type(studenti) == str:
            #    print(f"Studenti era una stringa: {type(studenti)} - {studenti}")
            #    studenti_b = convertiStrToDict(studenti)
            #    studenti = studenti_b
            #    print(f"Studenti ora è un dizionario: {type(studenti)} - {studenti}")
            nome = str(input("Inserisci studente: ")).lower()
            if nome in studenti.keys():
                voto = int(input("Inserisci il voto: "))
                studenti[nome].append(voto)
                scriviFile(NOME_FILE, studenti)
                print("Voto Inserito!")
            else:
                print("Studente non in elenco!")
        case "3":
            studenti = leggFile(NOME_FILE)
            if len(studenti) != 0:
                for nome in studenti.keys():       
                    if len(studenti[nome]) > 0:
                        media = sum(studenti[nome]) / len(studenti[nome])
                        print(f"Nome: {nome}, Media: {media}")
                    else:
                        print(f"Nome: {nome}, Nessun voto inserito")
            else:
                print("Nessuno studente trovato!")
            #if type(studenti) == dict:
            #    print(f"Studenti era un dizionario: {type(studenti)} - {studenti}")
            #    studenti_c = convertiDictToStr(studenti)
            #    studenti = studenti_c
            #    print(f"Studenti è una stringa {type(studenti)}-\n{studenti}")
        case "4":
            pass
        case "0":
            print("Ciao!")
            break
        case _:
            print("Input Errato")
    print("")