
def max_num(num1, num2, num3):                                     # man kann auch strings und Bulienwerte abfragen
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

inp1 = float(input("Zahl1: "))
inp2 = float(input("Zahl2: "))
inp3 = float(input("Zahl3: "))

print(max_num(inp1, inp2, inp3))