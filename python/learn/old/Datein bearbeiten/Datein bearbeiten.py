
dateinhalt = open("lololol", "r")
print(dateinhalt.read())
dateinhalt.close()

dateinhalt = open("lololol", "a")
dateinhalt.write("\nLOL LOL")               # "\n" schreibt in einen neuen Absatz
dateinhalt.close()

dateinhalt = open("lololol", "w")           # mit "w" überschreibt man die ganze Datei
print(dateinhalt.write("LOL LOL LOL"))
dateinhalt.close()

dateinhalt = open("lol.html", "w")           # wenn man eine nicht existierende Datei angibt wird eine neue erstellt
print(dateinhalt.write("<p>Das hier ist HTML</p>"))
dateinhalt.close()
