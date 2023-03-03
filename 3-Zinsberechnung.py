Betrag = input("Dein Betrag: ")
Zinssatz = input("Dein Zinssatz pro Monat in Prozent: ")
Monate = input("Über wie viele Monate: ")
ZinssatzInProzent = float(float(Zinssatz)/100)

Zinsen = int(Betrag) * float(ZinssatzInProzent) * int(Monate)

print(f"Deine Zinsen über {Monate} Monate betragen {Zinsen} Euro.")
