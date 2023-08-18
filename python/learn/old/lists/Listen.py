freund1 = "Jonte"
freund2 = "Anton"
freund3 = "Lenny"
freund4 = "Vincent"

freunde = [freund1, freund2, freund3, freund4]

print()
print(freunde[0])       # druckt den Namen an jeweiliger Stelle (negative Zahlen zählen von Hinten)
print(freunde[1:])      # druckt alle Namen von der eingegebenen Stelle bis zur letzten
print(freunde[1:2])     # druckt alle Namen von Stelle 1 bis 3
print()
freunde[1] = "Leo"      # endert Namen an der 1. Stelle zu Leo

Glückszahlen = [4, 8, 15, 16, 23, 42]
freunde.append("Jakob")                   # fügt "Jakob" zu "freunde" hinzu
freunde.insert(2, "LOL")                  # setzt etwas vor die angegebene Stelle in die Liste ein
freunde.extend(Glückszahlen)              # kombiniert "Glückszahlen" mit "freunde"
freunde.remove("LOL")                     # löscht etwas aus der Liste
freunde.pop()                             # löscht das letzte Teil aus der Liste
print(freunde)
print(freunde.index("Lenny"))             # guckt an welcher Stelle "Lenny" steht
freunde.clear()  # löscht den Inhalt

freunde = ["Anton", "Anton", "Florian"]

print(freunde.count("Anton"))        # zählt wie oft Anton in der Liste steht
freunde.sort()                       # sortiert die Liste nach Alpabet und Zahlenreinfolge ("reverse" macht das Gegenteil)
print(freunde)

freunde2 = freunde.copy()            # kopiert "freunde" in "freunde2" why ever mit .copy
print(freunde2)

print(len(freunde))                  # fruckt wie viele Daten sich in "freunde" befinden
