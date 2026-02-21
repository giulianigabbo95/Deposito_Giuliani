'''
Creare un programma python che permette tramite le api di visualizzare le previsione
metereologiche della città scelta dall'utente.
L'utente potrà scegliere se visionarle dei prossimi 1, 3 o 7 giorni e se
visionare oltre che le temperature anche la velocità del vento e le
probabili precipitazioni.

# In collaborazione con Giovanni Iadelise, Maria Visone e Davide Cognetta
'''

import requests
import webbrowser


def chiediCitta():
    return input("Quale città vuoi cercare? ").capitalize().strip()


def ottieniCoordinate(citta):
    url_geo = f"https://geocoding-api.open-meteo.com/v1/search?name={citta}&count=1&language=it&format=json"
    risposta = requests.get(url_geo)
    dati = risposta.json()
    risultato = dati["results"][0]
    return risultato["latitude"], risultato["longitude"]


def inserisciPreferenze():
    giorni = input("Per quanti giorni vuoi le previsioni? (1, 3, 7): ")
    vuoi_vento = input("Vuoi vedere la velocità del vento? (s/n): ")
    vuoi_pioggia = input("Vuoi vedere le precipitazioni? (s/n): ")
    return giorni, vuoi_vento, vuoi_pioggia


def costruisciUrlMmeteo(lat, lon, giorni, vuoi_vento, vuoi_pioggia):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&forecast_days={giorni}&timezone=auto&daily=temperature_2m_max,temperature_2m_min"
    if vuoi_vento == "s":
        url += ",windspeed_10m_max"
    if vuoi_pioggia == "s":
        url += ",precipitation_sum"
    return url


def stampaPrevisioni(dati):
    previsioni = dati["daily"]
    for i in range(len(previsioni["time"])):
        giorno = previsioni["time"][i]
        t_max = previsioni["temperature_2m_max"][i]
        t_min = previsioni["temperature_2m_min"][i]
        output = f"Giorno: {giorno}, Temperatura max:{t_max}°C, Temperatura min: {t_min}°C"
        if "windspeed_10m_max" in previsioni:
            output += f" Vento: {previsioni['windspeed_10m_max'][i]} km/h"
        if "precipitation_sum" in previsioni:
            output += f" Precipitazioni: {previsioni['precipitation_sum'][i]} mm"
        print(output)


# MAIN
citta = chiediCitta()
lat, lon = ottieniCoordinate(citta)
giorni, vuoi_vento, vuoi_pioggia = inserisciPreferenze()                    #
url_meteo = costruisciUrlMmeteo(lat, lon, giorni, vuoi_vento, vuoi_pioggia)

nuova_risposta = requests.get(url_meteo)
nuovi_dati = nuova_risposta.json()

webbrowser.open(url_meteo)
stampaPrevisioni(nuovi_dati)