
ist_männlich = False

if ist_männlich:                                          # if ist das Schlüsselwort
    print("Du bist ein Junge oder ein Mann.")             # wird nur ausgeführt wenn "ist_männlich" wahr ist
else:
    print("Du bist ein Mädchen oder eine Frau")           # mit "else" wird etaws anderes ausgeführt,
                                                          # wenn "ist_mänlich falsch ist

ist_groß = False
ist_männlich = False

if ist_männlich or ist_groß:                              # mit "or" muss nur eine der Variablen wahr sein
    print("Du bist ein Mann oder groß oder beides. :b")
else:
    print("Du bist kein Mann und auch nicht groß.")

print()

if ist_männlich and ist_groß:                             # mit "and" müssen beide Variablen wahr sein
    print("Du bist ein großer Mann!")
elif ist_männlich and not(ist_groß):                      # "elif" = else + neue Bedingung
    print("Du bist ein kleiner Mann!")                     # "not" verneint die Variable
elif not(ist_männlich) and ist_groß:
    print("Du bist eine große Frau!")
elif not(ist_männlich) and not(ist_groß):
    print("Du bist eine kleine Frau!")
else:
    print("Wie hast du das gehackt!?")


