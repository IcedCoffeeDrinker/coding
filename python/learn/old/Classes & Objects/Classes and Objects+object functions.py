# man hat die Möglichkeit eigene Datentypen zu erstellen (z.B. die Werte eines Studenten)
#wie das weiß ich zu diesem Zeitpunkt noch nicht aber es wird sicher gleich hier drunter stehen :D

from Stundent import Student

student1 = Student("Jimmy", "Lappen", 5.6, True)     # ich habe in Student.py die Regeln für den Wert "Student" erstellt
student2 = Student("the king", "Pro", 1.0, False)    # nach diesen Regeln hab ich hier einen wirklichen unwirklichen
                                                     # Studenten erstellt
print(student1.name)
print(student2.rang)

# Informationen bei "Student.py"

print(student2.is_legendarry())