import random as rnd

def creaGruppi(n_persone:list, n_gruppi:int):
    if n_gruppi > len(n_persone):
        print("Il numero di gruppi deve essere minore o uguale al numero di persone.")
        return
    else:
        rnd.shuffle(n_persone)
        gruppi = [[] for _ in range(n_gruppi)]
        for i, persona in enumerate(n_persone):
            gruppi[i % n_gruppi].append(persona)
        for idx, gruppo in enumerate(gruppi):
            print(f"Gruppo {idx + 1}: {', '.join(gruppo)}")


list_name = [
    "Elisabetta Carella",
    "Fabio D'Alessandro",
    "Gabriele Carucci",
    "Gabriele Giuliani",
    "Giovanni Iadalise",
    "Ilaria Cuccaro",
    "Marco Aurelio De Felicis",
    "Maria Visione",
    "Mariagrazia Nuzzolese",
    "Nico Davide Cognetta",
    "Roberto Dessi",
    "Stefano Romanelli",
    "Valero Carìa",
    "Veronica Veneroso",
]

numero_gruppi = int(input('Quanti gruppi vuoi formare? '))

print(creaGruppi(list_name, numero_gruppi)) 