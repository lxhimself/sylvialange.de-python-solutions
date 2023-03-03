Sekunden = int(input("Gib die Sekunden an: "))

Jahre = 0
Tage = 0
Stunden = 0
Minuten = 0

while Sekunden >= 60:
    Sekunden -= 60
    Minuten += 1

while Minuten >= 60:
    Minuten -= 60
    Stunden +=1

while Stunden >= 24:
    Stunden -= 24
    Tage +=1

while Tage >= 365:
    Tage -= 365
    Jahre += 1


print(f"Das sind {Jahre} Jahre, {Tage} Tage, {Stunden} Stunden, {Minuten} Minuten und {Sekunden} Sekunden.")



