monthConversions = {
    "Jan": "Januar",
    "Feb": "Februar",                  # man benutzt dictionarys wenn man Datenpaare hat
    "Mär": "März",                     # man kann strings Werte und Bulienwerte benutzen
    "Apr": "April",
    "Mai": "Mai",
    "Jun": "Juni",
    "Jul": "Juli",
    "Aug": "August",
    "Sep": "September",
    "Okt": "Oktober",
    "Nov": "November",
    "Dez": "Dezember",
}

print()
inp = input("Die ersten drei Buchstaben eines Monats: ")
print()
# print(monthConversions[inp])                einfachste Möglichkeit für output
print(monthConversions.get(inp, "fail"))              # fortgeschrittene Wariante (.get hat die möglichkeit
                                                      # alternatieve Sachen zu drucken


