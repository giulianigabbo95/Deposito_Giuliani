from datetime import datetime


class Turno:
    def __init__(self, ora_inizio, ora_fine):
        self._ora_inizio = ora_inizio
        self._ora_fine = ora_fine

    def ePuntuale(self):
        ora_attuale = datetime.now().time()
        if self._ora_inizio <= ora_attuale and ora_attuale <= self._ora_fine:
            return True
        else:
            return False
        
    # def stampa
        
    def __str__(self):
        return f"Turno: {self._ora_inizio.strftime('%H:%M')} - {self._ora_fine.strftime('%H:%M')}"