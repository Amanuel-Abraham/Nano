from Sprint_1.Raad_het_nummer import raad_het_nummer
from Sprint_2.Galgje import main
from Sprint_1.Raad_het_nummer import raad_het_nummer


import os
bestandsnaam = os.path.join(os.path.dirname(__file__), "..", "Sprint_2", "galgje.txt")
def toonweer():
    import requests

    resource_uri = "https://api.open-meteo.com/v1/forecast?latitude=52.09&longitude=5.12&current_weather=true"

    response = requests.get(resource_uri)
    response_data = response.json()

    weerbericht = response_data["current_weather"]
    temp = weerbericht["temperature"]
    wind = weerbericht["windspeed"]


    # print(response_data)
    # print(weerbericht)
    print(f"De temperature : {temp} \n"
          f"De windsnelheid : {wind} ")




def welkom():
    print("===================================")
    print("     WELKOM BIJ DE GAME")
    print("===================================")
    print()
    print("Kies een spel dat je wilt spelen:")
    print("1: Raad het nummer ")
    print("2: Galgje ")
    print("3: Stoppen ")
    print("4: Toon de weer")
    print()

    try:
        keuze = int(input("Voer je keuze in (1-4): "))
    except ValueError:
        print("Ongeldige invoer! Kies een nummer.")
        return None

    return keuze


while True:
    keuze = welkom()

    if keuze == 1:
        print("Je hebt gekozen voor Raad het nummer!")
        raad_het_nummer()
    elif keuze == 2:
        print("Je hebt gekozen voor Galgje!")
        main(bestandsnaam)
    elif keuze == 3:
        print("Bedankt voor het spelen! ")
        break
    elif keuze == 4:
        toonweer()
    else:
        print("Ongeldige keuze, probeer opnieuw.")


