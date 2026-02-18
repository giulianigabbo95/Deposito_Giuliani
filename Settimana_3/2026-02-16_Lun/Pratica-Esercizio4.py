'''
Scrivere un programma che prenda i nomi degli alunni di una classe e i loro voti.
Quando l'utente scrive media il programma andrà a stampare i nomi di tutti gli alunni e per ogni alunno la media dei voti.
Esempio:
    Nome: Giovanni, Media: 7.5
    Nome: Alfredo, Media: 9
    Nome: Michela, Media 10
'''

studenti = {}

while True:
    nome_studente = input('Inserisci un nome o "media" per ottenere la media dei voti: ').lower()
    
    if nome_studente == 'media':
        break
    
    if nome_studente not in studenti:  # Uguale a dire studenti.keys() perché sottointeso
        studenti[nome_studente] = {}
        
        while True:
            nome_materia = input('Inserisci una materia o "stop" per uscire: ').lower()
            
            if nome_materia == 'stop':
                break
            
            if nome_materia not in studenti[nome_studente]:
                studenti[nome_studente][nome_materia] = []
                
                while True:
                    voto = int(input('Inserisci il voto o "stop" per uscire: '))
                    
                    if voto == 'stop':
                        break
                    
                    studenti[nome_studente][nome_materia].append(float(voto))
            
            else:
                print('Materia presente!')

    else:
        print('Studente già presente!')

'''
studenti = {
    'gabriele': {
        'scienze': [2.0], 
        'matematica': [
            5.0, 
            9.0
        ]
    }, 
    'alessio': {
        'inglese': [
            5.0, 
            10.0
        ]
    }
}
'''

for nome, valore in studenti.items():
    lista_voti = []
    
    for voti in valore.values():
        lista_voti.extend(voti)
    
    if len(lista_voti) > 0:
        media = sum(lista_voti) / len(lista_voti)
        print(f"Nome: {nome}, Media: {media}")
    else:
        print(f"Nome: {nome}, Nessun voto inserito")