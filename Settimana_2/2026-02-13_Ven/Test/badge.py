class Badge:
    def __init__(self, codice):
        self._codice = codice
        self._attivo = True

    def eAttivo(self):
        return self._attivo

    def disattivaBadge(self):
        self._attivo = False

    def get_codice(self):
        return self._codice
    
    # def stampa
    
    def __str__(self):
        stato = "Attivo" if self._attivo else "Disattivato"
        return f"Badge: {self._codice} ({stato})"