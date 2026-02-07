
'''
Break, Continue, Pass e Splat
'''
#Variabili
numeri = [1, 2, 3, 4, 5]

#BREAK
'''
Break viene utilizzato per interrompere l'esecuzione di un ciclo in anticipo se si verifica una condizione specifica.
'''


for numero in numeri:
    if numero == 3:
        print("Il comando 'if numero == 3: break' su un ciclo for sulla mia lista di numeri:", numeri, "si blocca prima della stampa del numero 3")
        break
    print(numero)
    
    

print("")
#CONTINUE
'''
Continue viene utilizzato per saltare il resto del blocco di codice all'interno di un ciclo e passare alla prossima iterazione. 
'''

for numero in numeri:
    if numero == 3:
        print("Il comando 'if numero == 3: continue' su un ciclo for sulla mia lista di numeri:", numeri, "salta la stampa del numero 3")
        continue
    print(numero)



print("")
#PASS
'''
Pass serve come segnaposto per un'istruzione vuota, quindi viene utilizzato quando non si desidera eseguire alcuna azione all'interno di un ciclo. 
'''

for i in range(5):
    if i == 3:
        pass
    else:
        print("Con if", i , "== 3: pass non entro in questo ELSE e quindi in questa stampa ma vado avanti anche se l'if è vuoto! Senza 'pass' riceverei errore!")



print("")
#Splat a.k.a. *
'''
Splat viene utilizzato per espandere un iterabile (come una lista, una tupla o un range) in elementi separati.
'''

numeri = [*range(1, 11, 3)]
print("il comando [*range(1, 11, 3)] stampa tutti i numeri da 1 a 10 con un passo di 3:", numeri)
# In questo caso, [*range(1, 11)] espande la sequenza di numeri generati da range(1, 11) nella lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
# L'operatore * svolge il ruolo di "splat", consentendo di trattare gli elementi dell'iterabile come elementi separati nella lista.