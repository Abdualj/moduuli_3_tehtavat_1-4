# Ohjelma kysyy kalastajalta kuhan pituuden
kuhan_pituus = float(input("Anna kuhan pituus senttimetreinä: "))

# Määritellään alimmainen sallittu pituus (37 cm)
alamitta = 37

# Tarkistetaan, onko kuha alamittainen
if kuhan_pituus < alamitta:
    puuttuu = alamitta - kuhan_pituus
    print(f"Kuha on alamittainen. Laske kuha takaisin järveen. Pituudesta puuttuu {puuttuu:.1f} cm.")
else:
    print("Kuha on sallittua pyyntimittaa suurempi.")
