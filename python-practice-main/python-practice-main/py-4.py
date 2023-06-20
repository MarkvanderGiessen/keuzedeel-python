# Functies en modules

# Functie voor het berekenen van de omtrek van een cirkel
def bereken_omtrek(r):
    omtrek = 2 * 3.14 * r
    return omtrek

# Functie voor het berekenen van de oppervlakte van een cirkel
def bereken_oppervlakte(r):
    oppervlakte = 3.14 * (r ** 2)
    return oppervlakte

# Gebruiker invoer
radius = float(input("Voer de straal van de cirkel in: "))

# Omtrek berekenen en weergeven
omtrek = bereken_omtrek(radius)
print("De omtrek van de cirkel is:", omtrek)

# Oppervlakte berekenen en weergeven
oppervlakte = bereken_oppervlakte(radius)
print("De oppervlakte van de cirkel is:", oppervlakte)