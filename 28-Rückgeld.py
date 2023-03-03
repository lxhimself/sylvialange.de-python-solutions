Geld = (input("Gib einen Euro und Cent Betrag ein, durch ein Leerzeichen getrennt (z.B. 184 23): "))
Einzeldaten = Geld.split(" ")

print(f"Sie müssen {Einzeldaten[0]} Euro und {Einzeldaten[1]} Cent zurück geben.")

Euros = int(Einzeldaten[0])
Cents = int(Einzeldaten[1])

Zweihunderter = 0
Einhunderter = 0
Fuenfziger= 0
Zwanziger = 0
Zehner = 0
Fuenfer = 0
Zweier = 0
Einer = 0

FuenfzigCent = 0 
ZwanzigCent = 0
ZehnCent = 0
FuenfCent = 0
ZweiCent = 0
EinCent = 0

while Euros >= 200:
    Euros -= 200
    Zweihunderter +=1

print (f"200er Scheine: {Zweihunderter}")

while Euros >= 100:
    Euros -=100
    Einhunderter +=1

print(f"100er Scheine: {Einhunderter}")

while Euros >= 50:
    Euros -=50
    Fuenfziger +=1

print(f"50er Scheine: {Fuenfziger}")

while Euros >= 20:
    Euros -=20
    Zwanziger +=1

print(f"20er Scheine: {Zwanziger}")

while Euros >= 10:
    Euros -=10
    Zehner +=1

print(f"10er Scheine: {Zehner}")

while Euros >= 5:
    Euros -=5
    Fuenfer +=1

print(f"5er Scheine: {Fuenfer}")

while Euros >= 2:
    Euros -=2
    Zweier +=1

print(f"2er Stücke: {Zweier}")

while Euros >= 1:
    Euros -=1
    Einer +=1

print(f"1er Stücke: {Einer}")

                                        # Cents Starten Hier

while Cents >= 50:
    Cents = Cents -50
    FuenfzigCent +=1

print(f"50cent Stücke: {FuenfzigCent}")

while Cents >= 20:
    Cents = Cents -20
    ZwanzigCent +=1

print(f"20cent Stücke: {ZwanzigCent}")

while Cents >= 10:
    Cents = Cents -10
    ZehnCent +=1

print(f"10cent Stücke: {ZehnCent}")

while Cents >= 5:
    Cents = Cents -5
    FuenfCent +=1

print(f"5cent Stücke: {FuenfCent}")

while Cents >= 2:
    Cents = Cents -2
    ZweiCent +=1

print(f"2cent Stücke: {ZweiCent}")


while Cents >= 1:
    Cents = Cents -1
    EinCent +=1

print(f"1cent Stücke: {EinCent}")