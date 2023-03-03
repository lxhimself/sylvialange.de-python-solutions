Bugs = int(input("Wie viele Käfer zu Beginn? "))
RaumVolumen = int(input("Volumen des Raums? z.B. 3m Kantenlänge wären 27m3 "))

Woche = 1

while Bugs * 0.0002 < RaumVolumen:
    print(f"Bugs nach {Woche} Woche: {Bugs}")
    Woche += 1
    Bugs = Bugs * 1.95

    
