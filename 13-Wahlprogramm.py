Kanditat1 = str(input("Name des ersten Kanditaten: "))
Stimmen1 = float(input("Wie viele Stimmen für Nr.1: "))
Kanditat2 = str(input("Name des zweiten Kanditaten: "))
Stimmen2 = float(input("Wie viele Stimmen für Nr.2: "))
Kanditat3 = str(input("Name des dritten Kanditaten: "))
Stimmen3 = float(input("Wie viele Stimmen für Nr.3: "))

StimmenMax = Stimmen1 + Stimmen2 + Stimmen3

Stimmen1Anteil = Stimmen1*100/StimmenMax
Stimmen2Anteil = Stimmen2*100/StimmenMax
Stimmen3Anteil = Stimmen3*100/StimmenMax

if Stimmen1Anteil > Stimmen2Anteil and Stimmen1Anteil > Stimmen2Anteil:
    print(f"Sieger ist: {Kanditat1} mit {Stimmen1Anteil}% der Stimmen.")
    print(f"{Kanditat2} steht bei {Stimmen2Anteil}% und {Kanditat3} steht bei {Stimmen3Anteil}%")

elif Stimmen2Anteil > Stimmen1Anteil and Stimmen2Anteil > Stimmen3Anteil:
    print(f"Sieger ist: {Kanditat2} mit {Stimmen2Anteil}% der Stimmen.")
    print(f"{Kanditat1} steht bei {Stimmen1Anteil}% und {Kanditat3} steht bei {Stimmen3Anteil}%")
    
elif Stimmen3Anteil > Stimmen1Anteil and Stimmen3Anteil > Stimmen2Anteil:
    print(f"Sieger ist: {Kanditat3} mit {Stimmen3Anteil}% der Stimmen.")
    print(f"{Kanditat1} steht bei {Stimmen1Anteil}% und {Kanditat2} steht bei {Stimmen2Anteil}%")
