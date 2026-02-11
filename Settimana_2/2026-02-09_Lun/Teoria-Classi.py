'''
Classi

'''
print("")
print("START")

class Persona():
    x = 10
    def __init__(self):
        pass
    
class Pippo:
    def __init__(self):
        pass

gabriele_OBJ = Persona()
marco_OBJ = Persona()
salvatore_OBJ = Persona()
salvatore_OBJ.x = 17

print(Persona)
print(gabriele_OBJ.x)
print(marco_OBJ.x)
print(salvatore_OBJ.x)

franco_OBJ = Pippo()
print(Pippo)
print(franco_OBJ)

print("----------------------------------------------------------")

#Tipi basilari
print(type(10))         # <class 'int'>
print(type(3.14))       # <class 'float'>
print(type("test"))     # <class 'str'>
print(type([1, 2]))     # <class 'list'>

#Tipi NON basilari
class MioOggetto:
    def __init__(self):
        pass
    def __str__(self):
        # Viene richiamato quando facciamo: print(instanza_di_Persona)
        return "Ciao Gabriele sono un metodo speciale"

obj = MioOggetto()
print(type(obj))        # definisce il tipo dell'oggetto

print(obj)

print("----------------------------------------------------------")

class Auto:
    numero_ruote = 4
    
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello
    
    def stampa_info(self):
        print("L'auto è una", self.marca, self.modello)


auto1 = Auto("Opel", "Corsa")
auto2 = Auto("Fiat", "Panda")
auto1.stampa_info()
auto2.stampa_info()


print("----------------------------------------------------------")


class Contatore:
    numero_istanze = 0 # Attributo di Classe
    
    def __init__(self):
        Contatore.numero_istanze += 1
        
    @classmethod
    def mostraNumero_Istanze(cls):
        print(f"Sono state create {cls.numero_istanze} istanze")
    
# Creazione di alcune istanze
c1 = Contatore()
c2 = Contatore()

Contatore.mostraNumero_Istanze()
# Output: Sono state create 2 istanze

print("STOP")
print("")