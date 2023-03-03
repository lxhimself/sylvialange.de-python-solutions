from random import randint

Zahl1 = randint(1,20)
Zahl2 = randint(1,20)

Richtig = 0
Falsch = 0
i = 1

while i <=10:
    print(f"Was ist {Zahl1} + {Zahl2}?")
    Ergebnis = int(input("---> "))

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
