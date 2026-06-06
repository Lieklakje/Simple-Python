import random
print("Hallo speler. Welkom bij het spel Mastermind. De computer genereert een code van 4 kleuren. De kleuren zijn: Rood (R), Groen (G), Blauw (B), Paars (P), Wit (W), Zwart (Z). Je hebt 10 pogingen om de correcte code te raden. Succes!")

R = "rood"
G = "groen"
B = "blauw"
P = "paars"
W = "wit"
Z = "zwart"

geheime_code = random.choices([R, G, B, P, W, Z], k=4)
print(geheime_code)

print(input("Geef een code van 4 kleuren in: "))

poging = 0
while poging < 10:
    print("Poging", poging + 1)