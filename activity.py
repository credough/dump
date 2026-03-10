import random

while True:
 gender = random.randint(1,10)

 g = str(input("Enter name:"))
 if g == "stop":
    break

 if gender % 2 == 0:
    print("BADING!")
 else:
    print("LALAKI AKO")

 
 
