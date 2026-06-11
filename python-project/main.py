import random
print("Welkom bij het spel Mastermind. De computer genereert een code van 6 kleuren: Rood (R), Groen (G), Blauw (B), Paars (P), Wit (W), Zwart (Z). Vul de input in als x x x x of X X X X, waarbij x de eerste letter van de kleur is. Je hebt 10 pogingen om de correcte code te raden. Succes!")
print("")
print("")

R = "rood"
G = "groen"
B = "blauw"
P = "paars"
W = "wit"
Z = "zwart"

kleuren = {"R": R, "G": G, "B": B, "P": P, "W": W, "Z": Z}

geheime_code = random.choices([R, G, B, P, W, Z], k=4)
#print(geheime_code)
dih=input("a")
print(dih.split())
poging = 0
while poging < 10:
    poging += 1
    print("Poging", poging)
    gok = input("Voer een code van 4 kleuren in: ").upper().split()
    while len(gok) !=4 or not all(k in kleuren for k in gok):
        #'all' hebben we met behulp van AI leren gebruiken
        print("Foute invoer, probeer het opnieuw.")
        print("")
        #poging += 1
        #print("Poging", poging)
        gok = input("Voer een code van 4 kleuren in: ").upper().split()


    
    gok_kleuren = [kleuren[k] for k in gok]
    print("Je gok:", gok_kleuren)
    #print("Geheime code:", geheime_code)  

    goedePlaats = 0
    verkeerdePlaats = 0
# Z en W
    if gok_kleuren == geheime_code:
        print("Gefeliciteerd, je hebt het goed!")
        break

    elif gok_kleuren != geheime_code and poging!=10 :
        print("ZZW" + " - Probeer het opnieuw.")
        print("")

    else:
        print("Helaas, je hebt alle pogingen opgebruikt.")
        print("De geheime code was:", geheime_code)



