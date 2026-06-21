from types import NoneType
import random

R = "rood"
G = "groen"
B = "blauw"
P = "paars"
W = "wit"
Z = "zwart"


kleuren = {"R": R, "G": G, "B": B, "P": P, "W": W, "Z": Z}
record = 0
# Deze variabel is alleen nodig voor aan het einde van de rondes en het spel
verlies = False


# Deze variabel is nodig zodat er niks fout gaat bij poging 10 (winst of verlies)
def geef_feedback(gok_kleuren, geheime_code, gok):
    goedePlaats = 0
    verkeerdePlaats = 0

    over_geheim = []
    over_gok = []

    if len(gok) == 4:
        # Eerst de Z's tellen
        for i in range(4):
            if gok_kleuren[i] == geheime_code[i]:
                goedePlaats += 1
            else:
                over_geheim.append(geheime_code[i])
                over_gok.append(gok_kleuren[i])

        # Daarna de W's tellen
        for kleur in over_gok:
            if kleur in over_geheim:
                verkeerdePlaats += 1
                over_geheim.remove(kleur)

        return "Z" * goedePlaats + "W" * verkeerdePlaats
        # Geeft aan hoeveel Z's en W's de speler heeft gegokt
    else:
        return gok


def geef_begin_tekst():
    print("Welkom bij het spel Mastermind.")
    print(
        "De computer genereert een code van 6 kleuren: \nRood (R), Groen (G), Blauw (B), Paars (P), Wit (W), Zwart (Z)."
    )
    print("Vul de input in als XXXX, waarbij X de eerste letter van de kleur is.")
    print("Je hebt 10 pogingen om de correcte code te raden.")
    print("Als de invoer niet kloppend is verlies je die poging.")
    print(
        "In de feedback betekent een Z: juiste kleur op de juiste plaats; een W: juiste kleur op de verkeerde plaats."
    )
    print('Als je "skip" invoert stop je de huidige ronde en wordt de score gereset.')
    print("Succes!")
    print("")
    print("")
    # Dit is de begin tekst vooraf aan iedere ronde


def doe_een_gok():
    # Als de invoer goed is, doe dan break uit de loop of ga door
    # Maak je een fout, doe dan continue
    while True:
        gok = input("Voer een code van 4 kleuren in XXXX: ").upper()
        if gok == "SKIP":
            return gok
        break

    if gok != "SKIP":
        return list(gok)
    # Maakt van 4 letters een lijstje van 4 letters


# 1 spel
def start_een_spel(record, verlies):
    geef_begin_tekst()
    geheime_code = random.choices(["R", "G", "B", "P", "W", "Z"], k=4)
    # Dit maakt een random code, lengte van 4, met de keuze uit de bovenstaande (6) letters

    pogingen = 0
    for pogingen in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        # Variabel "pogingen" krijgt na elke poging een waarde van +1 (met als begin waarde "1")
        print("Poging", pogingen)
        gok = doe_een_gok()

        if gok == geheime_code and verlies != True:
            print("Gefeliciteerd! Dat was de code. Je hebt gewonnen.")
            if verlies != True:
                if record == "SKIP" or record == None:
                    record = 0
                    # Record wordt alleen gereset als het moet
                if pogingen < record or record == 0:
                    record = pogingen
                    # Als bij winst het aantal pogingen kleiner is dan de vorige getal van record wordt het aantal pogingen van nu het record
            verlies = False
            # "verlies" wordt weer gereset
            return record
            # Eindigt deze ronde en geeft het record voor aan het einde van het spel
        if gok == "SKIP":
            print("De geheime code was: ", "".join(geheime_code))
            return
            # Dit is als de speler deze ronde wilt overslaan/score wilt resetten
        feedback = geef_feedback(gok, geheime_code, gok)
        if feedback == "":
            feedback = "Niks is correct"
            # Als er geen feedback is krijgt de speler duidelijk te zien dat alles incorrect is
        if len(gok) != 4 or not all(k in kleuren for k in gok):
            print("Foute invoer, probeer het opnieuw.")
            print("")
            continue
            # De all() is met behulp van AI
            # Als (gok) niet een geldige gok is verliest de speler een beurt en krijgt hij/zij een melding
        if gok != geheime_code:
            print(
                "Een Z betekent op zijn plek, een W betekent niet op zijn plek: "
                + feedback
            )
            print("")

    print("")
    # De join gevonden op het internet, zodat de lijst met letters weer 1 string wordt
    if gok != geheime_code and pogingen == 10 and gok != "SKIP":
        print("Jammer! Je hebt verloren. De geheime code is: " + "".join(geheime_code))
        verlies = True
    return record


# Spelletjes
ronde = 1
opnieuw = "ja"
while opnieuw == "ja":
    record = start_een_spel(record, verlies)
    print("")
    opnieuw = input("Wil je nog opnieuw spelen? (ja/nee) ").lower()
    print("")
    while opnieuw not in ["ja", "nee"]:
        opnieuw = input("Kunt u dat opnieuw invoeren? ").lower()
        # Als de speler geen ja of nee zegt dan wordt er opnieuw naar een antwoord gevraagd
    print("")
    if opnieuw == "nee":
        # Als de speler nee zegt stop het spel en krijgt hij/zij het volgende de zien:
        print("")
        print("")
        print(r"""
                                    ___________
                                   '._==_==_=_.' 
                                   .-\:      /-.
                                  | (|:.     |) |
                                   '-|:.     |-'
                                     \::.    /
                                      '::. .'
                                        ) (
                                      _.' '._
                                     `'''''''`

                            ╔════════════════════════╗
                            ║       BESTE SCORE      ║
                            ╠════════════════════════╣""")
        if record == 1:
            print("                            ║       ", "1", " POGING       ║ ")

        elif record == 0 or record == None:
            print("                            ║      ", "-", " POGINGEN      ║ ")
        elif record == 10:
            print("                            ║      ", "10", "POGINGEN      ║ ")
        elif record != 0 and record != None:
            print("                            ║      ", record, " POGINGEN      ║ ")
        print(r"""                            ╚════════════════════════╝

                             Bedankt voor het spelen! 




        """)
        # De speler krijgt hier te zien wat zijn/haar beste score is.
        # Er zijn 2 soorten uitkomsten, maar bij "1" en "10" zou het tabel niet meer heel zijn, dus is er een aparte "print" functie nodig.
        # De r""".....""" hebben we met AI ontdekt, het geeft de tekst letterlijk hoe het staat,
        # Bijvoorbeeld is een backslash gewoon aangegeven als een backslash en hoeft er geen "\" voor te staan.
        # Ook hebben we die trofee en tabel met behulp van ChatGPT gemaakt.

    else:
        print("")
        print("")
        ronde += 1
        print("Ronde: " + str(ronde))
        print("")
        # Speler krijgt te zien in welke ronde hij/zij nu zit als er een volgende ronde is.
        # Vanaf ronde 2 ziet de speler elke keer in welke ronde hij/zij zit.
