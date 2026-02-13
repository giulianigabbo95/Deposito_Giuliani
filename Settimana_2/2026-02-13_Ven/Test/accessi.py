from datetime import datetime


class ControlloAccessi:
    def __init__(self):
        self._log = []

    def verificaAccesso(self, persona):
        consentito = persona.eAutorizzato()
        log = LogAccesso(persona, consentito)
        self._log.append(log)
        if consentito == True:
            print(persona.stampaGeneralita(), "Accesso Consentito")
        else:
            print(persona.stampaGeneralita(), ": Accesso Negato")
        return consentito

    def mostraLog(self):
        print("Logs")
        for record in self._log:
            print(record)

 
class LogAccesso:
    def __init__(self, persona, consentito):
        self._persona = persona
        self._data_ora = datetime.now()
        self._consentito = consentito

    # def stampa
    
    def __str__(self):
        if self._consentito == True:
            stato = "Consentito"
        else:
            stato = "Negato"
        return f"Alle {self._data_ora.strftime('%d/%m/%Y %H:%M:%S')} la persona {self._persona.stampaGeneralita()} è {stato}"