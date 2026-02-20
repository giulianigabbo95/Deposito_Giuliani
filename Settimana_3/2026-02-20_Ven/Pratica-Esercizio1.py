'''
Create un programma python utilizzando le api https://pokeapi.co/api/v2/pokemon/ {numero} che simula un pokedex.
Quando troverete un pokemon in maniera randomica verificherà se è presente nel vostro pokedex (pokedex.json).
In caso non fosse presente vi permetterà di catturarlo salvando le caratteristiche.
(Sul sistema API sono presenti poco più di 1000 Pokémon)

# In collaborazione con Giovanni Iadelise, Maria Visone e Davide Cognetta
'''

import json
import random
import requests


#NOME_FILE = "pokedex.json"
NOME_FILE = r"C:/Users/Gahab/Documents/GitHub/Corso_PyML_Deposito_Studente_Giuliani/Settimana_3/2026-02-20_Venr/pokedex.json"


def caricaPokedex():
    try:
        with open(NOME_FILE, "r") as file:
            pokedex = json.load(file)
        print("pokedex pronto!")
    except:
        pokedex = {}
        #print("pokedex caricato", pokedex) # Debug
    return pokedex


def stampaPokemonInfo(dex_number):
    url_pokedex = f"https://pokeapi.co/api/v2/pokemon/{dex_number}"
    try:
        response = requests.get(url_pokedex)
        if response.status_code == 200:
            raw_data = response.json()
            #print(f"Dati grezzi ricevuti per: {raw_data['name']}" # Debug
            pokemon_data = {
                "nome": raw_data["name"],
                "pokedex_N°": raw_data["id"],
                "type": [t["type"]["name"] for t in raw_data["types"]]
            }
            #print(pokemon_data) # Debug
            return pokemon_data
        else:
            print("Errore: Pokémon is MissingNO")
            return None
    except Exception as e:
        print(f"Errore di connessione: {e}")
        return None


def eCatturato(id_pkmn, pkdex):
    if id_pkmn in pkdex: # Scrivere "in pkdex" è uguale a scrivere "in pkdex.keys()" IN QUESTO CASO
        return True
    else:
        return False


#MAIN
pokedex = caricaPokedex()
numero_incontro = 0

while True:
    id_pokemon = random.randint(1, 1025)
    print(f"Incontro numero {numero_incontro+1}: è apparso il pokemon {id_pokemon}")
    if eCatturato(id_pokemon, pokedex) == True:
        print("Questo Pokémon è già stato catturato!")
        # print("Vuoi provare a catturare un altro esemplare?") # DA IMPLEMENTARE
        print("Fuga!")
    else: 
        print("Questo Pokémon non è stato catturato!.")
        print("Lo cerco su internet...")
        pokemon = stampaPokemonInfo(id_pokemon)
        if pokemon is not None: # Scrivere "pokemon is not None" è uguale a scrivere solo "pokemon" IN QUESTO CASO
            print(f"Hai incontrato {pokemon['nome'].capitalize()}!")
            print("Tipo:", ", ".join(pokemon["type"]))
            scelta = input("Vuoi catturarlo? [S] o [N]: ").lower()
            if scelta == "s":
                pokedex[str(id_pokemon)] = pokemon
                with open(NOME_FILE, "w") as f:
                    json.dump(pokedex, f, indent=4)
                print(f"Preso! {pokemon['nome']} salvato nel pokedex.")
            else:
                print("Scampato Pericolo!")
    uscita = input ("Vuoi continuare a giocare? [S] o [N]").lower()
    if uscita == "n":
        print ("Grazie per aver giocato")
        break

print(f"Fine dei {numero_incontro} incontri!")