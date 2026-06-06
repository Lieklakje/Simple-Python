import random

print("Hallo speler. Welkom bij het spel Mastermind. De computer genereert een code van 4 kleuren. De kleuren zijn: Rood (R), Groen (G), Blauw (B), Paars (P), Wit (W), Zwart (Z). Je hebt 10 pogingen om de correcte code te raden. Succes!")

R = "rood"
G = "groen"
B = "blauw"
P = "paars"
W = "wit"
Z = "zwart"

geheime_code = random.choices([R, G, B, P, W, Z], k=4)

poging = 0
while poging < 10:
    gok = input("Geef een code van 4 kleuren in (bijv. R G B P): ").upper().split()
    poging += 1
    print("Poging", poging)

    if gok == geheime_code:
        print("Gefeliciteerd, je hebt het goed!")
        break
    elif gok != geheime_code:
        print("Helaas, dat is niet correct. Probeer het opnieuw.")
