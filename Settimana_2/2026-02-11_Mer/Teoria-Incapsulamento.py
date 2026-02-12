'''
Incapsulamento


'''

x = 10
print(x)

class Pippo():
    x = 20
    __y = 30            # Incapsulamento attivo
    
    def get_y(self):
        z = 40          # Incapsulamento passivo
        return self.__y
        
        
    
p = Pippo()

print(x)
print(p.x)
print("Scrivere p.__y genera errore")    #
print(p.get_y())









class Computer:
    def __init__(self):
        self.__processore = "Intel i5" # Attributo privato
        
    def get_processore(self):
        return self.__processore
    
    def set_processore(self, processore):
        self.__processore = processore
        
pc = Computer()
print(pc.get_processore())

pc.set_processore("AMD Ryzen 5")    # Accede all'attributo privato tramite il getter
print(pc.get_processore())          # Modifica l'attributo privato tramite il setter










# Variabile Globale
numero = 10

def funzione_esterna():
    # Variabile lcoale nella funzione esterna
    numero = 5
    print("Numero dentro funzione_esterna", numero)
    
    def funzione_interna():
        # Utilizzo nonlocal per modificare la variabile locale della funzione esterna
        nonlocal numero
        numero = 3
        print("Numero dentro funzione_interna (nonlocal):", numero)
    
    print("Numero dentro funzione_esterna", numero)
    
    funzione_interna()
    
print("Numero nel main (globale):", numero)
funzione_esterna()
print("Numero nel main dopo chiamata (globale non cambiato):", numero)