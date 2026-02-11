'''
Ereditarietà
'''

# Classe Base
class Animale:
    def __init__(self):
        self.nome = NotImplemented
    
    def parla(self):
        print(f"{self.nome} fa suono generico.")
        
# Classe derivata (eredita da Animale)
class Cane(Animale):
    
    def parla(self):
        print(f"{self.nome} abbaia!")
        
animale_generico = Animale("AnimaleGenerico")
cane = Cane("Fido")

animale_generico.parla()    # Output: AnimaleGenerico fa suono generico
cane.parla()                # Output: Fido abbaia!



class Veicolo:
    def __init__(self, marca, modello):
        self.marca =  marca
        self.modello = modello
        
    def mostraInformazioni(self):
        