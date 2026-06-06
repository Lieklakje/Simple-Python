import random

R = "rood"
G = "groen"
B = "blauw"
P = "paars"
W = "wit"
Z = "zwart"

input("Hallo speler. Welkom bij het spel Mastermind. De computer genereert een code van 4 kleuren. De kleuren zijn: Rood (R), Groen (G), Blauw (B), Paars (P), Wit (W), Zwart (Z). Je hebt 10 pogingen om de correcte code te raden. Druk op Enter om te beginnen. Succes!")

geheime_code = random.choices([R, G, B, P, W, Z], k=4)
