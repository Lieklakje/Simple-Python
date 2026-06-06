import random

print("Hallo speler. Welkom bij het spel Mastermind. De computer genereert een code van 4 kleuren. De kleuren zijn: Rood (R), Groen (G), Blauw (B), Paars (P), Wit (W), Zwart (Z). Je hebt 10 pogingen om de correcte code te raden. Succes!")

R = "rood"
G = "groen"
B = "blauw"
P = "paars"
W = "wit"
Z = "zwart"

kleuren = {"R": R, "G": G, "B": B, "P": P, "W": W, "Z": Z}

geheime_code = random.choices([R, G, B, P, W, Z], k=4)

poging = 0
while poging < 10:
    print(f"\nPoging {poging + 1} van 10")
    gok = input("Geef een code van 4 kleuren in (bijv. R G B P): ").upper().split()

    if len(gok) != 4 or not all(k in kleuren for k in gok):
        print("Ongeldige invoer. Gebruik de letters R, G, B, P, W of Z, gescheiden door spaties.")
        continue

    gok_kleuren = [kleuren[k] for k in gok]

    if gok_kleuren == geheime_code:
        print(f"Gefeliciteerd! Je hebt de geheime code geraden in {poging + 1} pogingen!")
        break

    poging += 1
    print(f"Jouw gok: {gok_kleuren}")
    print(f"Nog {10 - poging} pogingen over.")
else:
    print(f"\nGame over! De geheime code was: {geheime_code}")
