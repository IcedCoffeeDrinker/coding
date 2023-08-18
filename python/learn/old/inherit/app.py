from Chef import Chef                                  # man kann Module in andere Module einbringen
from ChineseChef import ChineseChef                    # und Teile überschreiben
print("Chef:")                                         # mehr dazu bei ChineseChef.py

myChef = Chef()                                        # als Erstes muss eine Variable definiert werden

myChef.make_chicken()                                  # dann können die Inhalte mit einem operator oder so
myChef.make_special_dish()                             #  aufgerufen werden

print("Chinaman:")

myChineseChef = ChineseChef()

myChineseChef.make_chicken()
myChineseChef.make_special_dish()
