Laenge = float(input("Länge des Grundstücks in Metern: "))
Breite = float(input("Breite des Grundstücks in Metern: "))
QMPreis = float(input("Quadratmeterpreis in Euro: "))
Provision = float(input("Provisionssatz des Maklers in Prozent: "))
UST = 1.19

Grundstueckspreis = Laenge * Breite * QMPreis * UST
Maklerprovision = Grundstueckspreis * (Provision / 100)
Gesamt = Grundstueckspreis + Maklerprovision

print(f"""Das Grundstück kostet {Grundstueckspreis} €
Der Makler bekommt zusätzlich {Maklerprovision} €
Die Kacke kostet dich also insgesamt {Gesamt} €
""")