'''
Esercizio 1 (Facile):
Crea una classe chiamata Punto.
Questa classe dovrebbe avere:
- Due attributi: x e y, per rappresentare le coordinate del punto nel piano.
- Un metodo "cambiaCoordinate" che prenda in input un valore per dx e un valore per dy e modifichi le coordinate del punto di questi valori.
- Un metodo "calcolaDistanzaOrigine" che restituisca la distanza del punto dall'origine (0,0) del piano.
EXTRA: Crea N oggetti di tipo Punto e stampali tutti insieme
'''
print("")
print("START")

import math

#-FUNZIONI-#

#-CLASSI-#
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def cambiaCoordinate(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y
        
    def calcolaDistanzaOrigine(self):
        return math.sqrt(self.x**2 + self**2)
    
    def __str__(self):
        return f"Punto({self.x}, {self.y})"

####-MAIN-####
#Variabili
punto_a = Punto(3, 4)

while True:
    print("Le coordinare del punto ", punto_a," sono:", punto_a.x, punto_a.y)
    print("La distanza dall'orgine (0, 0) è:", punto_a.calcolaDistanzaOrigine())
    
    selezione = input("Vuoi modificarle? [S] o [N]: ").upper()
    
    if selezione == 'N':
        print("Ciao!")
        break
    elif selezione == 'S':
        nuova_x = int(input("Inserisci quanto vuoi aggiungere sull'asse delle ascisse:"))
        nuova_y = int(input("Inserisci quanto vuoi aggiungere sull'asse delle ordinate:"))
        punto_a.cambiaCoordinate(nuova_x, nuova_y)
        #print("La distanza dall'orgine (0, 0) ora è:", p.calcolaDistanzaOrigine())
    else:
        print("Input errato. Riproviamo")
    
    print("")
    
#EXTRA
punti = [Punto(1, 3), Punto (2, 4), Punto(4, 5)]

for punto in punti:
    punto.cambiaCoordinate(-1, -1)
    print(punto, "- distanza dall'origine:", punto.calcolaDistanzaOrigine())


print("")
#####################################################################################################################################################################################
print("------------------------")
print("")
'''
Esercizio 2 (Facile):
Crea una classe chiamata Libro.
Questa classe dovrebbe avere:
- Tre attributi: titolo, autore e pagine.
- Un metodo "stampaInfo" che restituisca una stringa del tipo "Il libro 'titolo' è stato scritto da 'autore' e ha 'pagine' pagine.".
'''

#-FUNZIONI-#

#-CLASSI-#
class Libro:
    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine

    def stampaInfo(self):
        return f"Il libro '{self.titolo}' è stato scritto da '{self.autore}' e ha '{self.pagine}' pagine."

####-MAIN-####
#Variabili
l = Libro("Dieci Piccoli Indiani", "A. Christie", 100)

while True:
    print("L del punto sono:", l)
    
    selezione = input("Vuoi leggere che libri ci sono? [S] o [N]: ")
    
    if selezione == 'N':
        print("Ciao!")
        break
    elif selezione == 'S':
        l.stampaInfo()
    else:
        print("Input errato. Riproviamo")
    
    print("")

print("")
#####################################################################################################################################################################################
print("------------------------")
print("")
'''
Esercizio 3: 
Crea una classe biblioteca che permetta di creare un libro e stamparlo
Extra: permetti di creare quanti libri vuole l'utente
'''

#-FUNZIONI-#

#-CLASSI-#
class Libro:
    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine

    def __str__(self):
        return f"'{self.titolo}' di {self.autore} ({self.pagine} pagine)"
    
class Biblioteca:
    def __init__(self):
        self.libri = []

    def aggiungiLibro(self, libro):
        self.libri.append(libro)

    def stampaLibri(self):
        if not self.libri:
            print("La biblioteca è vuota.")
        else:
            for libro in self.libri:
                print(libro)
    
####-MAIN-####
#Variabili
biblioteca = Biblioteca()

while True:
    titolo = input("Inserisci il titolo del libro per cominciare (o [N] per terminare: ").upper()
    
    if titolo == 'N':
        print("Ciao!")
        break
    else:
        autore = input("Inserisci l'autore: ")
        pagine = int(input("Inserisci il numero di pagine: "))
        libro = Libro(titolo, autore, pagine)
        biblioteca.aggiungiLibro(libro)

print("Libri nella biblioteca:")
biblioteca.stampaLibri()

print("STOP")
print("")
