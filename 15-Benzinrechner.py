Literpreis = float(input("Was koscht der Litter grat? "))
Verbraucht = float(input("Wie viele Litter haste durchgejagt? "))
Kilometer = float(input("Wie viele Killomeder haste geschafft? "))

VerbrauchPro100 = Verbraucht / (Kilometer/100)
PreisPro100 = VerbrauchPro100 * Literpreis 
PreisGesamtstrecke = Literpreis * Verbraucht

print(f"""Verbrauch pro 100 km: {VerbrauchPro100} l
Preis pro 100 km: {PreisPro100} €)
Preis der Strecke: {PreisGesamtstrecke} €""")