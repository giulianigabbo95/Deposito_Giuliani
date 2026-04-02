'''
Polimorfismo
Pratica che permette di trattare oggetti di classi diverse attraverso un'interfaccia comune. 
Si manifesta principalmente attraverso l'overriding (sovrascrittura) dei metodi. 
Non essendo supportato l'overloading dei metodi, si possono ottenere risultati simili utilizzando argomenti predefiniti e variadici.
'''
print("")
print("START")
print("Questa è la 8° lezione")

class Animale:
    def emetti_suono(self):
        print("Questo animale fa un suono")

class Cane(Animale):
    def emetti_suono(self):
        print("Bau")

class Gatto(Animale):
    def emetti_suono(self):
        print("Miao")


print("----------------------------------------------------------")
print("STOP")
print("")