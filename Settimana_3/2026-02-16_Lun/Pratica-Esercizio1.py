'''
Creare un programma che richieda all'utente tre numeri.
Il programma verifica la presenza di almeno due numeri uguali.
Se non ci sono coppie di numeri uguali restituisce il numero più grande dei tre.
'''

print('Modo 1')

a = int(input('Inserisci il 1° numero: '))
b = int(input('Inserisci il 2° numero: '))
c = int(input('Inserisci il 3° numero: '))

numeri = [a, b, c]

massimo = numeri[0]

for n in numeri:
    if numeri[n] == numeri[n+1]:
        print('Ci sono almeno due numeri uguali')
        break
    else:
        if numeri[n+1] > massimo:
            massimo = numeri[n+1]

print('Il maggiore è:', massimo)

##########################

print('Modo 2')

x = int(input('Inserisci il 4° numero: '))
y = int(input('Inserisci il 5° numero: '))
z = int(input('Inserisci il 6° numero: '))

if x == y or x == z or z == y:
    print('Ci sono almeno due numeri uguali')
else:
    maggiore = 0
    if x < y < z or y < x < z:
        maggiore = z
    elif x < z < y or z < x < y:
        maggiore = y
    elif y < z < x or z < y < x:
        maggiore = x
    else:
        print('Hai scordato uan condizione!')
    print('Il maggiore è:', maggiore)
    if z > x and z > y:
        maggiore = z
    elif y > x and y > z:
        maggiore = y
    elif x > z and x > y:
        maggiore = x
    else:
        print('Hai scordato uan condizione!')
    print('Il maggiore è:', maggiore)
    
##########################

print('Modo 3')

def eCoppia(numero1:int, numero2:int):
    True if numero1 == numero2 else False

def eMaggiore(numero1:int, numero2:int):
    True if numero1 > numero2 else False

numeri.append(x)
numeri.append(y)
numeri.append(z)

massimo = numeri[1]

for n in len(numeri)-1:
    if eCoppia(numeri[n], numeri[n+1]):
        print(f'{numeri[n]} e {numeri[n+1]} sono uguali')
    else:
        if eMaggiore(numeri[n+1], massimo):
            massimo = numeri[n+1]
            print(f'Il maggiore è {maggiore}')
            