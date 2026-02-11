
'''
Sintassi e Operazioni Basilari
'''
print("")
print("START")
print("Questa è la 1° lezione")

#Commento Singola Linea
'''
Commento Multi Linea
'''

#Variabili
nome_1 = "Alice"
nome_2 = "Paolo"
nome_3 = input("Come ti chiami? ")

eta_1 = 15
eta_2 = 20
eta_3 = input("Quanti anni hai? ")

genere_1 = "m"
genere_2 = "f"
genere_3 = input("Sei maschio (m) o femmina (f)? ")



#Stampa Data Inseriti
print("Il mio nome è:", nome_1, "sono", genere_1, "e ho", eta_1, "anni!")
print("Il mio nome è:", nome_2, "sono", genere_2, "e ho", eta_2, "anni!")
print("Il mio nome è:", nome_3, "sono", genere_3, "e ho", eta_3, "anni!")

#Concatenazione Stringhe
print("Cosa succede se sommo due nomi come Alice e Paolo? con 'nome_1+nome_2':", nome_1 + nome_2)

#Operazioni Base
print("Se scrivo 1+2, succede:", 1+2)
print("Se scrivo 2**3, succede:", 2**3)
print("Se scrivo una divisione tra interi come eta_1/eta_2, succede:", eta_1 / eta_2, "...")
print("...quindi se inserisco questo numero in una variabile diventa un float!")

#Funzioni e Metodi
print("Il mio nome è lungo:", len(nome_3), "secondo len()")
print("La terza lettera del mio nome è:", nome_3[2], "stampata con nome_3[2]")
print("Il mio nome è:", nome_3[2], "stampata con s[2]")
print("Il mio nome in maiuscolo :", nome_3.upper(), "secondo nome_3.upper")

#Booleani
BooleanT = True
BooleanF = False
print("Il mio booleano BooleanF era settato a falso, confermo stampandolo:", BooleanF)
print("Il mio booleano BooleanF castato a intero è 0, confermo stampandolo:", int(BooleanF))

print("STOP")
print("")
