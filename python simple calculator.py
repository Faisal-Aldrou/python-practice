a = int(input())
b = int(input())
c = input("enter operator: ")
if c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
elif c == "*":
    print(a * b)
elif c == "/":
    print(a / b)
elif c == "%":
    print(a % b)
else:
    print("unknown operator")

