# Controlestructuren

# If-else statement
leeftijd = int(input("Hoe oud ben je? "))

if leeftijd >= 18:
    print("Je bent volwassen.")
else:
    print("Je bent minderjarig.")

# While loop
teller = 1
while teller <= 5:
    print("Teller:", teller)
    teller += 1

# For loop
getallen = [1, 2, 3, 4, 5]
for nummer in getallen:
    print("Getal:", nummer)