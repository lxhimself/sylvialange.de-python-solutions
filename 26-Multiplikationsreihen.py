Reihe = int(input("Welche Reihe: "))
Laenge = int(input("Wie weit: "))

for i in range(1, Laenge+1):
    print(f"{i} x {Reihe} = {i*Reihe}")