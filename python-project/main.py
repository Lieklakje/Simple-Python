import random

R = "rood"
G = "groen"
B = "blauw"
P = "paars"
W = "wit"
Z = "zwart"

kleuren = {"R": R, "G": G, "B": B, "P": P, "W": W, "Z": Z}


def geef_feedback(gok_kleuren, geheime_code):
    goedePlaats = 0
    verkeerdePlaats = 0
    
    over_geheim = []
    over_gok = []
    
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


def geef_begin_tekst():
    print("Welkom bij het spel Mastermind.")
    print("De computer genereert een code van 6 kleuren: Rood (R), Groen (G), Blauw (B), Paars (P), Wit (W), Zwart (Z).")
    print("Vul de input in als XXXX, waarbij X de eerste letter van de kleur is.")
    print("Je hebt 10 pogingen om de correcte code te raden.")
    print("In de feedback betekent een Z: aantal op de goede plaats. En W: aantal in de geheime code, maar op de verkeerde plaats")
    print("Succes!")

def doe_een_gok():
    # Doe een gok
    # Als de invoer goed is, doe dan break uit de loop of ga door
    # Maak je een fout, doe dan continue
    while True:
        gok = input("Voer een code van 4 kleuren in XXXX: ").upper()
        # De all() test is met behulp van AI
        if len(gok) != 4 or not all(k in kleuren for k in gok):
            print("Foute invoer, probeer het opnieuw.")
            print("")
            continue

        # werkt goed blijkbaar
        #print(gok)
        break

    # Maakt van 4 letters een lijstje van 4 letters. Handig voor straks
    return list(gok)

# 1 spel
def start_een_spel():
    geef_begin_tekst()
    geheime_code = random.choices(["R", "G", "B", "P", "W", "Z"], k=4)
    # print(geheime_code)

    print("")

    pogingen = 0
    while pogingen < 10:
        pogingen += 1
        print("")
        print("Poging", pogingen)
        gok = doe_een_gok()

        if gok == geheime_code:
            print("Gefeliciteerd! Dat was de code. Je hebt gewonnen.")
            return

        feedback = geef_feedback(gok, geheime_code)
        print("Een Z betekent op zijn plek, een W betekent niet op zijn plek: " + feedback)

    print("")
    # de join gevonden op het internet, zodat de lijst met letters weer 1 string wordt
    print("Jammer! Je hebt verloren. De geheime code is: " + "".join(geheime_code))
    return


# Spelletjes
opnieuw = "ja"
while opnieuw == "ja":
    start_een_spel()
    print("")
    opnieuw = input("Wil je nog opnieuw spelen? (ja/nee) ")

    

