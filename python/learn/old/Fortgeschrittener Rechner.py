
print()

num1 = float(input("Gib die erste Zahl ein: "))
op = input("Gib den Operator ein: ")
num2 = float(input("Gib die zweite Zahl ein: "))

print()

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("fail")