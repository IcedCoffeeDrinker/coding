# es gibt verschiedene Modies:

# open("text", "r")       # mit "r" liest man eine Datei
# open("text", "w")       # mit "w" schreibt man in eine Datei
# open("text", "a")       # mit "a" kann man einer Datei nur Sachen hinzufügen und nicht verendern
# open("text", "r+")      # mit "r+" kann man lesen und schreiben


file_inhalt = open("text", "r")

print(file_inhalt.readable())          # druckt ob Datei lesbar ist

print(file_inhalt.read())              # druckt den Dateiinhalt
print(file_inhalt.readline())          # druckt erste Zeile
print(file_inhalt.readline())          # druckt zweite Zeile
#print(file_inhalt.readlines()[1])     # druckt aus einer Datei wie aus einer Liste (eine Spalte = ein Wert)
                                       # gibt aber in Kombination mit ".read" irgendwie ein Error
print()
print()

Dateinhalt = open("text", "r")
for inhalt in Dateinhalt.readlines():
    print(inhalt)

file_inhalt.close()                    # schließt eine Datei (dann wird auch der Modus zurückgesetzt) sollte man immer
