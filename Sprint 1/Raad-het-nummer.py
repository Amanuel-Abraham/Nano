import random
from random import randint

def genereer_getal(moeilijkheid):

    if moeilijkheid == 1:
        moeilijkheid = str("easy")
        getal = randint(1,10)
    elif moeilijkheid == 2:
        moeilijkheid = str("normaal")
        getal = randint(1,50)
    elif moeilijkheid == 3:
        moeilijkheid = str("moeilijk")
        getal = randint(1,100)

    # print(moeilijkheid)
    return (getal)

def max_pogingen(moeilijkheid):
    if moeilijkheid == 1:
        moeilijkheid = str("easy")
        max_pogingen = 5
    elif moeilijkheid == 2:
        moeilijkheid = str("normaal")
        max_pogingen = 7
    elif moeilijkheid == 3:
        moeilijkheid = str("moeilijk")
        max_pogingen = 10

    return max_pogingen


def raad_het_nummer():

    # naam
    naam = input("wat is je naam:")
    # Functie genereer_getal(moeilijkheid) returnt het te raden getal
    moeilijkheid = int(input("Kies een moeilijkheid (1=easy, 2=normaal, 3=moeilijk):"))
    getal = genereer_getal(moeilijkheid)
    print(getal)
    #Functie  max_pogingen(moeilijkheid) returnt 5, 7 of 10
    poging = max_pogingen(moeilijkheid)
    print(f"Je hebt  {poging}  pogingen.")

    getal_raden = int(input('Doe een gok (of enter om te stoppen):'))
    print(getal_raden)
    tip = "hoger"

    for x in range(poging -1):

        if getal_raden == getal:
            print("gelukt je hebt geraden")
            break
        elif getal_raden != getal:
            if getal_raden > getal:
                tip = "lager"
            else:
                tip = "hoger"
            aantal = (poging -1) - x
            print(f"Je hebt nog {aantal} pogingen. TIP: {tip}")
            getal_raden = int(input('Doe nog een gok (of enter om te stoppen):'))
        elif getal_raden == "":
              print("er is iets gegaan")

        # elif getal_raden != getal and getal_raden > getal:
        #  aantal = (poging -1) - x
        #  print(f"Je hebt nog {aantal} pogingen. TIP: {tip}")
        #  getal_raden = int(input('Doe nog een gok (of enter om te stoppen):'))
        #
        # elif getal_raden != getal and getal_raden < getal:
        #  aantal = (poging - 1) - x
        #  print(f"Je hebt nog {aantal} pogingen. TIP: hoger raden")
        #  getal_raden = int(input('Doe nog een gok (ozf enter om te stoppen):'))




raad_het_nummer()




