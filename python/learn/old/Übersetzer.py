'''
Giraffensprache:
Vocale -> g
--------------------

Hund -> Hgnd
Sushi -> Sgshg
'''

print()

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUÄÖÜ":
            translation += "G"
        elif letter in "aeiouäöü":
            translation += "g"
        else:
            translation += letter
    return translation

print(translate(input("Gib einen Satz ein: ")))