'''
Docstring for CorsoPyML_Deposito_Studente_Giuliani.Settimana_2.2026-02-12_Gio.Teoria-Astrazione
'''

from abc import ABC, abstractmethod

class Animale(ABC):
    @abstractmethod
    def muovi(self):
        pass
    
class Cane(Animale):
    def muovi(self):
        print("Corro")
        
class Pesce(Animale):
    def muovi(self):
        print("Nuoto")
        
        
class Forma(ABC)