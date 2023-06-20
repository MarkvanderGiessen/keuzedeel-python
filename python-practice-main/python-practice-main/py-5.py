# Gegevensstructuren

# Lijst
dagen_van_de_week = ["Maandag", "Dinsdag", "Woensdag", "Donderdag", "Vrijdag", "Zaterdag", "Zondag"]

print("De dagen van de week zijn:")
for dag in dagen_van_de_week:
    print(dag)

# Tuple
coördinaten = (3, 4)
x, y = coördinaten

print("De x-coördinaat is:", x)
print("De y-coördinaat is:", y)

# Dictionaire
telefoonboek = {
    "Jan": 123456789,
    "Piet": 987654321,
    "Klaas": 456789123
}

print("Het telefoonnummer van Jan is:", telefoonboek["Jan"])
print("Het telefoonnummer van Klaas is:", telefoonboek["Klaas"])