
'''
Liste, Tuple e Insiemi
'''

print("Questa è la 2° lezione")

# LISTE
# Sono Modificabili

#Variabili
numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9] #Lista1
nomi = ["Alice", "Bob", "Charle"] #Lista2


print("Il 1° elemento / L'elmento 0 della lista numeri è numeri[0]:", numeri[0])
print("Il 3° elemento / L'elmento 2 della lista numeri è numeri[2]:", numeri[2])
print("Tutta la lista numeri è:", numeri)
print("Se stampo una posizione che non esiste come numeri[30], ricevo errore 'IndexError: list index out of range'")
#print(numeri[30]) #NON DeCommentare - Genera Errore!

numeri[4] = 10
print("Posso modificare una parte della lista con numeri[4] = 10:", numeri)
print("Posso anche stampare la lunghezza della lista con len(numeri):", len(numeri))

numeri.append(6)
numeri.insert(2,10)
numeri.remove(4)
numeri.sort()
print("Posso anche agguiungere, inserire rimuovere, ordinare gli elementi con numeri.append(6), numeri.insert(2,10), numeri.remove(4), numeri.sort():", numeri)




# TUPLE 
# Sono Immutabili 

#Variabili
mix = [1, "due", True, 4.5] #Lista3
punto = 3, 4 #Tupla1 - A volte può essere senza parentesi - MA Quando?
colore_rgb = (255, 128, 0) #Tupla2
info_personali = ("Alice", 25, "F") #Tupla3


print("Il 2° elemento / L'elemento 1 della lista numeri è punto[1]:", punto[1])



# INSIEMI
# Sono omogenei, tengono solo un tipo di dato alla volta

#Variabili
gruppo = set([1, 2, 3, 4, 5]) #Insieme1 - A volte si usa set(...) - MA Quando? Con le []?
gruppetto = {4, 5, 6} #Insieme2 - Si può usare anche con {}


print("L'insieme 1 unito al 2 è:", gruppo.union(gruppetto)) # Nuovo insieme con tutti gli elementi presenti in entrambi gli insiemi
print("L'insieme 1 intersecato al 2 è:", gruppo.intersection(gruppetto)) # Nuovo insieme con solo gli elementi comuni a entrambi gli insiemi
print("L'insieme 1 sottratto al 2 è:", gruppo.difference(gruppetto)) # Nuovo insieme con gli elementi del primo insieme ma non nel secondo
print("L'insieme 1 con differenza simmetrica con il 2 è:", gruppo.symmetric_difference(gruppetto)) #  Nuovo insieme con gli elementi solo in uno degli insiemi, ma non in entrambi
print("Posso sapere la lunghezza del gruppo con len(gruppo):", len(gruppo))

gruppo.add(45)
print("Posso aggiungere un elemento all'insieme con add(45):", gruppo)

gruppo.remove(45)
print("Posso rimuovere un elemento dall'insieme con remove(45) o discard(45);", gruppo) #La differenza è che il primo genera un errore se l'elemento non è presente nell'insieme

gruppone = gruppo.copy()
print("Posso copiare il gruppo con gruppone = gruppo.copy:", gruppone)