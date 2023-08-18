#So erstellt man einen eigenen Datentypen oder sowas ähnliches:

class Student:
    def __init__(self, name, rang, noten, ist_dumm):
        self.name = name
        self.rang = rang
        self.noten = noten
        self.ist_dumm = ist_dumm

# Wenn note <= backfish (1) dann ist "is_legendarry = True

    def is_legendarry(self):
      if self.noten <= 1:
        return True
      else:
        return False