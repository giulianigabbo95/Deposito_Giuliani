'''
Esercizio 2
Scrivi un programma che:
1. Chiede all'utente di inserire due numeri che definiscono un intervallo (ad esempio 10 e 50).
2. Individua e stampa:
    - solo i numeri primi, oppure
    - solo i numeri non primi, oppure
    - entrambi, separandoli in due collezioni diverse (a tua scelta).
3. Chiede all'utente se desidera ripetere il programma.
'''

while True:
    #Variabili
    start = 0
    stop = 0
    primi = []
    divisibili = []

#1 - Chiede all'utente di inserire due numeri che definiscono un intervallo.
    while(start <= 0 or stop <= 0):
        print("Inserisci due numeri positivi!")
        start = int(input("Inserisci il primo numero dell'intervallo: "))
        stop = int(input("Inserisci il secondo numero dell'intervallo: "))
        if start >= stop:
            print("Il primo numero deve essere minore del secondo.")

#2 - Individua e stampa:
    for numero in range(start, stop+1, 1):
        if numero < 2:
            primi.append(numero)
        else:
            primo = True
            for num in range(2, numero, 1):
                if numero % num == 0:
                    primo = False
                    break
            if primo == True:
                primi.append(numero)
            else:
                divisibili.append(numero)
    print("Numeri primi nell'intervallo: ", primi)
    print("Numeri non primi nell'intervallo: ", divisibili)
    
#3 - Chiede all'utente se desidera ripetere il programma.
    selezione = input("Vuoi ricominciare? [S] o [N]: ").upper()
    if selezione == "N":
        break
    elif selezione == "S":
        pass
    else:
        print("Hai sbagliato a inserire! Ricomincio comunque.")
        
    print("")