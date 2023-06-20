# Bestandsverwerking

# Bestand openen in leesmodus
bestandsnaam = "mijn_bestand.txt"
bestand = open(bestandsnaam, "r")

# Inhoud van het bestand lezen
inhoud = bestand.read()

# Het aantal regels in het bestand tellen
aantal_regels = len(inhoud.split("\n"))

# Het aantal woorden in het bestand tellen
aantal_woorden = len(inhoud.split())

# Het aantal tekens in het bestand tellen
aantal_tekens = len(inhoud)

# Het bestand sluiten
bestand.close()

# Resultaten weergeven
print("Bestandsnaam:", bestandsnaam)
print("Aantal regels:", aantal_regels)
print("Aantal woorden:", aantal_woorden)
print("Aantal tekens:", aantal_tekens)