# Kysytään käyttäjältä sukupuoli ja hemoglobiiniarvo
sukupuoli = input("Anna biologinen sukupuoli (nainen/mies): ").lower()
hemoglobiini = float(input("Anna hemoglobiiniarvo (g/l): "))

# Tarkistetaan sukupuoli ja määritellään hemoglobiiniarvon rajat
if sukupuoli == "nainen":
    if hemoglobiini < 117:
        print("Hemoglobiiniarvo on alhainen.")
    elif 117 <= hemoglobiini <= 175:
        print("Hemoglobiiniarvo on normaali.")
    else:
        print("Hemoglobiiniarvo on korkea.")
elif sukupuoli == "mies":
    if hemoglobiini < 134:
        print("Hemoglobiiniarvo on alhainen.")
    elif 134 <= hemoglobiini <= 195:
        print("Hemoglobiiniarvo on normaali.")
    else:
        print("Hemoglobiiniarvo on korkea.")
else:
    print("Virheellinen sukupuoli.")
