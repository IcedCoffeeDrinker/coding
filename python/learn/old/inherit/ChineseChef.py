from Chef import Chef

class ChineseChef(Chef):                      # man kann in Klammern andere Klassivizierungen einfügen

    def make_special_dish(self):              # man kann auch überschreiben oder hinzufügen
        print("The chef makes orange chicken")

    def make_fried_rice(self):
        print("The chef makes fried rice")