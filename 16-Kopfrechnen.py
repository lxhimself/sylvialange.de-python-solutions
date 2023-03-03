from random import randint

Zahl1 = randint(1,20)
Zahl2 = randint(1,20)

print(f"Was ist {Zahl1} + {Zahl2}?")

Ergebnis = int(input("---> "))


if Ergebnis == Zahl1 + Zahl2:
    print("Nice Job, das stimmt!")
    
else:
    print(f"Das ... war nix. Richtig ist {Zahl1 + Zahl2} ")
