Preis = float(input("Dein Preis: "))
Rabatt = float(input("Dein Rabatt in Prozent: "))
Endpreis = Preis - Preis*Rabatt/100

if Rabatt > 100:
    print("Ich bezahl dich noch oder was? Verpiss dich")
elif Rabatt == 100:
    print("Geschenkt oder was? Verpiss dich")
else:
    print(f"Dein Endpreis ist {Endpreis} Euro.")