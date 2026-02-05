
'''
While e For
'''

#WHILE
'''
Il Ciclo While si usa quando non si sa quante volte bisogna iterare
'''

#Variabili
i = 0
lista = [2, 4, 6, 8, 10, 12, 14]

while (i < len(lista)-1):
    print("Stampa l'elemento lista[i]:", lista[i], "incrementando i:", i, "a ogni giro")
    i += 1



#FOR
'''
Il Ciclo For si usa quando si sa che si itererà un tot numero di volte
'''

#Variabili
lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

for elemento in lista:
    print("Per ogni elemento in lista, stampa l'elemento:", elemento)
    
    #RANGE
    '''
    Il Range si usa nei cicli FOr per iterare su un insieme di valori interi
    '''
    for i in range(1, 30, 3):
        print("La funzione incorporata range(1, 30, 2) stampa tutti i valori da 1 a 30 (escluso) con un passo di 3:", i)