print()                   # Leehre Zeile
print("Giraffe Academy")
print("Giraffe\nAcademy") # Absatz (es geht auch \" )

Satz = "Hallo, was geht?"    # Satz als Variabale
print(Satz)

print(Satz + " Alles!")       # Variable + String
print(Satz , "Alles")       # Variable, Sting (getrente Werte)

print("Hi! " + Satz + " Alles!") # String + Variable + String

print(Satz.lower())        # druckt Satz in Kleinbuchstaben
print(Satz.upper())        # druckt Satz in großbuchstaben

print(Satz.isupper())      # druckt Satz nur wenn alles groß geschrieben ist
print(Satz.upper().isupper()) # combination

print(len(Satz))         # hat anzahl der Zeichen von Satz als output

print(Satz[0])           # hat das Zeichen an jeweiliger Stelle als output (0 = Satzanfang)

print(Satz.index("l"))   # guckt an welcher Stelle in Satz ein Zeichen oder ein String ist
print(Satz.index("was"))

print(Satz.replace("geht", "läuft"))      # ersetzt "geht" mit "läuft"
