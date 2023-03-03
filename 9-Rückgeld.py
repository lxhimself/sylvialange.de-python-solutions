Preis = float(input("Was koschts in Euro? "))
Bezahlt = float(input("Welcher Euroschein fladdert rübber? "))
Rueckgeld = Bezahlt - Preis 


if Bezahlt > Preis:
    print(f"Dein Wechselgeld: {Rueckgeld}")
elif Bezahlt == Preis:
    print("Passt jenau danke")
else:
    print("Dit reicht nich, sorry")