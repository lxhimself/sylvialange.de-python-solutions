Breite = float(input("Breite in m: "))
Höhe = float(input("Höhe in m: "))
Länge = float(input("Länge in m: "))

Volumen = Breite*Höhe*Länge
Oberfläche = 2*Breite*Höhe + 2*Länge*Höhe + 2*Breite*Länge
Raumdiagonale = (Breite**2 + Höhe**2 + Länge**2)**0.5




if Volumen < 0 or Oberfläche < 0 or Raumdiagonale < 0:
    print("Negativ kann ja wohl nicht sein.")

else:
    print(f"""Dein Quader hat folgende Eigenschaften:
    Volumen: {Volumen} m3
    Oberfläche: {Oberfläche} m2
    Raumdiagonale: {Raumdiagonale} m""")
    

