# Funktionen sind eine Zusammenfassung von code

def say_hi () :                # def ist das Schlüsselwort für eine Funktion
    print("Hallo, Benutzer!")                       # nur der versetzte Text ist in der Funxion

say_hi()                       # so führt man eine Funktion aus, hoffe ich

print()
print("oben")
say_hi()                  # soll demonstrieren dass "say_hi" hier und nicht weiter oben ausgeführt wird
print("unten")
print()

def hi_name (name):
    print("Hi " + name + "!")               # man kann Variablen extra leicht in Funktionen einfügen

hi_name("Philipp")


def hi_name_alter (name, alter):
    print("Du heißt " + name + ", und bist "+ str(alter) + " Jahre alt.")      # es gehen auch mehrere Variablen, ok?

hi_name_alter("Philipp", 13)

variable = 0
# -----------------------
def function(x):
    number = x+1
    return number
print(function(function(10)))
