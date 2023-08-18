from math import *

print(2)
print(3.14156)
print(-1.465165)

# Rechnungsopperratoren oder sowas

print(3 + 4)
print(4 - 3)
print(4 * 3)
print(9 / 3)

print(9 < 4)
print(9 > 4)
print(9 <= 4)
print(9 >= 4)
print(9 == 4)
print(9 != 4)

#Variablen:

i = 1
i = i + 1
i += 1         # Abkürzung !!!!!!!


print(10 % 3) # Rest als output

# Klammern und so...

print(10 * (4 + 1))

# Funktionen:

print(abs(-8))    # hat die absolute Zahl als output
print(pow(3, 2))    # hoch Rechnungen
print(max(4, 5))    # guckt welche Zahl größer ist
print(round(3.2))   # rundet Zahlen

# Functionen möglich mit Modul Import (from math import *)

print(floor(6.751))  # löscht alle Stellen hinter dem Komma
print(ceil(6.751))   # rundet Zahl auf Einer
print(sqrt(36))      # Quadratwurzel oder so vielleicht auch nur Wurzel
                     # ist da ein unterschied?


num1 = 7
num2 = 5
erge = float(num1) + float(num2)            # float konvertiert eine Variable in eine Zahl
                                            # int geht auch aber nur für ganze Zahlen
print(erge)


# Zahl in string konvertieren:

Zahl = 8
print(str(Zahl) + " ist meine Lieblingszahl")

# Zahl in intiger convertieren
float = erge
int = int(float)
variable = int(input("Zahl: "))

# Bereich von 3-10 (10 wird nicht gedruckt) / "range" ist najy halt die range von 3 bis 10 ohne 10

for index in range(3, 10):
    print(index)
