import random
a = random.randint(1, 100)
b = None
while b != a:
    b = int(input("Guess the number between 1 and 100"))
    if b < a:
        print("too low")
    elif b > a: 
        print("too high")
    else:
        print("correct")

     