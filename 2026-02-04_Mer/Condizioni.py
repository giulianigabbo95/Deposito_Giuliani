
'''
If, Elif, Else e Match
Controllo del Flusso
'''

print("Questa è la 2° lezione")

#Variabili
x = input("Dimmi un numero:")
y = input("Dimmene un altro:")
parola = input("Come ti chiami? ")



if x < y : print("Condizione in singola linea")

if x < y :
    print("Condizione")
    print("in multi linea")

if (x < y): print("Condizione in singola linea e con parentesi")

if (x < y):
    print("Condizione")
    print("in multi linea e con parentesi")


if x < y :
    print("Numero 1 < Numero 2")
elif x == y :
    print("Numero 1 = Numero 2")
elif x > y :
    print("Numero 1 > Numero 2")
else :
    print("Credo tu abbia sbagliato")


if x < y :
    print("IF")
else :
    print("ELSE")


if x < y :
    print("IF")
    if x < 5 :
        print("IF ANNIDATO")
else :
    print("ELSE")
    

parola.lower()
match parola:
    case "gabriele":
        print("Sei il proprietario di questo PC!")
    case "mirko":
        print("Sei il docente di questo corso!")
    case _: # Caso DEFAULT in cui parola non corrisponde a nessun'altra stringa elencata nei case precedenti. Praticamente è un un ELSE
        print("Non ti conosco")