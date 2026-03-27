import random

from requests import delete
from urllib3.http2.probe import acquire_and_get

score_bestand = "score.txt"
bestandsnaam = "galgje.txt"


def main(bestandsnaam):

    while True:
        print("1. Speel galgje")
        print("2. Verwijder een woord uit de woordenlijst.")
        print("3:Voeg woord toe aan de woordenlijst.")
        print("4:Toon aantal woorden in de woordenlijst.")
        print("5:Stoppen")
        keuze = int(input("Keuze: "))

        if keuze == 1:
            speelsessie(lees_woorden(bestandsnaam))
        elif keuze == 2:
            bestand = lees_woorden(bestandsnaam)

            for woord in bestand:
                print(woord)

            gekozen_woord = input("kies de woord die je wilt verwijderen ? ")

            if gekozen_woord in bestand:
                verwijderen = bestand.pop(gekozen_woord)
                print("de woord die je gekozen hebt is verwijdert")
                sla_woorden_op(bestandsnaam, bestand)
            else:
                print("de woord die je hebt gekozen is niet gevonden (probeer nog een keer)")
                gekozen_woord = input("kies de woord die je wilt verwijderen ? ")


        elif keuze == 3:
            woord = lees_woorden(bestandsnaam)
            nieuwe_woord = input("voer een woord in? ")
            if len(nieuwe_woord) < 6:
                moeilijkheid = 1
                woord[nieuwe_woord] = moeilijkheid
            elif len(nieuwe_woord) >= 7 and len(nieuwe_woord) <= 11:
                moeilijkheid = 2
                woord[nieuwe_woord] = moeilijkheid
            elif len(nieuwe_woord) > 11:
                moeilijkheid = 3
                woord[nieuwe_woord] = moeilijkheid

            sla_woorden_op(bestandsnaam, woord)

            print(f"{nieuwe_woord} is toegevoegd """)

        elif keuze == 4:
            aantal_woorden = len(lees_woorden(bestandsnaam))
            print(f"het aantal woorden in de woordenlijst is {aantal_woorden}")


        if keuze == 5:
            print("Tot volgende keer ")
            break


def lees_woorden(bestandsnaam):
    try:
        woorden_dict = {}

        with open(bestandsnaam, "r") as bestand:
            inhoud = bestand.read()
            text = inhoud.split()

        for woord in text:
            if len(woord) < 6:
                moeilijkheidgraad = 1
                woorden_dict.update({woord: moeilijkheidgraad})
            elif len(woord) >= 7 and len(woord) <= 11:
                moeilijkheidgraad = 2
                woorden_dict.update({woord: moeilijkheidgraad})
            elif len(woord) > 11:
                moeilijkheidgraad = 3
                woorden_dict.update({woord: moeilijkheidgraad})
    except FileNotFoundError:
        print(f"Fout: Het bestand '{bestandsnaam}' is niet gevonden.")
        return {}


    return woorden_dict


def  sla_woorden_op(bestandnaam, woorden_dict):
    with open(bestandnaam, "w") as bestand:

        for woorden in woorden_dict:
            bestand.write(woorden + "\n")


def bereken_score(aantal_levens_over, moeilijkheid):

    score = aantal_levens_over * moeilijkheid

    return score

def voeg_score_toe(naam, woord, score):

    with open(score_bestand, "a") as bestand:
        bestand.write(F"{naam},{woord},{score}\n")


def toon_tussenstand(woord, geraden_letters):
    woorden = []

    for letter in woord:
        if letter in geraden_letters:
            hoofdletter = letter.upper()
            woorden.append(hoofdletter)
        else:
            woorden.append("_")


    galgje_woord = ' '.join(woorden)
    print(galgje_woord)

    return galgje_woord


def kies_woord(woorden_dict, moeilijkheidsgraad):
    moeilijkheid = []

    if woorden_dict == {}:
        print("de bestand is leeg")
        random_woord = ""
    else:
        for woord in woorden_dict:
            if woorden_dict[woord] == moeilijkheidsgraad:
                moeilijkheid.append(woord)

        random_woord = random.choice(moeilijkheid)

    return random_woord


def speelsessie(woorden_dict):
    gebruiker = str(input("Naam:"))
    geraden_letters = set()
    aantal_pogingen = 0
    while True:
        try:
            moeilijkheidsgraad = input("Kies een moeilijkheidsgraad kiezen (1, 2 of 3)")
            moeilijkheidsgraad_getal = int(moeilijkheidsgraad)
            if moeilijkheidsgraad_getal >= 1 and moeilijkheidsgraad_getal <= 3:
                break
            else:
                print("ongeldige invoer")

        except ValueError:
            print("voer nog een keer ")


    woord = kies_woord(woorden_dict,moeilijkheidsgraad_getal)
    if woord == "":
        print("bestand is niet gevonden of de bestand is leeg")
        return
    else:
        toon_tussenstand(woord, geraden_letters)

        if moeilijkheidsgraad_getal == 1:
            aantal_levens = 10

        elif moeilijkheidsgraad_getal == 2:
            aantal_levens = 8

        elif moeilijkheidsgraad_getal == 3:
            aantal_levens = 6

        while aantal_levens > 0 and set(woord) != geraden_letters:
            raden = input("voer een  letter in: ")
            aantal_pogingen += 1
            if raden == "":
                break
            elif raden in woord:
                geraden_letters.update(raden)
                toon_tussenstand(woord, geraden_letters)
            elif raden in geraden_letters:
                print("deze is letter is ingevoerd")
            elif raden != geraden_letters:
                aantal_levens -= 1
                print("!FOUT")

        resultaat = bereken_score(aantal_levens, moeilijkheidsgraad_getal)
        voeg_score_toe(gebruiker, woord, resultaat)
        if set(woord) == geraden_letters:
            print(f"Word: {woord} | Resultaat: WIN")
            print(f"Pogingen: {aantal_pogingen}  | Levens resterend : {aantal_levens}")
            print(f"score:{resultaat}")

        else:
            print(f"Word: {woord} | Resultaat: VERLIES")
            print(f"Pogingen: {aantal_pogingen}  | Levens resterend : {aantal_levens}")
            print(f"score:{resultaat}")
            print(woord, "|", resultaat)











