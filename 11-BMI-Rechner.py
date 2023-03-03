Groesse = float(input("Größe in cm: "))
Gewicht = float(input("Gewicht in kg: "))
Geschlecht = str(input("m oder w? "))

BMI = Gewicht/((Groesse/100)**2)

if Geschlecht == "m":
    if BMI >= 20 and BMI <= 25:
        print(f"Dein BMI ist gesund, mit einem Wert von {BMI}")
    elif BMI >25:
        print(f"Zu fett, Bruder: {BMI}")
    elif BMI <20:
        print(f"Zu skinny, Bruder: {BMI}")

if Geschlecht == "w":
    if BMI >= 19 and BMI <= 24:
        print(f"Dein BMI ist gesund, mit einem Wert von {BMI}")
    elif BMI >24:
        print(f"Zu fett, Schwester: {BMI}")
    elif BMI <20:
        print(f"Zu skinny, Schwester: {BMI}")



if Geschlecht != "m" and Geschlecht != "w":
    print("Wir können nur m & w sorry")


