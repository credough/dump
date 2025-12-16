import random

choices = ["Red", "Green", "Blue"]

user = input("Choose color(Red, Green, Blue)")

computer = random.choice(choices)

print("Computer chose:", computer)

if user == computer:
    print("Match!")

else:
    print("Not match!")

