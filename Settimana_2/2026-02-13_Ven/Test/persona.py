from abc import ABC, abstractmethod
from datetime import datetime


class Persona(ABC):
    def __init__(self, nome, cognome, id_persona):
        self._nome = nome
        self._cognome = cognome
        self._id = id_persona

    @abstractmethod
    def eAutorizzato(self):
        pass

    def stampaGeneralita(self):
        print("(", self._id, ",", self._cognome, ",", self._nome, ")")
        
    def __str__(self):
        return self.stampaGeneralita()


class Dipendente(Persona):
    def __init__(self, nome, cognome, id_persona, turno, badge):
        super().__init__(nome, cognome, id_persona)
        self._turno = turno
        self._badge = badge

    def eAutorizzato(self):
        if self._badge.eAttivo() == True and self._turno.ePuntuale() == True:
            return True
        else:
            return False
        
    # def stampa
    
    def __str__(self):
        return f"Dipendente: {self.stampaGeneralita()} - {self._turno} - {self._badge}"


class Visitatore(Persona):
    def __init__(self, nome, cognome, id_persona, autorizzato):
        super().__init__(nome, cognome, id_persona)
        self._autorizzato = autorizzato

    def eAutorizzato(self):
        return self._autorizzato
    
    def __str__(self):
        if self._autorizzato == True:
            stato = "Autorizzato"
        else:
            stato = "Non Autorizzato"
        return f"VISITATORE: {self.stampaGeneralita()} - {stato}"