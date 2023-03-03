n = int(input("n = "))

ergebnis = 1

for i in range(1, 1+n):
    ergebnis = ergebnis * i 

print(f"Fakultät von {n} = {ergebnis}")
