from random import randint

Zahl1 = randint(1,20)
Zahl2 = randint(1,20)

Richtig = 0
Falsch = 0
i = 1

print("Addition üben:")

while i <=10:
    Ergebnis = int(input(f"Aufgabe {i}:    {Zahl1} + {Zahl2} = "))
    
    if Ergebnis == Zahl1 + Zahl2:
        print("Nice Job, das stimmt!")
        Zahl1 = randint(1,20)
        Zahl2 = randint(1,20)
        Richtig +=1
        i +=1
        
    else:
        print(f"Das ... war nix. Richtig ist {Zahl1 + Zahl2} ")
        Zahl1 = randint(1,20)
        Zahl2 = randint(1,20)
        Falsch +=1
        i +=1

print(f"""Richtige Antworten: {Richtig}
Falsche Antworten: {Falsch}""")

