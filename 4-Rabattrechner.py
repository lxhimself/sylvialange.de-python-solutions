Preis = float(input("Dein Preis: "))
Rabatt = float(input("Dein Rabatt in Prozent: "))
Endpreis = Preis - Preis*Rabatt/100

print(f"Dein Endpreis ist {Endpreis} Euro.")