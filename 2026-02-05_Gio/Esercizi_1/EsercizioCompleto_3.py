'''
Esercizio 3
Scrivi un programma che:
1. Chiede all'utente di inserire due numeri.
2. Calcola e stampa i fattori comuni dei due numeri.
3. Se lunico fattore comune è 1, stampa il messaggio: "I numeri sono coprimi".
4. Ripeti lo stesso concetto con due stringhe:
    - verifica se hanno tutte le lettere in comune (es. "abs" e "sab"),
    - in questo caso le stringhe sono definite "complementari".
5. Al termine, chiede all'utente se vuole ripetere l'operazione.
'''

while True:
    
#1 - Chiede all'utente di inserire due numeri.
    #Variabili
    fattori = []
    minore = 1
    num1 = int(input("Inserisci il 1° numero: "))
    num2 = int(input("Inserisci il 2° numero: "))
    
    if num1 <= 0 or num2 <= 0:
        print("I numeri devono essere entrambi positivi!")
        break
    if num1 > num2:
        minore = num2
    elif num1 < num2:
        minore = num1
    elif num1 == num2:
        print("I numeri sono uguali! Così non vale.")
        break
    else:
        print("Qualcosa è andato storto!")
        break

#2 - Calcola e stampa i fattori comuni dei due numeri.
    for i in range(1, minore + 1, 1):
        if num1 % i == 0 and num2 % i == 0:
            fattori.append(i)

#3 - Se lunico fattore comune è 1, stampa il messaggio: "I numeri sono coprimi".
    if len(fattori) == 1:
        print("I numeri sono coprimi!")
    else:
        print("Fattori comuni: ", fattori)

#4 - Ripeti lo stesso concetto con due stringhe.
    #Variabili
    complementari = True
    str1 = input("Inserisci la prima stringa: ").lower()
    str2 = input("Inserisci la seconda stringa: ").lower()

    '''
    #Alternativa più precisa
    if len(str1) != len(str2):
        print("Stringhe diverse!")
        break
    else:
        alfabeto = "abcdefghijklmnopqrstuvwxyz"

        for lettera in alfabeto:
            conta1 = 0
            conta2 = 0

            for c in str1:
                if c == lettera:
                    conta1 += 1
            for c in str2:
                if c == lettera:
                    conta2 += 1
    
    '''
    for lettera in str1:
        if lettera not in str2:
            complementari = False
    if complementari:
        print("Le stringhe sono complementari")
    else:
        print("Le stringhe NON sono complementari")

#5 - Al termine, chiede all'utente se vuole ripetere l'operazione.
    selezione = input("Vuoi ricominciare? [S] o [N]: ").upper()
   
    if selezione == "N":
        break
    elif selezione == "S":
        pass
    else:
        print("Hai sbagliato a inserire! Ricomincio comunque.")
    
    print("")