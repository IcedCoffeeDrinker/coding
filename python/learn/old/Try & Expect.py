

# number = int(input("Gib eine Zahl ein: "))       # hier ein extra Fehler :( : "int" gibt einen Error bei Dezimalzahlen
# print(number)

try:
    number  = int(input("Gib eine Zahl ein: "))    # damit nicht das ganze Pogramm crasht kann man eine Alternatieve
    print(number)                                  # coden, die dann ausgeführt wird (try: ... expect:)
except:
    print("Ungültige Zahl!")


try:
    value = 10 /0                                  # hier haben wir das Problem, dass ein Rechenfehler
                                                   # und kein Eingabefehler besteht. Trozdem wird
    number  = int(input("Gib eine Zahl ein: "))    # "Ungültige Zahl" gedruckt
    print(number)
except:
    print("Ungültige Zahl!")


try:
    value = 10 /0

    number  = int(input("Gib eine Zahl ein: "))    # hier hat man Individuelle Lösungen für spezifische Fehler
    print(number)
except ValueError:
    print("Ungültige Zahl!")
except ZeroDivisionError as Error:                 # speichert Fehler als Variable
    print(Error)


# man solte immer spezifische Fehlerlösungen benutzen
