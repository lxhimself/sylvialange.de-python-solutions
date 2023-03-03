n = int(input("Zahl, bitte: "))

x = 1

while (x*x) <= n:
    x += 1

print (f"Die näheste Zweiterpotenz zu {n} ist {(x-1)**2} mit der Basis {x-1}")